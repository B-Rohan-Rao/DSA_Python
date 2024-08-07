# Just to understand the concept of Trees
# The different dict items represents different items in this tress
# This just an example of binary tree(Trees with 2 branches). However, There can be tress with multiple branches.
head = {
    "value": 11,   # Parent Node
    "left": {
        "value": 7,   # Child Node, Sibling Node and parent node for next node
        "left": None,  # leaf Node as it do not have any more child node.
        "right": None
    },
    "right": {
        "value": 3,   # Child Node, Sibling Node and parent node for next node
        "left": None,
        "right": None
    }
}
