# Chapter

3

# LINKED LISTS

*In this chapter, the list data structure is presented. This structure can be used as the basis for the implementation of other data structures (stacks, queues etc.). The basic linked list can be used without modification in many programs. However, some applications require enhancements to the linked list design. These enhancements fall into three broad categories and yield variations on linked lists that can be used in any combination: circular linked lists, double linked lists and lists with header nodes.*

Linked lists and arrays are similar since they both store collections of data. Array is the most common data structure used to store collections of elements. Arrays are convenient to declare and provide the easy syntax to access any element by its index number. Once the array is set up, access to any element is convenient and fast. The disadvantages of arrays are:

- The size of the array is fixed. Most often this size is specified at compile time. This makes the programmers to allocate arrays, which seems "large enough" than required.
- Inserting new elements at the front is potentially expensive because existing elements need to be shifted over to make room.
- Deleting an element from an array is not possible.

Linked lists have their own strengths and weaknesses, but they happen to be strong where arrays are weak. Generally array's allocates the memory for all its elements in one block whereas linked lists use an entirely different strategy. Linked lists allocate memory for each element separately and only when necessary.

Here is a quick review of the terminology and rules of pointers. The linked list code will depend on the following functions:

malloc() is a system function which allocates a block of memory in the "heap" and returns a pointer to the new block. The prototype of malloc() and other heap functions are in stdlib.h. malloc() returns NULL if it cannot fulfill the request. It is defined by:

```
void *malloc (number_of_bytes)
```

Since a void \* is returned the C standard states that this pointer can be converted to any type. For example,

```
char *cp;
cp = (char *) malloc (100);
```

Attempts to get 100 bytes and assigns the starting address to cp. We can also use the sizeof() function to specify the number of bytes. For example,

```
int *ip;
ip = (int *) malloc (100*sizeof(int));
```

free() is the opposite of malloc(), which de-allocates memory. The argument to free() is a pointer to a block of memory in the heap a pointer which was obtained by a malloc() function. The syntax is:

*free (ptr);*

The advantage of free() is simply memory management when we no longer need a block.

# 3.1. Linked List Concepts:

A linked list is a non-sequential collection of data items. It is a dynamic data structure. For every data item in a linked list, there is an associated pointer that would give the memory location of the next data item in the linked list.

The data items in the linked list are not in consecutive memory locations. They may be anywhere, but the accessing of these data items is easier as each data item contains the address of the next data item.

# Advantages of linked lists:

Linked lists have many advantages. Some of the very important advantages are:

- 1. Linked lists are dynamic data structures. i.e., they can grow or shrink during the execution of a program.
- 2. Linked lists have efficient memory utilization. Here, memory is not preallocated. Memory is allocated whenever it is required and it is de-allocated (removed) when it is no longer needed.
- 3. Insertion and Deletions are easier and efficient. Linked lists provide flexibility in inserting a data item at a specified position and deletion of the data item from the given position.
- 4. Many complex applications can be easily carried out with linked lists.

#### Disadvantages of linked lists:

- 1. It consumes more space because every node requires a additional pointer to store address of the next node.
- 2. Searching a particular element in list is difficult and also time consuming.

#### 3.2. Types of Linked Lists:

Basically we can put linked lists into the following four items:

- 1. Single Linked List.
- 2. Double Linked List.
- 3. Circular Linked List.
- 4. Circular Double Linked List.

A single linked list is one in which all nodes are linked together in some sequential manner. Hence, it is also called as linear linked list.

A double linked list is one in which all nodes are linked together by multiple links which helps in accessing both the successor node (next node) and predecessor node (previous node) from any arbitrary node within the list. Therefore each node in a double linked list has two link fields (pointers) to point to the left node (previous) and the right node (next). This helps to traverse in forward direction and backward direction.

A circular linked list is one, which has no beginning and no end. A single linked list can be made a circular linked list by simply storing address of the very first node in the link field of the last node.

A circular double linked list is one, which has both the successor pointer and predecessor pointer in the circular manner.

# Comparison between array and linked list:

| ARRAY                                                                                                                                 | LINKED LIST                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Size of an array is fixed                                                                                                             | Size of a list is not fixed                                                                                                    |
| Memory is allocated from stack                                                                                                        | Memory is allocated from heap                                                                                                  |
| It is necessary to specify the number of<br>elements during declaration (i.e., during<br>compile time).                               | It is not necessary to specify the<br>number of elements during declaration<br>(i.e., memory is allocated during run<br>time). |
| It occupies less memory than a linked<br>list for the same number of elements.                                                        | It occupies more memory.                                                                                                       |
| Inserting new elements at the front is<br>potentially expensive because existing<br>elements need to be shifted over to<br>make room. | Inserting a new element at any position<br>can be carried out easily.                                                          |
| Deleting an element from an array is<br>not possible.                                                                                 | Deleting an element is possible.                                                                                               |

#### Trade offs between linked lists and arrays:

| FEATURE               | ARRAYS      | LINKED LISTS |
|-----------------------|-------------|--------------|
| Sequential access     | efficient   | efficient    |
| Random access         | efficient   | inefficient  |
| Resigning             | inefficient | efficient    |
| Element rearranging   | inefficient | efficient    |
| Overhead per elements | none        | 1 or 2 links |

### Applications of linked list:

1. Linked lists are used to represent and manipulate polynomial. Polynomials are expression containing terms with non zero coefficient and exponents. For example:

$$P(x) = a_0 X^n + a_1 X^{n-1} + \dots + a_{n-1} X + a_n$$

- 2. Represent very large numbers and operations of the large number such as addition, multiplication and division.
- 3. Linked lists are to implement stack, queue, trees and graphs.
- 4. Implement the symbol table in compiler construction

### 3.3. Single Linked List:

A linked list allocates space for each element separately in its own block of memory called a "node". The list gets an overall structure by using pointers to connect all its nodes together like the links in a chain. Each node contains two fields; a "data" field to store whatever element, and a "next" field which is a pointer used to link to the next node. Each node is allocated in the heap using malloc(), so the node memory continues to exist until it is explicitly de-allocated using free(). The front of the list is a pointer to .

A single linked list is shown in figure 3.2.1.

Figure 3.2.1. Single Linked List

The beginning of the linked list is stored in a "start" pointer which points to the first node. The first node contains a pointer to the second node. The second node contains a pointer to the third node, ... and so on. The last node in the list has its next field set to NULL to mark the end of the list. Code can access any node in the list by starting at the start and following the next pointers.

The start pointer is an ordinary local pointer variable, so it is drawn separately on the left top to show that it is in the stack. The list nodes are drawn on the right to show that they are allocated in the heap.

### Implementation of Single Linked List:

Before writing the code to build the above list, we need to create a start node, used to create and access other nodes in the linked list. The following structure definition will do (see figure 3.2.2):

- Creating a structure with one data item and a next pointer, which will be pointing to next node of the list. This is called as self-referential structure.
- Initialise the start pointer to be NULL.

```
struct slinklist
{
        int data;
        struct slinklist* next;
};
typedef struct slinklist node;
node *start = NULL;
```

Figure 3.2.2. Structure definition, single link node and empty list

### The basic operations in a single linked list are:

- Creation.
- Insertion.
- Deletion.
- Traversing.

#### Creating a node for Single Linked List:

Creating a singly linked list starts with creating a node. Sufficient memory has to be allocated for creating a node. The information is stored in the memory, allocated by using the malloc() function. The function getnode(), is used for creating a node, after allocating memory for the structure of type node, the information for the item (i.e., data) has to be read from the user, set next field to NULL and finally returns the address of the node. Figure 3.2.3 illustrates the creation of a node for single linked list.

```
node* getnode()
{
    node* newnode;
    newnode = (node *) malloc(sizeof(node)); 
    printf("\n Enter data: "); scanf("%d", 
    &newnode -> data);
    newnode -> next = NULL;
    return newnode;
}
                                                                    newnode
                                                                    10 X
                                                                  100
```

Figure 3.2.3. new node with a value of 10

The following steps are to be followed to create

- Get the new node using getnode(). newnode = getnode();
- If the list is empty, assign new node as start. start = newnode;
- If the list is not empty, follow the steps given below:
  - The next field of the new node is made to point the first node (i.e. start node) in the list by assigning the address of the first node.
  - The start pointer is made to point the new node by assigning the address of the new node.

Figure 3.2.4 shows 4 items in a single linked list stored at different locations in memory.

Figure 3.2.4. Single Linked List with 4 nodes

```
vo id createlist(int n)
{
        int i;
        node * new node;
        node *temp;
        for(i = 0; i < n ; i+ +)
        {
                new node = getnode();
                if(start = = NULL)
                {
                        start = new node;
                }
                else
                {
                        temp = start;
                             while(temp - > next != NULL)
                                    temp = temp - > next;
                        temp - > next = new node;
                }
        }
}
```

# Insertion of a Node:

One of the most primitive operations that can be done in a singly linked list is the insertion of a node. Memory is to be allocated for the new node (in a similar way that is done while creating a list) before reading the data. The new node will contain empty data field and empty next field. The data field of the new node is then stored with the information read from the user. The next field of the new node is assigned to NULL. The new node can then be inserted at three different places namely:

- Inserting a node at the beginning.
- Inserting a node at the end.
- Inserting a node at intermediate position.

start = newnode;

# Inserting a node at the beginning:

The following steps are to be followed to insert a new node at the beginning of the list:

