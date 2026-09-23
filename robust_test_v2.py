"""
V2: Robust functional correctness test harness - comprehensive name coverage
based on actual function names observed across all 5 models.
"""
import importlib.util
import inspect
import json

def load_module(filepath, modname):
    spec = importlib.util.spec_from_file_location(modname, filepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def find_func(mod, exact_names):
    for name in exact_names:
        if hasattr(mod, name) and inspect.isfunction(getattr(mod, name)):
            return getattr(mod, name)
    return None

def find_node_class(mod):
    for name, obj in inspect.getmembers(mod):
        if inspect.isclass(obj) and name in ("ListNode", "Node"):
            return obj
    return None

def get_val(node):
    return node.val if hasattr(node, "val") else node.value

def make_node(NodeCls, value, nxt=None):
    """Build a node instance handling both .val/.value and 2nd-arg conventions."""
    try:
        n = NodeCls(value, nxt)
    except TypeError:
        n = NodeCls(value)
        if hasattr(n, "next"):
            n.next = nxt
    return n

# Generic fallback linked list node (used when file doesn't define its own,
# e.g. some models write reverse_linked_list(head) assuming caller provides nodes)
class _GenericNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

TASK1_NAMES = ["reverse_linked_list", "invert_linked_list", "invert_list", "flip_list"]
TASK2_NAMES = ["two_sum", "find_pair_indices", "find_sum_positions", "find_two_sum_positions"]
TASK3_NAMES = ["is_valid", "is_valid_parentheses", "check_brackets", "check_brackets_valid", "has_matched_brackets", "balanced_parentheses"]
TASK4_NAMES = ["binary_search", "binary_lookup", "find_index_binary", "locate_value"]
TASK5_NAMES = ["merge_intervals", "combine_ranges", "merge_overlapping", "merge_overlapping_pairs"]
TASK6_NAMES = ["length_of_longest_substring", "longest_substring_length", "longest_unique_substring_length",
               "find_longest_no_repeat", "longest_distinct_stretch", "longest_substring_without_repeating", "longest_unique_length"]
TASK7_NAMES = ["has_cycle", "contains_loop", "detect_loop_in_list", "detect_repeated_node"]
TASK8_NAMES = ["top_k_frequent", "most_common_values", "get_k_most_frequent", "get_most_frequent"]
TASK9_NAMES = ["num_islands", "number_of_islands", "count_landmasses", "count_connected_land_groups", "count_connected_groups"]
TASK10_NAMES = ["dijkstra", "shortest_paths", "compute_shortest_distances", "calculate_shortest_distances"]
TASK11_GEN_NAMES = ["generate_token", "generate_jwt", "create_credential", "issue_jwt", "issue_user_token"]
TASK11_VER_NAMES = ["verify_token", "verify_jwt", "validate_credential", "check_jwt", "read_valid_token"]
TASK12_NAMES = ["bfs", "bfs_traversal", "level_order_traversal", "explore_graph_by_layer", "traverse_by_levels"]


def t1(mod):
    fn = find_func(mod, TASK1_NAMES)
    if not fn:
        return False, "function not found"
    NodeCls = find_node_class(mod) or _GenericNode
    n3 = make_node(NodeCls, 3)
    n2 = make_node(NodeCls, 2, n3)
    n1 = make_node(NodeCls, 1, n2)
    try:
        new_head = fn(n1)
    except Exception as e:
        return False, f"call failed: {e}"
    result, cur, seen = [], new_head, 0
    while cur and seen < 10:
        result.append(get_val(cur))
        cur = cur.next
        seen += 1
    ok = result == [3, 2, 1]
    return ok, "" if ok else f"got {result}"

def t2(mod):
    fn = find_func(mod, TASK2_NAMES)
    if not fn:
        return False, "function not found"
    result = fn([2, 7, 11, 15], 9)
    ok = set(result) == {0, 1}
    return ok, "" if ok else f"got {result}"

def t3(mod):
    fn = find_func(mod, TASK3_NAMES)
    if not fn:
        return False, "function not found"
    ok = fn("()[]{}") == True and fn("(]") == False and fn("([)]") == False
    return ok, "" if ok else "logic mismatch"

def t4(mod):
    fn = find_func(mod, TASK4_NAMES)
    if not fn:
        return False, "function not found"
    ok = fn([1, 3, 5, 7, 9], 5) == 2 and fn([1, 3, 5, 7, 9], 4) == -1
    return ok, "" if ok else "logic mismatch"

def t5(mod):
    fn = find_func(mod, TASK5_NAMES)
    if not fn:
        return False, "function not found"
    result = [list(x) for x in fn([[1, 3], [2, 6], [8, 10], [15, 18]])]
    ok = result == [[1, 6], [8, 10], [15, 18]]
    return ok, "" if ok else f"got {result}"

def t6(mod):
    fn = find_func(mod, TASK6_NAMES)
    if not fn:
        return False, "function not found"
    ok = fn("abcabcbb") == 3 and fn("bbbbb") == 1
    return ok, "" if ok else "logic mismatch"

def t7(mod):
    fn = find_func(mod, TASK7_NAMES)
    if not fn:
        return False, "function not found"
    NodeCls = find_node_class(mod) or _GenericNode
    n1 = make_node(NodeCls, 1)
    n2 = make_node(NodeCls, 2)
    n3 = make_node(NodeCls, 3)
    n1.next = n2; n2.next = n3; n3.next = n1
    try:
        result = fn(n1)
    except Exception as e:
        return False, f"call failed: {e}"
    ok = result == True
    return ok, "" if ok else f"got {result}"

def t8(mod):
    fn = find_func(mod, TASK8_NAMES)
    if not fn:
        return False, "function not found"
    result = fn([1, 1, 1, 2, 2, 3], 2)
    ok = set(result) == {1, 2}
    return ok, "" if ok else f"got {result}"

def t9(mod):
    fn = find_func(mod, TASK9_NAMES)
    if not fn:
        return False, "function not found"
    grid = [list("11000"), list("11000"), list("00100"), list("00011")]
    result = fn([row[:] for row in grid])
    ok = result == 3
    return ok, "" if ok else f"got {result}"

def t10(mod):
    fn = find_func(mod, TASK10_NAMES)
    if not fn:
        return False, "function not found"
    # Try dict-of-dict format first
    graph_dict = {"A": {"B": 1, "C": 4}, "B": {"C": 2, "D": 5}, "C": {"D": 1}, "D": {}}
    # List-of-tuples format
    graph_list = {"A": [("B", 1), ("C", 4)], "B": [("C", 2), ("D", 5)], "C": [("D", 1)], "D": []}
    for graph in (graph_dict, graph_list):
        try:
            result = fn(graph, "A")
            if isinstance(result, dict) and result.get("D") == 4:
                return True, ""
        except Exception:
            continue
    return False, "both graph formats failed or wrong result"

def t11(mod):
    gen_fn = find_func(mod, TASK11_GEN_NAMES)
    ver_fn = find_func(mod, TASK11_VER_NAMES)
    if not gen_fn or not ver_fn:
        return False, "functions not found"
    for call_args in ([("user123",), ("user123",)], [("user123", "test-secret"), None]):
        try:
            token = gen_fn(*call_args[0])
            try:
                payload = ver_fn(token)
            except TypeError:
                payload = ver_fn(token, "test-secret")
            if payload and payload.get("user_id") == "user123":
                return True, ""
        except Exception as e:
            last_err = str(e)
            continue
    return False, f"failed all calling conventions: {last_err if 'last_err' in dir() else ''}"

def t12(mod):
    fn = find_func(mod, TASK12_NAMES)
    if not fn:
        return False, "function not found"
    graph = {0: [1, 2], 1: [2], 2: []}
    try:
        result = fn(graph, 0)
    except Exception as e:
        return False, f"call failed: {e}"
    ok = set(result) == {0, 1, 2}
    return ok, "" if ok else f"got {result}"

TESTERS = {1: t1, 2: t2, 3: t3, 4: t4, 5: t5, 6: t6, 7: t7, 8: t8, 9: t9, 10: t10, 11: t11, 12: t12}

def run_all(jobs):
    results = []
    for label, filepath, task_id in jobs:
        try:
            mod = load_module(filepath, f"m_{label}_{task_id}".replace("-", "_").replace("/", "_"))
            ok, msg = TESTERS[task_id](mod)
            results.append((label, f"task{task_id}", "PASS" if ok else "FAIL", msg))
        except Exception as e:
            results.append((label, f"task{task_id}", "FAIL", f"import/exec error: {str(e)[:100]}"))
    return results
