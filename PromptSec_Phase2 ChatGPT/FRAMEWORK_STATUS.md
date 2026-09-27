# PromptSec Phase 2 — Framework Status

## Initial status

Model: ChatGPT
Collection status: **0 / 192 samples**
Analysis status: **Not started**
Validation status: **Not started**

## Progress tracker

| Task | Original | Typo | Synonym | Paraphrase | Total |
|---|---:|---:|---:|---:|---:|
| Reverse Linked List | 0/4 | 0/4 | 0/4 | 0/4 | 0/16 |
| Two Sum | 0/4 | 0/4 | 0/4 | 0/4 | 0/16 |
| Valid Parentheses | 0/4 | 0/4 | 0/4 | 0/4 | 0/16 |
| Binary Search | 0/4 | 0/4 | 0/4 | 0/4 | 0/16 |
| Merge Intervals | 0/4 | 0/4 | 0/4 | 0/4 | 0/16 |
| Longest Substring Without Repeating Characters | 0/4 | 0/4 | 0/4 | 0/4 | 0/16 |
| Detect Cycle in Linked List | 0/4 | 0/4 | 0/4 | 0/4 | 0/16 |
| Top K Frequent Elements | 0/4 | 0/4 | 0/4 | 0/4 | 0/16 |
| Number of Islands | 0/4 | 0/4 | 0/4 | 0/4 | 0/16 |
| Dijkstra's Shortest Path | 0/4 | 0/4 | 0/4 | 0/4 | 0/16 |
| JWT Authentication | 0/4 | 0/4 | 0/4 | 0/4 | 0/16 |
| BFS Graph Traversal | 0/4 | 0/4 | 0/4 | 0/4 | 0/16 |
| **TOTAL** | **0/48** | **0/48** | **0/48** | **0/48** | **0/192** |

## Validation target

A complete dataset has:
- 12 tasks;
- 4 variants per task;
- 4 repetitions per variant;
- 192 Python source files.

## Sample analysis example

Suppose a variant contains 1 bare-except sample out of 4:
- `bare_except = 1`
- `total_samples = 4`
- `bare_except_pct = 25.00`

This is an example of reporting, not an actual research result.

## Validation checklist

- [ ] All 192 files exist.
- [ ] No variant has missing repetitions.
- [ ] Model metadata recorded.
- [ ] Prompt wording unchanged.
- [ ] Outputs retained without selective deletion.
- [ ] Batch analyzer completed.
- [ ] Fisher tests completed or SciPy limitation recorded.
- [ ] Optional Bandit scan completed if used.
- [ ] JWT outputs qualitatively reviewed.