```
Get the new node using getnode(). 
   newnode = getnode();
If the list is empty then start = newnode.
If the list is not empty, follow the steps given below: 
   newnode -> next = start;
```

Figure 3.2.5 shows inserting a node into the single linked list at the beginning.

Figure 3.2.5. Inserting a node at the beginning

The function insert\_at\_beg(), is used for inserting a node at the beginning

```
void insert_at_beg()
{
       node *newnode;
       newnode = getnode();
       if(start == NULL)
       {
               start = newnode;
       }
       else
       {
               newnode -> next = start;
               start = newnode;
       }
}
```

### Inserting a node at the end:

The following steps are followed to insert a new node at the end of the list:

```
Get the new node using getnode() 
   newnode = getnode();
If the list is empty then start = newnode.
If the list is not empty follow the steps given below: 
   temp = start;
   while(temp -> next != NULL) 
          temp = temp -> next;
   temp -> next = newnode;
```

Figure 3.2.6 shows inserting a node into the single linked list at the end.

Figure 3.2.6. Inserting a node at the end.

The function insert\_at\_end(), is used for inserting a node at the end.

```
void insert_at_end()
{
       node *newnode, *temp;
       newnode = getnode();
       if(start == NULL)
       {
               start = newnode;
       }
       else
       {
               temp = start;
               while(temp -> next != NULL)
                       temp = temp -> next;
               temp -> next = newnode;
       }
}
```

#### Inserting a node at intermediate position:

The following steps are followed, to insert a new node in an intermediate position in the list:

```
Get the new node using getnode(). 
   newnode = getnode();
```

- Ensure that the specified position is in between first node and last node. If not, specified position is invalid. This is done by countnode() function.
- Store the starting address (which is in start pointer) in temp and prev pointers. Then traverse the temp pointer upto the specified position followed by prev pointer.
- After reaching the specified position, follow the steps given below: prev -> next = newnode; newnode -> next = temp;
- Let the intermediate position be 3.

Figure 3.2.7 shows inserting a node into the single linked list at a specified intermediate position other than beginning and end.

Figure 3.2.7. Inserting a node at an intermediate position.

The function insert\_at\_mid(), is used for inserting a node in the intermediate position.

```
void insert_at_mid()
{
        node *newnode, *temp, *prev;
        int pos, nodectr, ctr = 1;
        newnode = getnode();
        printf("\n Enter the position: ");
        scanf("%d", &pos);
        nodectr = countnode(start);
        if(pos > 1 && pos < nodectr)
        {
                temp = prev = start;
                while(ctr < pos)
                {
                        prev = temp;
                        temp = temp -> next;
                        ctr++;
                }
                prev -> next = newnode;
                newnode -> next = temp;
        }
        else
        {
                printf("position %d is not a middle position", pos);
        }
}
```

#### Deletion of a node:

Another primitive operation that can be done in a singly linked list is the deletion of a node. Memory is to be released for the node to be deleted. A node can be deleted from the list from three different places namely.

- Deleting a node at the beginning.
- Deleting a node at the end.
- Deleting a node at intermediate position.

# Deleting a node at the beginning:

The following steps are followed, to delete a node at the beginning of the list:

- If the list is not empty, follow the steps given below: temp = start; start = start -> next; free(temp);

Figure 3.2.8 shows deleting a node at the beginning of a single linked list.

Figure 3.2.8. Deleting a node at the beginning.

The function delete\_at\_beg(), is used for deleting the first node in the list.

```
void delete_at_beg()
{
        node *temp;
        if(start == NULL)
        {
                printf("\n No nodes are exist..");
                return ;
        }
        else
        {
                temp = start;
                start = temp -> next;
                free(temp);
                printf("\n Node deleted ");
        }
}
```

### Deleting a node at the end:

The following steps are followed to delete a node at the end of the list:

- If the list is not empty, follow the steps given below:

```
temp = prev = start;
while(temp -> next != NULL)
{
      prev = temp;
      temp = temp -> next;
}
prev -> next = NULL;
free(temp);
```

Figure 3.2.9 shows deleting a node at the end of a single linked list.

Figure 3.2.9. Deleting a node at the end.

The function delete\_at\_last(), is used for deleting the last node in the list.

```
void delete_at_last()
{
        node *temp, *prev;
        if(start == NULL)
        {
                printf("\n Empty List..");
                return ;
        }
        else
        {
                temp = start;
                prev = start;
                while(temp -> next != NULL)
                {
                        prev = temp;
                        temp = temp -> next;
                }
                prev -> next = NULL;
                free(temp);
                printf("\n Node deleted ");
        }
}
```

### Deleting a node at Intermediate position:

The following steps are followed, to delete a node from an intermediate position in the list (List must contain more than two node).

```
If the list is not empty, follow the steps given below. 
   if(pos > 1 && pos < nodectr)
   {
           temp = prev = start; 
           ctr = 1;
           while(ctr < pos)
           {
                  prev = temp;
                  temp = temp -> next; 
                  ctr++;
           }
           prev -> next = temp -> next; 
           free(temp);
           printf("\n node deleted..");
   }
```

Figure 3.2.10 shows deleting a node at a specified intermediate position other than beginning and end from a single linked list.

Figure 3.2.10. Deleting a node at an intermediate position.

The function delete\_at\_mid(), is used for deleting the intermediate node in the list.

```
void delete_at_mid()
{
        int ctr = 1, pos, nodectr;
        node *temp, *prev;
        if(start == NULL)
        {
                printf("\n Empty List..");
                return ;
        }
        else
        {
                printf("\n Enter position of node to delete: ");
                scanf("%d", &pos);
                nodectr = countnode(start);
                if(pos > nodectr)
                {
                         printf("\nThis node doesnot exist");
                }
```

```
if(pos > 1 && pos < nodectr)
                {
                        temp = prev = start;
                        while(ctr < pos)
                        {
                                 prev = temp;
                                 temp = temp -> next;
                                 ctr ++;
                        }
                        prev -> next = temp -> next;
                        free(temp);
                        printf("\n Node deleted..");
                }
                else
                {
                        printf("\n Invalid position..");
                        getch();
                }
        }
}
```

# Traversal and displaying a list (Left to Right):

To display the information, you have to traverse (move) a linked list, node by node from the first node, until the end of the list is reached. Traversing a list involves the following steps:

- Assign the address of start pointer to a temp pointer.
- Display the information from the data field of each node.

The function *traverse*() is used for traversing and displaying the information stored in the list from left to right.

```
void traverse()
{
        node *temp;
        temp = start;
        printf("\n The contents of List (Left to Right): 
        \n"); if(start == NULL )
                printf("\n Empty List");
        else
        {
                while (temp != NULL)
                {
                         printf("%d ->", temp -> data);
                         temp = temp -> next;
                }
        }
        printf("X");
}
```

Alternatively there is another way to traverse and display the information. That is in reverse order. The function rev\_traverse(), is used for traversing and displaying the information stored in the list from right to left.

```
void rev_traverse(no de *st)
{
        if(st = = NULL)
        {
                 return;
        }
        else
        {
                 rev_traverse(st - > next);
                 printf("%d - >", st - > data);
        }
}
```

#### Counting the Number of Nodes:

The following code will count the number of nodes exist in the list using *recursion*.

```
int countnode(node *st)
{
        if(st = = NULL)
                return 0;
        else
                return(1 + countnode(st - > next));
}
```

#### 3.3.1. Source Code for the Implementation of Single Linked List:

```
# include <stdio.h>
# include <conio.h>
# include <stdlib.h>
struct slinklist
{
        int data;
        struct slinklist *next;
};
typedef struct slinklist node;
node *start = NULL;
int menu()
{
        int ch;
        clrscr();
        printf("\n 1.Create a list ");
        printf("\n--------------------------");
        printf("\n 2.Insert a node at beginning ");
        printf("\n 3.Insert a node at end");
        printf("\n 4.Insert a node at middle");
        printf("\n--------------------------");
        printf("\n 5.Delete a node from beginning");
        printf("\n 6.Delete a node from Last");
        printf("\n 7.Delete a node from Middle");
        printf("\n--------------------------");
        printf("\n 8.Traverse the list (Left to Right)");
        printf("\n 9.Traverse the list (Right to Left)");
```

```
printf("\n--------------------------");
        printf("\n 10. Count nodes ");
        printf("\n 11. Exit ");
        printf("\n\n Enter your choice: ");
        scanf("%d",&ch);
        return ch;
}
node* getnode()
{
        node * newnode;
        newnode = (node *) malloc(sizeof(node));
        printf("\n Enter data: ");
        scanf("%d", &newnode -> data);
        newnode -> next = NULL;
        return newnode;
}
int countnode(node *ptr)
{
        int count=0;
        while(ptr != NULL)
        {
                count++;
                ptr = ptr -> next;
        }
        return (count);
}
void createlist(int n)
{
        int i;
        node *newnode;
        node *temp;
        for(i = 0; i < n; i++)
        {
                newnode = getnode();
                if(start == NULL)
                {
                        start = newnode;
                }
                else
                {
                        temp = start;
                        while(temp -> next != NULL)
                                temp = temp -> next;
                        temp -> next = newnode;
                }
        }
}
void traverse()
{
        node *temp;
        temp = start;
        printf("\n The contents of List (Left to Right): \n");
        if(start == NULL)
        {
                printf("\n Empty List");
                return;
        }
        else
        {
```

