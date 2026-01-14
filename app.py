import gradio as gr
from answer import answer_question

# ---------- Helper: format retrieved chunks ----------
def format_chunks(chunks):
    if not chunks:
        return "No knowledge-base retrieval was required for this question."

    formatted = []
    for i, doc in enumerate(chunks, 1):
        source = doc.metadata.get("source", "unknown")
        text = doc.page_content.strip()

        formatted.append(
            f"### Chunk {i}\n"
            f"**Source:** {source}\n\n"
            f"{text}"
        )

    return "\n\n---\n\n".join(formatted)



# ---------- Chat handler (Dictionary Format) ----------
def chat_handler(message, chat_history):
    """
    Inputs:
        message: str
        chat_history: List of dicts [{'role': 'user', 'content': '...'}, ...]
    """
    # Initialize if None
    chat_history = chat_history or []

    # 1. Build history string for your RAG backend
    #    (We must handle the dict format here)
    history_text = ""
    for msg in chat_history:
        # Check if msg is a dict (robustness)
        if isinstance(msg, dict):
            role = msg.get("role", "User")
            content = msg.get("content", "")
            history_text += f"{role.capitalize()}: {content}\n"
        # Fallback for tuples just in case mixed history occurs
        elif isinstance(msg, (list, tuple)) and len(msg) == 2:
            history_text += f"User: {msg[0]}\nAssistant: {msg[1]}\n"

    # 2. Get answer + retrieved chunks
    answer, chunks = answer_question(message, history_text)

    # 3. Update Chat History (DICTIONARY format required by your error)
    chat_history.append({"role": "user", "content": message})
    chat_history.append({"role": "assistant", "content": answer})

    # 4. Format chunks for display
    chunk_display = format_chunks(chunks)

    # Return: Updated History, Chunks, Clear Input
    return chat_history, chunk_display, ""


# ---------- Gradio UI ----------
with gr.Blocks(title="BlinkNow – DSA RAG Assistant", theme=gr.themes.Soft()) as demo:

    gr.Markdown(
        """
        # 📘 BlinkNow – Data Structures & Algorithms Assistant
        Ask a DSA question and see the **retrieved knowledge chunks** used to generate the answer.
        """
    )

    with gr.Row():
        # Left Column: Chat Interface
        with gr.Column(scale=2):
            # We do NOT pass type="messages" here to avoid the __init__ error,
            # but we WILL pass dictionary data to satisfy the runtime error.
            chatbot = gr.Chatbot(
                label="Chat",
                height=500
            )

            with gr.Row():
                user_input = gr.Textbox(
                    placeholder="Ask a DSA question...",
                    label="Your Question",
                    scale=4
                )
                send_btn = gr.Button("Send", variant="primary", scale=1)

        # Right Column: Retrieval Viewer
        with gr.Column(scale=3):
            gr.Markdown("### 🔍 Retrieved Context")
            retrieved_chunks = gr.Markdown(
                value="*Retrieved knowledge chunks will appear here after your query.*"
            )

    # ---------- Event Handling ----------
    send_btn.click(
        fn=chat_handler,
        inputs=[user_input, chatbot],
        outputs=[chatbot, retrieved_chunks, user_input]
    )

    user_input.submit(
        fn=chat_handler,
        inputs=[user_input, chatbot],
        outputs=[chatbot, retrieved_chunks, user_input]
    )

if __name__ == "__main__":
    demo.launch(
        share=True,
        inbrowser=True
    )