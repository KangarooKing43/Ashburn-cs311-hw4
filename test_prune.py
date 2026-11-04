"""
Homework 4: The Pruning Gardener -- verification suite.

Run: python test_prune.py
Prints the Success Token only if every check below passes.
"""

import base64
import hashlib
import random
import sys
from typing import List, Optional

from prune_tree import TreeNode, count_nodes, delete, insert, kth_smallest

ASSIGNMENT_ID = "HW04"


def get_student_id() -> str:
    """Prompt for the student's USI username; baked into the Success Token
    so a copied/shared token decodes to someone else's name, not yours."""
    student_id = input("Enter your USI username (e.g. cwill): ").strip()
    while not student_id:
        student_id = input("Username cannot be blank. Enter your USI username: ").strip()
    return student_id


def generate_token(assignment_id: str, student_id: str) -> str:
    digest = hashlib.sha256(f"CS311-{assignment_id}-{student_id}-VERIFIED".encode()).hexdigest()[:16]
    raw = f"CS311|{assignment_id}|{student_id}|PASS|{digest}"
    return base64.b64encode(raw.encode()).decode()


def print_success_banner(assignment_id: str) -> None:
    student_id = get_student_id()
    token = generate_token(assignment_id, student_id)
    print("\n" + "=" * 60)
    print(f"  ALL CHECKS PASSED -- {assignment_id}")
    print(f"  STUDENT: {student_id}")
    print("  SUCCESS TOKEN (paste this into Blackboard):")
    print(f"  {token}")
    print("=" * 60 + "\n")


def check(label: str, condition: bool, failures: list) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"  [{status}] {label}")
    if not condition:
        failures.append(label)


def inorder(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    return inorder(root.left) + [root.key] + inorder(root.right)


def is_bst(root: Optional[TreeNode], low=float("-inf"), high=float("inf")) -> bool:
    if root is None:
        return True
    if not (low < root.key < high):
        return False
    return is_bst(root.left, low, root.key) and is_bst(root.right, root.key, high)


def main() -> int:
    failures: list = []

    print("Replaying the Part A, Question 3 deletion (delete 25 from the Lab 8 tree)...\n")
    root = None
    for key in [50, 25, 75, 10, 30, 60, 80, 5]:
        root = insert(root, key)

    root = delete(root, 25)
    check("inorder after deleting 25 is [5,10,30,50,60,75,80] (25 gone, rest still sorted)", inorder(root) == [5, 10, 30, 50, 60, 75, 80], failures)
    check("count_nodes reports 7 remaining nodes", count_nodes(root) == 7, failures)
    check("tree still satisfies the BST property after deletion", is_bst(root), failures)

    if failures:
        print(f"\n{len(failures)} check(s) failed -- fix these before the stress test. No token issued.")
        return 1

    print("\nTesting count_nodes and kth_smallest edge cases...\n")
    check("count_nodes(None) == 0", count_nodes(None) == 0, failures)
    check("kth_smallest(None, 1) is None", kth_smallest(None, 1) is None, failures)

    small_root = None
    for key in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        small_root = insert(small_root, key)
    sorted_keys = sorted([8, 3, 10, 1, 6, 14, 4, 7, 13])
    for k in range(1, len(sorted_keys) + 1):
        result = kth_smallest(small_root, k)
        check(f"kth_smallest(tree, {k}) == {sorted_keys[k-1]}", result == sorted_keys[k - 1], failures)
    check("kth_smallest with k out of range returns None", kth_smallest(small_root, 100) is None, failures)

    if failures:
        print(f"\n{len(failures)} check(s) failed. No token issued.")
        return 1

    print("\nRunning randomized stress test (random insert/delete sequences)...\n")
    rng = random.Random(311)
    for trial in range(30):
        keys = rng.sample(range(1000), rng.randint(5, 40))
        stress_root = None
        present = set()
        for key in keys:
            stress_root = insert(stress_root, key)
            present.add(key)

        deletions = rng.sample(keys, k=rng.randint(1, len(keys)))
        for key in deletions:
            stress_root = delete(stress_root, key)
            present.discard(key)
            if not is_bst(stress_root):
                failures.append(f"trial {trial}: BST property violated after deleting {key}")
                break
            if inorder(stress_root) != sorted(present):
                failures.append(f"trial {trial}: inorder contents wrong after deleting {key}")
                break
            if count_nodes(stress_root) != len(present):
                failures.append(f"trial {trial}: count_nodes wrong after deleting {key}")
                break
        if failures:
            break

    check(f"stress test: 30 random insert/delete sequences all preserved the BST property and correct contents", not failures, failures)

    print()
    if failures:
        print(f"{len(failures)} check(s) failed. No token issued.")
        return 1

    print_success_banner(ASSIGNMENT_ID)
    return 0


if __name__ == "__main__":
    sys.exit(main())