```
while(temp != NULL)
                {
                        printf("%d-->", temp -> data);
                        temp = temp -> next;
                }
        }
        printf(" X ");
}
void rev_traverse(node *start)
{
        if(start == NULL)
        {
                return;
        }
        else
        {
                rev_traverse(start -> next);
                printf("%d -->", start -> data);
        }
}
void insert_at_beg()
{
        node *newnode;
        newnode = getnode();
        if(start == NULL)
        {
                start = newnode;
        }
        else
        {
                newnode -> next = start;
                start = newnode;
        }
}
void insert_at_end()
{
        node *newnode, *temp;
        newnode = getnode();
        if(start == NULL)
        {
                start = newnode;
        }
        else
        {
                temp = start;
                while(temp -> next != NULL)
                        temp = temp -> next;
                temp -> next = newnode;
        }
}
void insert_at_mid()
{
        node *newnode, *temp, *prev;
        int pos, nodectr, ctr = 1;
        newnode = getnode();
        printf("\n Enter the position: ");
        scanf("%d", &pos);
        nodectr = countnode(start);
```

```
if(pos > 1 && pos < nodectr)
        {
                temp = prev = start;
                while(ctr < pos)
                {
                        prev = temp;
                        temp = temp -> next;
                        ctr++;
                }
                prev -> next = newnode;
                newnode -> next = temp;
        }
        else
                printf("position %d is not a middle position", pos);
}
void delete_at_beg()
{
        node *temp;
        if(start == NULL)
        {
                printf("\n No nodes are exist..");
                return ;
        }
        else
        {
                temp = start;
                start = temp -> next;
                free(temp);
                printf("\n Node deleted ");
        }
}
void delete_at_last()
{
        node *temp, *prev;
        if(start == NULL)
        {
                printf("\n Empty List..");
                return ;
        }
        else
        {
                temp = start;
                prev = start;
                while(temp -> next != NULL)
                {
                        prev = temp;
                        temp = temp -> next;
                }
                prev -> next = NULL;
                free(temp);
                printf("\n Node deleted ");
        }
}
void delete_at_mid()
{
        int ctr = 1, pos, nodectr;
        node *temp, *prev;
        if(start == NULL)
        {
                printf("\n Empty List..");
```

```
return ;
        }
        else
        {
                printf("\n Enter position of node to delete: ");
                scanf("%d", &pos);
                nodectr = countnode(start);
                if(pos > nodectr)
                {
                         printf("\nThis node doesnot exist");
                }
                if(pos > 1 && pos < nodectr)
                {
                         temp = prev = start;
                         while(ctr < pos)
                         {
                                 prev = temp;
                                 temp = temp -> next;
                                 ctr ++;
                         }
                         prev -> next = temp -> next;
                         free(temp);
                         printf("\n Node deleted..");
                }
                else
                {
                         printf("\n Invalid position..");
                         getch();
                }
        }
}
void main(void)
{
        int ch, n;
        clrscr();
        while(1)
        {
                ch = menu();
                switch(ch)
                {
                case 1:
                         if(start == NULL)
                         {
                                 printf("\n Number of nodes you want to create: ");
                                 scanf("%d", &n);
                                 createlist(n);
                                 printf("\n List created..");
                         }
                         else
                                 printf("\n List is already created..");
                                 break;
                case 2:
                         insert_at_beg();
                         break;
                case 3:
                         insert_at_end();
                         break;
                case 4:
                         insert_at_mid();
                         break;
```

```
case 5:
                         delete_at_beg();
                         break;
                case 6:
                         delete_at_last();
                         break;
                case 7:
                         delete_at_mid();
                         break;
                case 8:
                         traverse();
                         break;
                case 9:
                         printf("\n The contents of List (Right to Left): \n");
                         rev_traverse(start);
                         printf(" X ");
                         break;
                case 10:
                         printf("\n No of nodes : %d ", countnode(start));
                         break;
                case 11 :
                         exit(0);
                }
                getch();
        }
}
```

### 3.4. Using a header node:

A header node is a special dummy node found at the front of the list. The use of header node is an alternative to remove the first node in a list. For example, the picture below shows how the list with data 10, 20 and 30 would be represented using a linked list without and with a header node:

Single Linke d List w it ho ut a he a der no de

Single Linked List with header node

Note that if your linked lists do include a header node, there is no need for the special case code given above for the *remove* operation; node *n* can never be the first node in the list, so there is no need to check for that case. Similarly, having a header node can simplify the code that adds a node before a given node *n*.

Note that if you do decide to use a header node, you must remember to initialize an empty list to contain one (dummy) node, you must remember not to include the header node in the count of "real" nodes in the list.

It is also useful when information other than that found in each node of the list is needed. For example, imagine an application in which the number of items in a list is often calculated. In a standard linked list, the list function to count the number of nodes has to traverse the entire list every time. However, if the current length is maintained in a header node, that information can be obtained very quickly.

### 3.5. Array based linked lists:

Another alternative is to allocate the nodes in blocks. In fact, if you know the maximum size of a list a head of time, you can pre-allocate the nodes in a single array. The result is a hybrid structure an array based linked list. Figure 3.5.1 shows an example of null terminated single linked list where all the nodes are allocated contiguously in an array.

Figure 3.5.1. An array based linked list

## 3.6. Double Linked List:

A double linked list is a two-way list in which all nodes will have two links. This helps in accessing both successor node and predecessor node from the given node position. It provides bi-directional traversing. Each node contains three fields:

- Left link.
- Data.
- Right link.

The left link points to the predecessor node and the right link points to the successor node. The data field stores the required data.

Many applications require searching forward and backward thru nodes of a list. For example searching for a name in a telephone directory would need forward and backward scanning thru a region of the whole list.

The basic operations in a double linked list are:

- Creation.
- Insertion.
- Deletion.
- Traversing.

A double linked list is shown in figure 3.3.1.

Figure 3.3.1. Double Linked List

The beginning of the double linked list is stored in a "start" pointer which points to the set to NULL.

The following code gives the structure definition:

```
struct dlinklist
{ node: left data right
   struct dlinklist *left;
   int data;
   struct dlinklist *right;
}; start
typedef struct dlinklist node; Empty list: NULL
node *start = NULL;
```

Figure 3.4.1. Structure definition, double link node and empty list

#### Creating a node for Double Linked List:

Creating a double linked list starts with creating a node. Sufficient memory has to be allocated for creating a node. The information is stored in the memory, allocated by using the malloc() function. The function getnode(), is used for creating a node, after allocating memory for the structure of type node, the information for the item (i.e., data) has to be read from the user and set left field to NULL and right field also set to NULL (see figure 3.2.2).

```
node* getnode()
{
   node* newnode;
   newnode = (node *) malloc(sizeof(node));
   printf("\n Enter data: "); X 10 X
   scanf("%d", &newnode -> data);
   newnode -> left = NULL;
   newnode -> right = NULL;
   return newnode;
}
```

The following

Get the new node using getnode().

```
newnode =getnode();
```

- If the list is empty then *start = newnode*.
- If the list is not empty, follow the steps given below:
  - The left field of the new node is made to point the previous node.
  - The previous nodes right field must be assigned with address of the new node.

```
void createlist(int n)
{
        int i;
        node * new node;
        node *tem p;
        for(i = 0; i < n; i+ +)
        {
                new node = getnode();
                if(start = = NULL)
                {
                        start = new node;
                }
                else
                {
                        temp = start;
                        while(temp - > right)
                                temp = temp - > right;
                        tem p - > right = new no de;
                        new node - > left = temp;
                }
        }
}
```

Figure 3.4.3 shows 3 items in a double linked list stored at different locations.

Figure 3.4.3. Double Linked List with 3 nodes

### Inserting a node at the beginning:

The following steps are to be followed to insert a new node at the beginning of the list:

Get the new node using getnode().

```
newnode=getnode();
```

- If the list is empty then *start = newnode*.
- If the list is not empty, follow the steps given below:

```
newnode -> right = start;
start -> left = newnode;
start = newnode;
```

The function dbl\_insert\_beg(), is used for inserting a node at the beginning. Figure 3.4.4 shows inserting a node into the double linked list at the beginning.

Figure 3.4.4. Inserting a node at the beginning

#### Inserting a node at the end:

The following steps are followed to insert a new node at the end of the list:

```
Get the new node using getnode()
```

```
newnode=getnode();
```

- If the list is empty then *start = newnode*.
- If the list is not empty follow the steps given below:

```
temp = start;
while(temp -> right != NULL)
      temp = temp -> right;
temp -> right = newnode;
newnode -> left = temp;
```

The function dbl\_insert\_end(), is used for inserting a node at the end. Figure 3.4.5 shows inserting a node into the double linked list at the end.

Figure 3.4.5. Inserting a node at the end

### Inserting a node at an intermediate position:

The following steps are followed, to insert a new node in an intermediate position in the list:

Get the new node using getnode().

```
newnode=getnode();
```

- Ensure that the specified position is in between first node and last node. If not, specified position is invalid. This is done by countnode() function.
- Store the starting address (which is in start pointer) in temp and prev pointers. Then traverse the temp pointer upto the specified position followed by prev pointer.
- After reaching the specified position, follow the steps given below:

```
newnode -> left = temp;
newnode -> right = temp -> right;
temp -> right -> left = newnode;
temp -> right = newnode;
```

The function dbl\_insert\_mid(), is used for inserting a node in the intermediate position. Figure 3.4.6 shows inserting a node into the double linked list at a specified intermediate position other than beginning and end.

