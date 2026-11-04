
from typing import Optional


class TreeNode:
    __slots__ = ("key", "left", "right")

    def __init__(self, key: int) -> None:
        self.key = key
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


def insert(root: Optional[TreeNode], key: int) -> TreeNode:
    """Given: standard BST insert. Do not modify."""
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root


def delete(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    """
    Recursively delete key from the BST.
    Return the new subtree root.
    """

    # Base case: empty subtree
    if root is None:
        return None

    # Search left subtree
    if key < root.key:
        root.left = delete(root.left, key)

    # Search right subtree
    elif key > root.key:
        root.right = delete(root.right, key)

    # Found the node to delete
    else:

        # Case 1: Leaf node
        if root.left is None and root.right is None:
            return None

        # Case 2: Only right child
        elif root.left is None:
            return root.right

        # Case 2: Only left child
        elif root.right is None:
            return root.left

        # Case 3: Two children
        else:
            # Find inorder successor
            successor = root.right

            while successor.left is not None:
                successor = successor.left

            # Replace current key with successor key
            root.key = successor.key

            # Delete original successor
            root.right = delete(root.right, successor.key)

    return root


def count_nodes(root: Optional[TreeNode]) -> int:
    """Recursively count the nodes in a BST."""

    # Base case: empty subtree
    if root is None:
        return 0

    # Count current node and both subtrees
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def kth_smallest(root: Optional[TreeNode], k: int) -> Optional[int]:
    """
    Return the k-th smallest key (1-indexed).
    Return None if k is out of range.
    """

    # Base cases: empty tree or invalid k
    if root is None or k < 1:
        return None

    # Count nodes in left subtree
    left_count = count_nodes(root.left)

    # Current node is the k-th smallest
    if k == left_count + 1:
        return root.key

    # Search left subtree
    elif k <= left_count:
        return kth_smallest(root.left, k)

    # Search right subtree with adjusted k
    else:
        return kth_smallest(root.right, k - left_count - 1)
