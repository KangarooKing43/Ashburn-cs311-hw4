# Homework 4: The Pruning Gardener

CS 311: Data Structures & Algorithms, Fall 2026, University of Southern Indiana.

## Get started

Open https://github.com/cwillpinto/cs311-hw04-pruning-gardener and select **Use this template > Create a new repository** under your own GitHub account. Clone your new repository and work there.

Complete `delete`, `count_nodes`, and `kth_smallest` in `prune_tree.py`. `TreeNode` and `insert` are provided; do not modify them.

```sh
python test_prune.py
```

The starter intentionally raises `NotImplementedError` until you implement the functions. The harness checks the assignment deletion trace, node counts, kth-smallest queries on a fixed tree, empty and out-of-range queries, and 30 randomized deletion sequences. Once all checks pass, enter your USI username to generate your Success Token.

Commit and push your work to your own repository.

### Direct-clone alternative

Create an empty repository under your own account first, then run:

```sh
git clone https://github.com/cwillpinto/cs311-hw04-pruning-gardener.git
cd cs311-hw04-pruning-gardener
git remote rename origin upstream
git remote add origin <your-own-repository-url>
git remote -v
git push -u origin main
```

Replace the placeholder with your repository URL. Confirm `origin` points to your account before pushing; use your actual branch name if different from `main`.

## Submit in Blackboard

1. `HW4_Theory.pdf` (or `.md`)
2. Your completed `prune_tree.py`
3. The Success Token from `test_prune.py`