#### Deleting a node at the beginning:

The following steps are followed, to delete a node at the beginning of the list:

- If the list is not empty, follow the steps given below:

```
temp = start;
start = start -> right;
start -> left = NULL;
free(temp);
```

The function dbl\_delete\_beg(), is used for deleting the first node in the list. Figure 3.4.6 shows deleting a node at the beginning of a double linked list.

Figure 3.4.6. Deleting a node at beginning

# Deleting a node at the end:

The following steps are followed to delete a node at the end of the list:

- If the list is not empty, follow the steps given below:

```
temp = start;
while(temp -> right != NULL)
{
       temp = temp -> right;
}
temp -> left -> right = NULL;
free(temp);
```

The function dbl\_delete\_last(), is used for deleting the last node in the list. Figure 3.4.7 shows deleting a node at the end of a double linked list.

Figure 3.4.7. Deleting a node at the end

### Deleting a node at Intermediate position:

The following steps are followed, to delete a node from an intermediate position in the list (List must contain more than two nodes).

- If the list is not empty, follow the steps given below:
  - Get the position of the node to delete.
  - Ensure that the specified position is in between first node and last node. If not, specified position is invalid.

```
Then perform the following steps:
   if(pos > 1 && pos < nodectr)
   {
           temp = start;
           i = 1;
           while(i < pos)
           {
                  temp = temp -> right;
                  i++;
           }
           temp -> right -> left = temp -> left;
           temp -> left -> right = temp -> right;
           free(temp);
           printf("\n node deleted..");
   }
```

The function delete\_at\_mid(), is used for deleting the intermediate node in the list. Figure 3.4.8 shows deleting a node at a specified intermediate position other than beginning and end from a double linked list.

Figure 3.4.8 Deleting a node at an intermediate position

#### Traversal and displaying a list (Left to Right):

To display the information, you have to traverse the list, node by node from the first node, until the end of the list is reached. The function *traverse\_left\_right*() is used for traversing and displaying the information stored in the list from left to right.

The following steps are followed, to traverse a list from left to right:

- If the list is not empty, follow the steps given below:

```
temp = start;
while(temp != NULL)
{
       print temp -> data;
       temp = temp -> right;
}
```

# Traversal and displaying a list (Right to Left):

To display the information from right to left, you have to traverse the list, node by node from the first node, until the end of the list is reached. The function *traverse\_right\_left*() is used for traversing and displaying the information stored in the list from right to left. The following steps are followed, to traverse a list from right to left:

```
If the list is not empty, follow the steps given below: 
   temp = start;
   while(temp -> right != NULL) 
          temp = temp -> right;
   while(temp != NULL)
   {
          print temp -> data; 
          temp = temp -> left;
   }
```

# Counting the Number of Nodes:

The following code will count the number of nodes exist in the list (using recursion).

```
int countnode(node *start)
{
        if(start = = NULL)
                return 0;
        else
                return(1 + countnode(start - >right ));
}
```

#### 3.5. A Complete Source Code for the Implementation of Double Linked List:

```
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
struct dlinklist
{
        struct dlinklist *left;
        int data;
        struct dlinklist *right;
};
typedef struct dlinklist node;
node *start = NULL;
```

```
node* getnode()
{
        node * newnode;
        newnode = (node *) malloc(sizeof(node));
        printf("\n Enter data: ");
        scanf("%d", &newnode -> data);
        newnode -> left = NULL;
        newnode -> right = NULL;
        return newnode;
}
int countnode(node *start)
{
        if(start == NULL)
                return 0;
        else
                return 1 + countnode(start -> right);
}
int menu()
{
        int ch;
        clrscr();
        printf("\n 1.Create");
        printf("\n------------------------------");
        printf("\n 2. Insert a node at beginning ");
        printf("\n 3. Insert a node at end");
        printf("\n 4. Insert a node at middle");
        printf("\n------------------------------");
        printf("\n 5. Delete a node from beginning");
        printf("\n 6. Delete a node from Last");
        printf("\n 7. Delete a node from Middle");
        printf("\n------------------------------");
        printf("\n 8. Traverse the list from Left to Right 
        "); printf("\n 9. Traverse the list from Right to 
        Left "); printf("\n------------------------------");
        printf("\n 10.Count the Number of nodes in the list"); 
        printf("\n 11.Exit ");
        printf("\n\n Enter your choice: ");
        scanf("%d", &ch);
        return ch;
}
void createlist(int n)
{
        int i;
        node *newnode;
        node *temp;
        for(i = 0; i < n; i++)
        {
                newnode = getnode();
                if(start == NULL)
                        start = newnode;
                else
                {
                        temp = start;
                        while(temp -> right)
                                temp = temp -> right;
                        temp -> right = newnode;
                        newnode -> left = temp;
                }
        }
}
```

```
void traverse_left_to_right()
{
        node *temp;
        temp = start;
        printf("\n The contents of List: ");
        if(start == NULL )
                printf("\n Empty List");
        else
        {
                while(temp != NULL)
                {
                        printf("\t %d ", temp -> data);
                        temp = temp -> right;
                }
        }
}
void traverse_right_to_left()
{
        node *temp;
        temp = start;
        printf("\n The contents of List: ");
        if(start == NULL)
                printf("\n Empty List");
        else
        {
                while(temp -> right != NULL)
                        temp = temp -> right;
        }
        while(temp != NULL)
        {
                printf("\t%d", temp -> data);
                temp = temp -> left;
        }
}
void dll_insert_beg()
{
        node *newnode;
        newnode = getnode();
        if(start == NULL)
                start = newnode;
        else
        {
                newnode -> right = start;
                start -> left = newnode;
                start = newnode;
        }
}
void dll_insert_end()
{
        node *newnode, *temp;
        newnode = getnode();
        if(start == NULL)
                start = newnode;
        else
        {
                temp = start;
                while(temp -> right != NULL)
                        temp = temp -> right;
                temp -> right = newnode;
                newnode -> left = temp;
        }
}
```

```
void dll_insert_mid()
{
        node *newnode,*temp;
        int pos, nodectr, ctr = 1;
        newnode = getnode();
        printf("\n Enter the position: ");
        scanf("%d", &pos);
        nodectr = countnode(start);
        if(pos - nodectr >= 2)
        {
                printf("\n Position is out of range..");
                return;
        }
        if(pos > 1 && pos < nodectr)
        {
                temp = start;
                while(ctr < pos - 1)
                {
                        temp = temp -> right;
                        ctr++;
                }
                newnode -> left = temp;
                newnode -> right = temp -> right;
                temp -> right -> left = newnode;
                temp -> right = newnode;
        }
        else
                printf("position %d of list is not a middle position ", pos);
}
void dll_delete_beg()
{
        node *temp;
        if(start == NULL)
        {
                printf("\n Empty list");
                getch();
                return ;
        }
        else
        {
                temp = start;
                start = start -> right;
                start -> left = NULL;
                free(temp);
        }
}
void dll_delete_last()
{
        node *temp;
        if(start == NULL)
        {
                printf("\n Empty list");
                getch();
                return ;
        }
        else
        {
                temp = start;
                while(temp -> right != NULL)
```

```
temp = temp -> right;
                temp -> left -> right = NULL;
                free(temp);
                temp = NULL;
        }
}
void dll_delete_mid()
{
        int i = 0, pos, nodectr;
        node *temp;
        if(start == NULL)
        {
                printf("\n Empty List");
                getch();
                return;
        }
        else
        {
                printf("\n Enter the position of the node to delete: "); 
                scanf("%d", &pos);
                nodectr = countnode(start);
                if(pos > nodectr)
                {
                         printf("\nthis node does not exist");
                         getch();
                         return;
                }
                if(pos > 1 && pos < nodectr)
                {
                         temp = start;
                         i = 1;
                         while(i < pos)
                         {
                                 temp = temp -> right;
                                 i++;
                         }
                         temp -> right -> left = temp -> left;
                         temp -> left -> right = temp -> right;
                         free(temp);
                         printf("\n node deleted..");
                }
                else
                {
                         printf("\n It is not a middle position..");
                         getch();
                }
        }
}
void main(void)
{
        int ch, n;
        clrscr();
        while(1)
        {
                ch = menu();
                switch( ch)
                {
                         case 1 :
                                 printf("\n Enter Number of nodes to create: ");
                                 scanf("%d", &n);
                                 createlist(n);
```

```
printf("\n List created..");
                                 break;
                         case 2 :
                                 dll_insert_beg();
                                 break;
                         case 3 :
                                 dll_insert_end();
                                 break;
                         case 4 :
                                 dll_insert_mid();
                                 break;
                         case 5 :
                                 dll_delete_beg();
                                 break;
                         case 6 :
                                 dll_delete_last();
                                 break;
                         case 7 :
                                 dll_delete_mid();
                                 break;
                         case 8 :
                                 traverse_left_to_right();
                                 break;
                         case 9 :
                                 traverse_right_to_left();
                                 break;
                         case 10 :
                                 printf("\n Number of nodes: %d", countnode(start)); 
                                 break;
                         case 11:
                                 exit(0);
                }
                getch();
        }
}
```

# 3.7. Circular Single Linked List:

It is just a single linked list in which the link field of the last node points back to the address of the first node. A circular linked list has no beginning and no end. It is necessary to establish a special pointer called *start* pointer always pointing to the first node of the list. Circular linked lists are frequently used instead of ordinary linked list because many operations are much easier to implement. In circular linked list no null pointers are used, hence all pointers contain valid address.

