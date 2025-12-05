#ifndef FT_BTREE_H
#define FT_BTREE_H

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

typedef struct s_btree
{
    struct s_btree *left;
    struct s_btree *right;
    void *item;
} t_btree;


#endif
