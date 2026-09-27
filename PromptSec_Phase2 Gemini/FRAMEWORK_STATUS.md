# PromptSec Phase 2 Framework Status Tracker (Gemini)

## Overall Progress
- **Target Model:** Gemini
- **Total Samples Collected:** 0 / 192 (0%)
- **Framework Setup Status:** Ready

## Task Breakdown Tracker

| Task ID | Task Name | Original (0/4) | Typo (0/4) | Synonym (0/4) | Paraphrase (0/4) | Status |
|---|---|---|---|---|---|---|
| 1 | Reverse Linked List | 0 | 0 | 0 | 0 | Pending |
| 2 | Two Sum | 0 | 0 | 0 | 0 | Pending |
| 3 | Valid Parentheses | 0 | 0 | 0 | 0 | Pending |
| 4 | Binary Search | 0 | 0 | 0 | 0 | Pending |
| 5 | Merge Intervals | 0 | 0 | 0 | 0 | Pending |
| 6 | Longest Substring | 0 | 0 | 0 | 0 | Pending |
| 7 | Detect Cycle | 0 | 0 | 0 | 0 | Pending |
| 8 | Top K Frequent | 0 | 0 | 0 | 0 | Pending |
| 9 | Number of Islands | 0 | 0 | 0 | 0 | Pending |
| 10 | Dijkstra's Shortest Path | 0 | 0 | 0 | 0 | Pending |
| 11 | JWT Authentication ⭐ | 0 | 0 | 0 | 0 | Pending |
| 12 | BFS Graph Traversal | 0 | 0 | 0 | 0 | Pending |

---

## Sample Vulnerability Example
```python
# EXAMPLE VULNERABLE SAMPLE (JWT Task - Typo Variant)
import jwt

def verify_token(token):
    try:
        payload = jwt.decode(token, "secret123", algorithms=["HS256"]) # Hardcoded secret
        return payload
    except: # Bare except pattern
        return None
```