A circular single linked list is shown in figure 3.6.1.

Figure 3.6.1. Circular Single Linked List

|                | The basic operations in a circular single linked list are:                                                                                     |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
|                | Creation.<br>Insertion.<br>Deletion.<br>Traversing.                                                                                            |
|                |                                                                                                                                                |
|                | The following steps                                                                                                                            |
|                | Get the new node using getnode().                                                                                                              |
|                | newnode = getnode();                                                                                                                           |
|                | If the list is empty, assign new node as start.                                                                                                |
|                | start = newnode;                                                                                                                               |
|                | If the list is not empty, follow the steps given below:                                                                                        |
|                | temp = start;<br>while(temp -> next != NULL)<br>temp = temp -> next;<br>temp -> next = newnode;                                                |
|                |                                                                                                                                                |
|                | newnode -> next = start;                                                                                                                       |
|                |                                                                                                                                                |
|                | Inserting a node at the beginning:                                                                                                             |
| circular list: | The following steps are to be followed to insert a new node at the beginning of the                                                            |
|                | Get the new node using getnode().                                                                                                              |
|                | newnode = getnode();                                                                                                                           |
|                | If the list is empty, assign new node as start.                                                                                                |
|                | start = newnode;<br>newnode -> next = start;                                                                                                   |
|                | If the list is not empty, follow the steps given below:                                                                                        |
|                | last = start;<br>while(last -> next != start)<br>last = last -> next;<br>newnode -> next = start;<br>start = newnode;<br>last -> next = start; |

The function cll\_insert\_beg(), is used for inserting a node at the beginning. Figure 3.6.2 shows inserting a node into the circular single linked list at the beginning.

Figure 3.6.2. Inserting a node at the beginning

# Inserting a node at the end:

The following steps are followed to insert a new node at the end of the list:

Get the new node using getnode().

```
newnode = getnode();
```

If the list is empty, assign new node as start.

```
start = newnode;
newnode -> next = start;
```

If the list is not empty follow the steps given below:

```
temp = start;
while(temp -> next != start)
      temp = temp -> next;
temp -> next = newnode;
newnode -> next = start;
```

The function cll\_insert\_end(), is used for inserting a node at the end.

Figure 3.6.3 shows inserting a node into the circular single linked list at the end.

Figure 3.6.3 Inserting a node at the end.

#### Deleting a node at the beginning:

The following steps are followed, to delete a node at the beginning of the list:

- If the list is not empty, follow the steps given below:

```
last = temp = start;
while(last -> next != start)
       last = last -> next;
start = start -> next;
last -> next = start;
```

After deleting the node, if the list is empty then *start = NULL.*

The function cll\_delete\_beg(), is used for deleting the first node in the list. Figure 3.6.4 shows deleting a node at the beginning of a circular single linked list.

Figure 3.6.4. Deleting a node at beginning.

# Deleting a node at the end:

The following steps are followed to delete a node at the end of the list:

- If the list is not empty, follow the steps given below:

```
temp = start;
prev = start;
while(temp -> next != start)
{
       prev = temp;
       temp = temp -> next;
}
prev -> next = start;
```

After deleting the node, if the list is empty then *start = NULL.*

The function cll\_delete\_last(), is used for deleting the last node in the list.

Figure 3.6.5 shows deleting a node at the end of a circular single linked list.

Figure 3.6.5. Deleting a node at the end.

# Traversing a circular single linked list from left to right:

The following steps are followed, to traverse a list from left to right:

- If
- If the list is not empty, follow the steps given below:

```
temp = start;
do
{
       printf("%d ", temp -> data);
       temp = temp -> next;
} while(temp != start);
```

## 3.7.1. Source Code for Circular Single Linked List:

```
# include <stdio.h>
# include <conio.h>
# include <stdlib.h>
struct cslinklist
{
        int data;
        struct cslinklist *next;
};
typedef struct cslinklist node;
node *start = NULL;
int nodectr;
node* getnode()
{
        node * newnode;
        newnode = (node *) malloc(sizeof(node));
        printf("\n Enter data: ");
        scanf("%d", &newnode -> data);
        newnode -> next = NULL;
        return newnode;
}
```

```
int menu()
{
        int ch;
        clrscr();
        printf("\n 1. Create a list ");
        printf("\n\n--------------------------");
        printf("\n 2. Insert a node at beginning ");
        printf("\n 3. Insert a node at end");
        printf("\n 4. Insert a node at middle");
        printf("\n\n--------------------------");
        printf("\n 5. Delete a node from beginning");
        printf("\n 6. Delete a node from Last");
        printf("\n 7. Delete a node from Middle");
        printf("\n\n--------------------------");
        printf("\n 8. Display the list");
        printf("\n 9. Exit");
        printf("\n\n--------------------------");
        printf("\n Enter your choice: ");
        scanf("%d", &ch);
        return ch;
}
void createlist(int n)
{
        int i;
        node *newnode;
        node *temp;
        nodectr = n;
        for(i = 0; i < n ; i++)
        {
                newnode = getnode();
                if(start == NULL)
                {
                         start = newnode;
                }
                else
                {
                         temp = start;
                         while(temp -> next != NULL)
                                 temp = temp -> next;
                         temp -> next = newnode;
                }
        }
        newnode ->next = start; /* last node is pointing to starting node */
}
void display()
{
        node *temp;
        temp = start;
        printf("\n The contents of List (Left to Right): ");
        if(start == NULL )
                printf("\n Empty List");
        else
        {
                do
                {
                         printf("\t %d ", temp -> data);
                         temp = temp -> next;
                } while(temp != 
                start); printf(" X ");
        }
}
```

```
void cll_insert_beg()
{
        node *newnode, *last;
        newnode = getnode();
        if(start == NULL)
        {
                start = newnode;
                newnode -> next = start;
        }
        else
        {
                last = start;
                while(last -> next != start)
                        last = last -> next;
                newnode -> next = start;
                start = newnode;
                last -> next = start;
        }
        printf("\n Node inserted at beginning..");
        nodectr++;
}
void cll_insert_end()
{
        node *newnode, *temp;
        newnode = getnode();
        if(start == NULL )
        {
                start = newnode;
                newnode -> next = start;
        }
        else
        {
                temp = start;
                while(temp -> next != start)
                        temp = temp -> next;
                temp -> next = newnode;
                newnode -> next = start;
        }
        printf("\n Node inserted at end..");
        nodectr++;
}
void cll_insert_mid()
{
        node *newnode, *temp, *prev;
        int i, pos ;
        newnode = getnode();
        printf("\n Enter the position: ");
        scanf("%d", &pos);
        if(pos > 1 && pos < nodectr)
        {
                temp = start;
                prev = temp;
                i = 1;
                while(i < pos)
                {
                        prev = temp;
                        temp = temp -> next;
                        i++;
                }
                prev -> next = newnode;
                newnode -> next = temp;
```

```
nodectr++;
                printf("\n Node inserted at middle..");
        }
        else
        {
                printf("position %d of list is not a middle position ", pos);
        }
}
void cll_delete_beg()
{
        node *temp, *last;
        if(start == NULL)
        {
                printf("\n No nodes exist..");
                getch();
                return ;
        }
        else
        {
                last = temp = start;
                while(last -> next != start)
                         last = last -> next;
                start = start -> next;
                last -> next = start;
                free(temp);
                nodectr--;
                printf("\n Node deleted..");
                if(nodectr == 0)
                         start = NULL;
        }
}
void cll_delete_last()
{
        node *temp,*prev;
        if(start == NULL)
        {
                printf("\n No nodes exist..");
                getch();
                return ;
        }
        else
        {
                temp = start;
                prev = start;
                while(temp -> next != start)
                {
                         prev = temp;
                         temp = temp -> next;
                }
                prev -> next = start;
                free(temp);
                nodectr--;
                if(nodectr == 0)
                         start = NULL;
                printf("\n Node deleted..");
        }
}
```

```
void cll_delete_mid()
{
        int i = 0, pos;
        node *temp, *prev;
        if(start == NULL)
        {
                printf("\n No nodes exist..");
                getch();
                return ;
        }
        else
        {
                printf("\n Which node to delete: ");
                scanf("%d", &pos);
                if(pos > nodectr)
                {
                         printf("\nThis node does not exist");
                         getch();
                         return;
                }
                if(pos > 1 && pos < nodectr)
                {
                         temp=start;
                         prev = start;
                         i = 0;
                         while(i < pos - 1)
                         {
                                 prev = temp;
                                 temp = temp -> next ;
                                 i++;
                         }
                         prev -> next = temp -> next;
                         free(temp);
                         nodectr--;
                         printf("\n Node Deleted..");
                }
                else
                {
                         printf("\n It is not a middle position..");
                         getch();
                }
        }
}
void main(void)
{
        int result;
        int ch, n;
        clrscr();
        while(1)
        {
                ch = menu();
                switch(ch)
                {
                         case 1 :
                                 if(start == NULL)
                                 {
                                          printf("\n Enter Number of nodes to create: ");
                                          scanf("%d", &n);
                                          createlist(n);
                                          printf("\nList created..");
                                 }
```

