#include "ft_btree.h"

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


int main(void)
{

    char *str = "creating node";
    char *node_content = btree_create_node(str)->item;
    if(!node_content)
        return(0);
    printf("print content : %s", node_content);
}
