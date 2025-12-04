#include "ft_btree.h"


void btree_apply_prefix(t_btree *root, void (*applyf)(void *))
{
    if(!root)
        return;

    applyf(root->item);

    btree_apply_prefix(root->left, applyf);
    btree_apply_prefix(root->right, applyf);

}

t_btree *btree_create_node(void *item)
{

    t_btree *new_node;

    if(!item)
        return(NULL);

    new_node = malloc(sizeof(t_btree));
    if(!new_node)
        return (NULL);

    new_node -> item = item;
    new_node -> left = 0;
    new_node -> right = 0;

    return(new_node);
}

void ft_putstr(void* str)
{
    int i = 0;
    char *s = (char *)str;
    while(s[i])
    {
        write(1,&s[i],1);
        i++;
    }
    write(1, " |", 2);

}



int main(void)
{
    t_btree *nodeA = btree_create_node("A");
    t_btree *nodeB = btree_create_node("B");
    t_btree *nodeC = btree_create_node("C");
    t_btree *nodeD = btree_create_node("D");
    t_btree *nodeE = btree_create_node("E");
    t_btree *nodeF = btree_create_node("F");

    nodeA -> left = nodeB;
    nodeA -> right = nodeC;

    nodeB -> left = nodeD;
    nodeB -> right = nodeE;

    nodeC -> left = nodeF;

    
    btree_apply_prefix(nodeA, ft_putstr);



}