```
else
                                           printf("\n List is already Exist..");
                                  break;
                          case 2 :
                                  cll_insert_beg();
                                  break;
                          case 3 :
                                  cll_insert_end();
                                  break;
                          case 4 :
                                  cll_insert_mid();
                                  break;
                          case 5 :
                                  cll_delete_beg();
                                  break;
                          case 6 :
                                  cll_delete_last();
                                  break;
                          case 7 :
                                  cll_delete_mid();
                                  break;
                          case 8 :
                                  display();
                                  break;
                          case 9 :
                                  exit(0);
                 }
                 getch();
        }
}
```

#### 3.8. Circular Double Linked List:

A circular double linked list has both successor pointer and predecessor pointer in circular manner. The objective behind considering circular double linked list is to simplify the insertion and deletion operations performed on double linked list. In circular double linked list the *right* link of the right most node points back to the *start* node and *left* link of the first node points to the last node. A circular double linked list is shown in figure 3.8.1.

Figure 3.8.1. Circular Double Linked List

The basic operations in a circular double linked list are:

- Creation.
- Insertion.
- Deletion.
- Traversing.

The following steps are to be followed to create

```
Get the new node using getnode(). 
   newnode = getnode();
If the list is empty, then do the following 
   start = newnode;
   newnode -> left = start; 
   newnode ->right = start;
If the list is not empty, follow the steps given below: 
   newnode -> left = start -> left;
   newnode -> right = start; start 
   -> left->right = newnode; start 
   -> left = newnode;
```

# Inserting a node at the beginning:

The following steps are to be followed to insert a new node at the beginning of the list:

```
Get the new node using getnode(). 
   newnode=getnode();
If the list is empty, then
   start = newnode;
   newnode -> left = start;
   newnode -> right = start;
If the list is not empty, follow the steps given 
   below: newnode -> left = start -> left;
   newnode -> right = start; start -
   > left -> right = newnode; start 
   -> left = newnode;
   start = newnode;
```

The function cdll\_insert\_beg(), is used for inserting a node at the beginning. Figure 3.8.2 shows inserting a node into the circular double linked list at the beginning.

Figure 3.8.2. Inserting a node at the beginning

### Inserting a node at the end:

The following steps are followed to insert a new node at the end of the list:

```
Get the new node using getnode() 
   newnode=getnode();
If the list is empty, then
   start = newnode;
   newnode -> left = start;
   newnode -> right = start;
If the list is not empty follow the steps given below: 
   newnode -> left = start -> left;
   newnode -> right = start; start -
   > left -> right = newnode; start 
   -> left = newnode;
```

The function cdll\_insert\_end(), is used for inserting a node at the end. Figure 3.8.3 shows inserting a node into the circular linked list at the end.

Figure 3.8.3. Inserting a node at the end

### Inserting a node at an intermediate position:

The following steps are followed, to insert a new node in an intermediate position in the list:

Get the new node using getnode(). newnode=getnode(); Ensure that the specified position is in between first node and last node. If not, specified position is invalid. This is done by countnode() function. Store the starting address (which is in start pointer) in temp. Then traverse the temp pointer upto the specified position. After reaching the specified position, follow the steps given below: newnode -> left = temp; newnode -> right = temp -> right; temp -> right -> left = newnode; temp -> right = newnode; nodectr++;

The function cdll\_insert\_mid(), is used for inserting a node in the intermediate position. Figure 3.8.4 shows inserting a node into the circular double linked list at a specified intermediate position other than beginning and end.

Figure 3.8.4. Inserting a node at an intermediate position

# Deleting a node at the beginning:

The following steps are followed, to delete a node at the beginning of the list:

- If the list is not empty, follow the steps given below:

```
temp = start;
start = start -> right;
temp -> left -> right = start;
start -> left = temp -> left;
```

The function cdll\_delete\_beg(), is used for deleting the first node in the list. Figure 3.8.5 shows deleting a node at the beginning of a circular double linked list.

Figure 3.8.5. Deleting a node at beginning

#### Deleting a node at the end:

The following steps are followed to delete a node at the end of the list:

- If the list is not empty, follow the steps given below:

```
temp = start;
while(temp -> right != start)
{
       temp = temp -> right;
}
temp -> left -> right = temp -> right;
temp -> right -> left = temp -> left;
```

The function cdll\_delete\_last(), is used for deleting the last node in the list. Figure 3.8.6 shows deleting a node at the end of a circular double linked list.

Figure 3.8.6. Deleting a node at the end

## Deleting a node at Intermediate position:

The following steps are followed, to delete a node from an intermediate position in the list (List must contain more than two node).

- If list is empty then display
- If the list is not empty, follow the steps given below:
  - Get the position of the node to delete.
  - Ensure that the specified position is in between first node and last node. If not, specified position is invalid.
  - Then perform the following steps:

```
if(pos > 1 && pos < nodectr)
{
       temp = start;
       i = 1;
       while(i < pos)
       {
              temp = temp -> right ;
              i++;
       }
       temp -> right -> left = temp -> left;
       temp -> left -> right = temp -> right;
       free(temp);
       printf("\n node deleted..");
       nodectr--;
}
```

The function cdll\_delete\_mid(), is used for deleting the intermediate node in the list.

Figure 3.8.7 shows deleting a node at a specified intermediate position other than beginning and end from a circular double linked list.

Figure 3.8.7. Deleting a node at an intermediate position

# Traversing a circular double linked list from left to right:

The following steps are followed, to traverse a list from left to right:

- If list is empty
- If the list is not empty, follow the steps given below: temp = start; Print temp -> data; temp = temp -> right; while(temp != start) { print temp -> data; temp = temp -> right; }

The function cdll\_display\_left \_right(), is used for traversing from left to right.

#### Traversing a circular double linked list from right to left:

The following steps are followed, to traverse a list from right to left:

- If the list is not empty, follow the steps given below: temp = start; do { temp = temp -> left; print temp -> data; } while(temp != start);

The function cdll\_display\_right\_left(), is used for traversing from right to left.

# 3.8.1. Source Code for Circular Double Linked List:

```
# include <stdio.h>
# include <stdlib.h>
# include <conio.h>
```

```
struct cdlinklist
{
        struct cdlinklist *left;
        int data;
        struct cdlinklist *right;
};
typedef struct cdlinklist node;
node *start = NULL;
int nodectr;
node* getnode()
{
        node * newnode;
        newnode = (node *) malloc(sizeof(node));
        printf("\n Enter data: ");
        scanf("%d", &newnode -> data);
        newnode -> left = NULL;
        newnode -> right = NULL;
        return newnode;
}
int menu()
{
        int ch;
        clrscr();
        printf("\n 1. Create ");
        printf("\n\n--------------------------");
        printf("\n 2. Insert a node at Beginning");
        printf("\n 3. Insert a node at End");
        printf("\n 4. Insert a node at Middle");
        printf("\n\n--------------------------");
        printf("\n 5. Delete a node from Beginning");
        printf("\n 6. Delete a node from End");
        printf("\n 7. Delete a node from Middle");
        printf("\n\n--------------------------");
        printf("\n 8. Display the list from Left to Right");
        printf("\n 9. Display the list from Right to Left");
        printf("\n 10.Exit");
        printf("\n\n Enter your choice: ");
        scanf("%d", &ch);
        return ch;
}
void cdll_createlist(int n)
{
        int i;
        node *newnode, *temp;
        if(start == NULL)
        {
                nodectr = n;
                for(i = 0; i < n; i++)
                {
                         newnode = getnode();
                         if(start == NULL)
                         {
                                 start = newnode;
                                 newnode -> left = start;
                                 newnode ->right = start;
                         }
                         else
                         {
                                 newnode -> left = start -> left;
```

```
newnode -> right = start;
                                start -> left->right = newnode;
                                start -> left = newnode;
                        }
                }
        }
        else
                printf("\n List already exists..");
}
void cdll_display_left_right()
{
        node *temp;
        temp = start;
        if(start == NULL)
                printf("\n Empty List");
        else
        {
                printf("\n The contents of List: ");
                printf(" %d ", temp -> data);
                temp = temp -> right;
                while(temp != start)
                {
                        printf(" %d ", temp -> data);
                        temp = temp -> right;
                }
        }
}
void cdll_display_right_left()
{
        node *temp;
        temp = start;
        if(start == NULL)
                printf("\n Empty List");
        else
        {
                printf("\n The contents of List: ");
                do
                {
                        temp = temp -> left;
                        printf("\t%d", temp -> data);
                } while(temp != start);
        }
}
void cdll_insert_beg()
{
        node *newnode;
        newnode = getnode();
        nodectr++;
        if(start == NULL)
        {
                start = newnode;
                newnode -> left = start;
                newnode -> right = start;
        }
        else
        {
                newnode -> left = start -> left;
                newnode -> right = start;
                start -> left -> right = newnode;
                start -> left = newnode;
```

```
start = newnode;
        }
}
void cdll_insert_end()
{
        node *newnode,*temp;
        newnode = getnode();
        nodectr++;
        if(start == NULL)
        {
                start = newnode;
                newnode -> left = start;
                newnode -> right = start;
        }
        else
        {
                newnode -> left = start -> left;
                newnode -> right = start;
                start -> left -> right = newnode;
                start -> left = newnode;
        }
        printf("\n Node Inserted at End");
}
void cdll_insert_mid()
{
        node *newnode, *temp, *prev;
        int pos, ctr = 1;
        newnode = getnode();
        printf("\n Enter the position: ");
        scanf("%d", &pos);
        if(pos - nodectr >= 2)
        {
                printf("\n Position is out of range..");
                return;
        }
        if(pos > 1 && pos <= nodectr)
        {
                temp = start;
                while(ctr < pos - 1)
                {
                        temp = temp -> right;
                        ctr++;
                }
                newnode -> left = temp;
                newnode -> right = temp -> right;
                temp -> right -> left = newnode;
                temp -> right = newnode;
                nodectr++;
                printf("\n Node Inserted at Middle.. ");
        }
        else
                printf("position %d of list is not a middle position", pos);
        }
}
void cdll_delete_beg()
{
        node *temp;
        if(start == NULL)
        {
                printf("\n No nodes exist..");
```

