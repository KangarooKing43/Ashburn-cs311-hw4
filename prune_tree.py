"""
Homework 4: The Pruning Gardener -- starter.

Complete delete, count_nodes, and kth_smallest below. TreeNode and
insert are already provided -- do not modify them. See
HW4_The_Pruning_Gardener.md, Part B, for the full requirements.
"""

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
    Recursively delete `key` from the subtree rooted at `root`.
    Return the new subtree root. Handle all three cases from Part A,
    Question 1 (leaf, one child, two children -- via inorder
    successor). Deleting a key not present should leave the tree
    unchanged.
    """
    # TODO
    raise NotImplementedError


def count_nodes(root: Optional[TreeNode]) -> int:
    """Recursively return the number of nodes in the subtree rooted at `root`."""
    # TODO
    raise NotImplementedError


def kth_smallest(root: Optional[TreeNode], k: int) -> Optional[int]:
    """
    Return the k-th smallest key (1-indexed) in the subtree rooted at
    `root`, using count_nodes on subtrees to navigate directly instead
    of a full inorder traversal. Return None if k is out of range.
    """
    # TODO
    raise NotImplementedError
