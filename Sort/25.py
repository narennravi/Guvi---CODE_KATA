# Question:-
'''
You are given a preorder traversal of binary search tree print the post order traversal of it.

Input Description:
You are given with preorder traversal of binary search tree

Output Description:
Print the post order traversal of tree

Sample Input :
1 0 2

Sample Output :
0 2 1
'''



# Solution:-
def construct_postorder(preorder):
    if not preorder:
        return []

    root = preorder[0]
    left_subtree = [x for x in preorder if x < root]
    right_subtree = [x for x in preorder if x > root]

    postorder_left = construct_postorder(left_subtree)
    postorder_right = construct_postorder(right_subtree)

    return postorder_left + postorder_right + [root]


# Read input
preorder = list(map(int, input().split()))

# Compute postorder traversal
postorder = construct_postorder(preorder)

# Print the postorder traversal
print(' '.join(map(str, postorder)))