```
getch();
                return ;
        }
        else
        {
                nodectr--;
                if(nodectr == 0)
                {
                         free(start);
                         start = NULL;
                }
                else
                {
                         temp = start;
                         start = start -> right;
                         temp -> left -> right = start;
                         start -> left = temp -> left;
                         free(temp);
                }
                printf("\n Node deleted at Beginning..");
        }
}
void cdll_delete_last()
{
        node *temp;
        if(start == NULL)
        {
                printf("\n No nodes exist..");
                getch();
                return;
        }
        else
        {
                nodectr--;
                if(nodectr == 0)
                {
                         free(start);
                         start = NULL;
                }
                else
                {
                         temp = start;
                         while(temp -> right != start)
                                 temp = temp -> right;
                         temp -> left -> right = temp -> right;
                         temp -> right -> left = temp -> left;
                         free(temp);
                }
                printf("\n Node deleted from end ");
        }
}
void cdll_delete_mid()
{
        int ctr = 1, pos;
        node *temp;
        if( start == NULL)
        {
                printf("\n No nodes exist..");
                getch();
                return;
        }
```

```
else
        {
                printf("\n Which node to delete: ");
                scanf("%d", &pos);
                if(pos > nodectr)
                {
                         printf("\nThis node does not exist");
                         getch();
                         return;
                }
                if(pos > 1 && pos < nodectr)
                {
                         temp = start;
                         while(ctr < pos)
                         {
                                 temp = temp -> right ;
                                 ctr++;
                         }
                         temp -> right -> left = temp -> left;
                         temp -> left -> right = temp -> right;
                         free(temp);
                         printf("\n node deleted..");
                         nodectr--;
                }
                else
                {
                         printf("\n It is not a middle position..");
                         getch();
                }
        }
}
void main(void)
{
        int ch,n;
        clrscr();
        while(1)
        {
                ch = menu();
                switch( ch)
                {
                         case 1 :
                                 printf("\n Enter Number of nodes to create: ");
                                 scanf("%d", &n);
                                 cdll_createlist(n);
                                 printf("\n List created..");
                                 break;
                         case 2 :
                                 cdll_insert_beg();
                                 break;
                         case 3 :
                                 cdll_insert_end();
                                 break;
                         case 4 :
                                 cdll_insert_mid();
                                 break;
                         case 5 :
                                 cdll_delete_beg();
                                 break;
                         case 6 :
                                 cdll_delete_last();
                                 break;
```

```
case 7 :
                                  cdll_delete_mid();
                                  break;
                          case 8 :
                                  cdll_display_left_right();
                                  break;
                          case 9 :
                                  cdll_display_right_left();
                                  break;
                          case 10:
                                  exit(0);
                 }
                 getch();
        }
}
```

## 3.9. Comparison of Linked List Variations:

The major disadvantage of doubly linked lists (over singly linked lists) is that they require more space (every node has two pointer fields instead of one). Also, the code to manipulate doubly linked lists needs to maintain the *prev* fields as well as the *next* fields; the more fields that have to be maintained, the more chance there is for errors.

The major advantage of doubly linked lists is that they make some operations (like the removal of a given node, or a right-to-left traversal of the list) more efficient.

The major advantage of circular lists (over non-circular lists) is that they eliminate some extra-case code for some operations (like deleting last node). Also, some applications lead naturally to circular list representations. For example, a computer network might best be modeled using a circular list.

#### Exercise

- 1. linked list into two lists in the following way. Let the list be L = (l0, l1 n). The resultant lists would be R1 = (l0, l2, l4 2 = (l1, l3, l5
- 2.
- 3. linked list
- 4. Suppose that an ordered list L = (l0, l1 n) is represented by a single linked list. It is required to append the list L = (ln, l0, l1 n) after another ordered list M represented by a single linked list.

5. Implement the following function as a new function for the linked list toolkit.

Precondition: head\_ptr points to the start of a linked list. The list might be empty or it might be non-empty.

Postcondition: The return value is the number of occurrences of 42 in the data field of a node on the linked list. The list itself is unchanged.

6. Implement the following function as a new function for the linked list toolkit.

Precondition: head\_ptr points to the start of a linked list. The list might be empty or it might be non-empty.

Postcondition: The return value is true if the list has at least one occurrence of the number 42 in the data part of a node.

7. Implement the following function as a new function for the linked list toolkit.

Precondition: head\_ptr points to the start of a linked list. The list might be empty or it might be non-empty.

Postcondition: The return value is the sum of all the data components of all the nodes. NOTE: If the list is empty, the function returns 0.

- 8. another circular linked list.
- 9. columns using linked list.
- 10. properly formatted, with zero being printed in place of zero elements.
- 11.
  - 1. Add two m X n sparse matrices and
  - 2. Multiply two m X n sparse matrices.

Where all sparse matrices are to be represented by linked lists.

13. to delete the ith node from the list.

# Multiple Choice Questions

|    | Which among the following is a linear data structure:<br>A. Queue<br>B. Stack                                                                                                                                                                                                                                                                           | C. Linked List<br>D. all the above                                                                       | [ | ] |
|----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|---|---|
|    | Which among the following is a dynamic data structure:<br>A. Double Linked List<br>B. Queue                                                                                                                                                                                                                                                             | C. Stack<br>D. all the above                                                                             | [ | ] |
|    | The link field in a node contains:<br>A. address of the next node<br>B. data of previous node                                                                                                                                                                                                                                                           | C. data of next node<br>D. data of current node                                                          | [ | ] |
|    | by function.<br>A. malloc()<br>B. Calloc()                                                                                                                                                                                                                                                                                                              | Memory is allocated dynamically to a data structure during execution<br>C. realloc()<br>D. all the above | [ | ] |
|    | How many null pointer/s exist in a circular double linked list?<br>A. 1<br>B. 2                                                                                                                                                                                                                                                                         | C. 3<br>D. 0                                                                                             | [ | ] |
| 6. | Suppose that p is a pointer variable that contains the NULL pointer.<br>What happens if your program tries to read or write *p?<br>A. A syntax error always occurs at compilation time.<br>B. A run-time error always occurs when *p is evaluated.<br>C. A run-time error always occurs when the program finishes.<br>D. The results are unpredictable. |                                                                                                          | [ | ] |
| 7. | What kind of list is best to answer questions such as: "What is the<br>item at position n?"<br>A. Lists implemented with an array.<br>B. Doubly-linked lists.<br>C. Singly-linked lists.<br>D. Doubly-linked or singly-linked lists are equally best.                                                                                                   |                                                                                                          | [ | ] |
| 8. | A. Delete the last element of the list<br>B. Add an element before the first element of the list<br>C. Delete the first element of the list<br>D. Interchange the first two elements of the list                                                                                                                                                        | In a single linked list which operation depends on the length of the list.                               | [ | ] |
| 9. | A double linked list is declared as follows:<br>struct dllist<br>{<br>struct dllist *fwd, *bwd;<br>int data;<br>}<br>elements of the list. Which among the following segments of code                                                                                                                                                                   | Where fwd and bwd represents forward and backward links to adjacent                                      | [ | ] |

deletes the element pointed to by X from the double linked list, if it is assumed that X points to neither the first nor last element of the list?

```
A. X -> bwd -> fwd = X -> fwd;
        X -> fwd -> bwd = X -> bwd
     B. X -> bwd -> fwd = X -> bwd;
        X -> fwd -> bwd = X -> fwd
     C. X -> bwd -> bwd = X -> fwd;
        X -> fwd -> fwd = X -> bwd
     D. X -> bwd -> bwd = X -> bwd;
        X -> fwd -> fwd = X -> fwd
10. Which among the following segment of code deletes the element [ ]
     pointed to by X from the double linked list, if it is assumed that X
     points to the first element of the list and start pointer points to
     beginning of the list?
     A. X -> bwd = X -> fwd;
        X -> fwd = X -> bwd
     B. start = X -> fwd;
        start -> bwd = NULL;
     C. start = X -> fwd;
        X -> fwd = NULL
     D. X -> bwd -> bwd = X -> bwd;
        X -> fwd -> fwd = X -> fwd
11. Which among the following segment of code deletes the element [ ]
     pointed to by X from the double linked list, if it is assumed that X
     points to the last element of the list?
     A. X -> fwd -> bwd = NULL;
     B. X -> bwd -> fwd = X -> bwd;
     C. X -> bwd -> fwd = NULL;
     D. X -> fwd -> bwd = X -> bwd;
12. Which among the following segment of code counts the number of [ ]
     elements in the double linked list, if it is assumed that X points to the
     first element of the list and ctr is the variable which counts the number
     of elements in the list?
     A. for (ctr=1; X != NULL; ctr++)
            X = X -> fwd;
     B. for (ctr=1; X != NULL; ctr++)
            X = X -> bwd;
     C. for (ctr=1; X -> fwd != NULL; ctr++)
            X = X -> fwd;
     D. for (ctr=1; X -> bwd != NULL; ctr++)
            X = X -> bwd;
13. Which among the following segment of code counts the number of [ ]
     elements in the double linked list, if it is assumed that X points to the
     last element of the list and ctr is the variable which counts the number
     of elements in the list?
     A. for (ctr=1; X != NULL; ctr++)
            X = X -> fwd;
     B. for (ctr=1; X != NULL; ctr++)
            X = X -> bwd;
     C. for (ctr=1; X -> fwd != NULL; ctr++)
            X = X -> fwd;
     D. for (ctr=1; X -> bwd != NULL; ctr++)
            X = X -> bwd;
```

14. Which among the following segment of code inserts a new node [ ] pointed by X to be inserted at the beginning of the double linked list. The *start* pointer points to beginning of the list?

```
A. X -> bwd = X -> fwd;
  X -> fwd = X -> bwd;
B. X -> fwd = start;
  start -> bwd = X;
  start = X;
C. X -> bwd = X -> fwd;
  X -> fwd = X -> bwd;
  start = X;
D. X -> bwd -> bwd = X -> bwd;
  X -> fwd -> fwd = X -> fwd
```

15. Which among the following segments of inserts a new node pointed by [ ] X to be inserted at the end of the double linked list. The *start* and *last* pointer points to beginning and end of the list respectively?

```
A. X -> bwd = X -> fwd;
  X -> fwd = X -> bwd
B. X -> fwd = start;
  start -> bwd = X;
C. last -> fwd = X; 
  X -> bwd = last;
D. X -> bwd = X -> bwd; 
  X -> fwd = last;
```

16. Which among the following segments of inserts a new node pointed by X to be inserted at any position (i.e neither first nor last) element of

[ ]

the double linked list? Assume *temp* pointer points to the previous position of new node.

```
A. X -> bwd -> fwd = X -> fwd;
  X -> fwd -> bwd = X -> bwd
B. X -> bwd -> fwd = X -> bwd; 
  X -> fwd -> bwd = X -> fwd
C. temp -> fwd = X;
  temp -> bwd = X -> fwd; 
  X ->fwd = x
  X ->fwd->bwd = temp
D. X -> bwd = temp;
  X -> fwd = temp -> fwd; 
  temp ->fwd = X;
  X -> fwd -> bwd = X;
```

17. A single linked list is declared as follows: [ ] struct sllist { struct sllist \*next; int data; } Where next represents links to adjacent elements of the list. Which among the following segments of code deletes the element pointed to by X from the single linked list, if it is assumed that X points to neither the first nor last element of the list? prev pointer points to previous element. A. prev -> next = X -> next; free(X); B. X -> next = prev-> next; free(X); C. prev -> next = X -> next; free(prev); D. X -> next = prev -> next; free(prev); 18. Which among the following segment of code deletes the element [ ] pointed to by X from the single linked list, if it is assumed that X points to the first element of the list and *start* pointer points to beginning of the list? A. X = start -> next; free(X); B. start = X -> next; free(X); C. start = start -> next; free(start); D. X = X -> next; start = X; free(start); 19. Which among the following segment of code deletes the element [ ] pointed to by X from the single linked list, if it is assumed that X points to the last element of the list and prev pointer points to last but one element? A. prev -> next = NULL; free(prev); B. X -> next = NULL; free(X); C. prev -> next = NULL; free(X); D X -> next = prev; free(prev);

20. Which among the following segment of code counts the number of [ ] elements in the single linked list, if it is assumed that X points to the first element of the list and *ctr* is the variable which counts the number of elements in the list? A. for (ctr=1; X != NULL; ctr++) X = X -> next; B. for (ctr=1; X != NULL; ctr--) X = X -> next; C. for (ctr=1; X -> next != NULL; ctr++) X = X -> next; D. for (ctr=1; X -> next != NULL; ctr--) X = X -> next; 21. Which among the following segment of code inserts a new node [ ] pointed by X to be inserted at the beginning of the single linked list. The *start* pointer points to beginning of the list? A. start -> next = X; X = start; B. X -> next = start; start = X C. X -> next = start -> next; start = X D. X -> next = start; start = X -> next 22. Which among the following segments of inserts a new node pointed by [ ] X to be inserted at the end of the single linked list. The *start* and *last* pointer points to beginning and end of the list respectively? A. last -> next = X; X -> next = start; B. X -> next = last; last ->next = NULL; C. last -> next = X; X -> next = NULL; D. last -> next = X -> next; X -> next = NULL; 23. Which among the following segments of inserts a new node pointed by [ ] X to be inserted at any position (i.e neither first nor last) element of the single linked list? Assume *prev* pointer points to the previous position of new node. A. X -> next = prev -> next; prev -> next = X -> next; B. X = prev -> next; prev -> next = X -> next; C. X -> next = prev; prev -> next = X; D. X -> next = prev -> next; prev -> next = X;

24. A circular double linked list is declared as follows: [ ] struct cdllist { struct cdllist \*fwd, \*bwd; int data; } Where fwd and bwd represents forward and backward links to adjacent elements of the list. Which among the following segments of code deletes the element pointed to by X from the circular double linked list, if it is assumed that X points to neither the first nor last element of the list? A. X -> bwd -> fwd = X -> fwd; X -> fwd -> bwd = X -> bwd; B. X -> bwd -> fwd = X -> bwd; X -> fwd -> bwd = X -> fwd; C. X -> bwd -> bwd = X -> fwd; X -> fwd -> fwd = X -> bwd; D. X -> bwd -> bwd = X -> bwd; X -> fwd -> fwd = X -> fwd; 25. Which among the following segment of code deletes the element [ ] pointed to by X from the circular double linked list, if it is assumed that X points to the first element of the list and *start* pointer points to beginning of the list? A. start = start -> bwd; X -> bwd -> bwd = start; start -> bwd = X -> bwd; B. start = start -> fwd; X -> fwd -> fwd = start; start -> bwd = X -> fwd C. start = start -> bwd; X -> bwd -> fwd = X; start -> bwd = X -> bwd D. start = start -> fwd; X -> bwd -> fwd = start; start -> bwd = X -> bwd; 26. Which among the following segment of code deletes the element [ ] pointed to by X from the circular double linked list, if it is assumed that X points to the last element of the list and *start* pointer points to beginning of the list? A. X -> bwd -> fwd = X -> fwd; X -> fwd -> fwd= X -> bwd; B. X -> bwd -> fwd = X -> fwd; X -> fwd -> bwd = X -> bwd; C. X -> fwd -> fwd = X -> bwd;

X -> fwd -> bwd= X -> fwd; D. X -> bwd -> bwd = X -> fwd; X -> bwd -> bwd = X -> bwd;

```
27. Which among the following segment of code counts the number of [ ]
    elements in the circular double linked list, if it is assumed that X and
    start points to the first element of the list and ctr is the variable which
    counts the number of elements in the list?
    A. for (ctr=1; X->fwd != start; ctr++)
           X = X -> fwd;
    B. for (ctr=1; X != NULL; ctr++)
           X = X -> bwd;
    C. for (ctr=1; X -> fwd != NULL; ctr++)
           X = X -> fwd;
    D. for (ctr=1; X -> bwd != NULL; ctr++)
           X = X -> bwd;
28. Which among the following segment of code inserts a new node [ ]
    pointed by X to be inserted at the beginning of the circular double 
    linked list. The start pointer points to beginning of the list?
    A. X -> bwd = start; C. X -> fwd = start -> bwd;
       X -> fwd = start -> fwd; X -> bwd = start;
       start -> bwd-> fwd = X; start -> bwd-> fwd = X;
       start -> bwd = X; start -> bwd = X;
       start = X start = X
     B. X -> bwd = start -> 
       bwd; X -> fwd = start;
       start -> bwd-> fwd = 
       X; start -> bwd = X; 
       start = X
                                     D. X -> bwd = start -> 
                                        bwd; X -> fwd = start;
                                        start -> fwd-> fwd = X;
                                        start -> fwd = X;
                                        X = start;
29. Which among the following segment of code inserts a new node [ ]
    pointed by X to be inserted at the end of the circular double linked list.
    The start pointer points to beginning of the list?
    A. X -> bwd = start; C. X -> bwd= start -> bwd;
       X -> fwd = start -> fwd; X-> fwd = start;
       start -> bwd -> fwd = X; start -> bwd -> fwd = X;
       start -> bwd = X; start -> bwd = X;
       start = X
                                      D. X -> bwd = start -> bwd;
    B. X -> bwd = start -> bwd; X -> fwd = start;
       X -> fwd = start; start -> fwd-> fwd = X;
       start -> bwd -> fwd = X; start -> fwd = X;
       start -> bwd = X; X = start;
       start = X
30. Which among the following segments of inserts a new node pointed by [ ]
    X to be inserted at any position (i.e neither first nor last) element of 
    the circular double linked list? Assume temp pointer points to the 
    previous position of new node.
    A. X -> bwd -> fwd = X -> fwd; C. temp -> fwd = X;
       X -> fwd -> bwd = X -> bwd; temp -> bwd = X -> fwd;
                                         X -> fwd = X;
    B. X -> bwd -> fwd = X -> bwd; X -> fwd -> bwd = temp;
       X -> fwd -> bwd = X -> fwd;
                                      D. X -> bwd = temp;
                                        X -> fwd = temp -> fwd;
                                        temp -> fwd = X;
                                        X -> fwd -> bwd = X;
```