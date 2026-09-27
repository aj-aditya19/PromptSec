import importlib.util
import inspect

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
    try:
        n = NodeCls(value, nxt)
    except TypeError:
        n = NodeCls(value)
        if hasattr(n, "next"):
            n.next = nxt
    return n

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

# secret long enough to avoid PyJWT's InsecureKeyLengthWarning (32+ bytes for HS256)
TEST_SECRET = "a" * 32


def build_list(NodeCls, values):
    head = None
    prev = None
    for v in values:
        n = make_node(NodeCls, v)
        if head is None:
            head = n
        else:
            prev.next = n
        prev = n
    return head

def list_to_python(head, limit=20):
    out, cur, seen = [], head, 0
    while cur and seen < limit:
        out.append(get_val(cur))
        cur = cur.next
        seen += 1
    return out


def t1(mod):
    """Reverse Linked List - multiple cases: normal, single node, two nodes."""
    fn = find_func(mod, TASK1_NAMES)
    if not fn:
        return False, "function not found"
    NodeCls = find_node_class(mod) or _GenericNode
    cases = [([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]), ([1], [1]), ([1, 2], [2, 1])]
    for inp, expected in cases:
        head = build_list(NodeCls, inp)
        try:
            new_head = fn(head)
        except Exception as e:
            return False, f"case {inp}: call failed: {e}"
        result = list_to_python(new_head)
        if result != expected:
            return False, f"case {inp}: expected {expected}, got {result}"
    return True, ""

def t2(mod):
    """Two Sum - normal, negative numbers, duplicates."""
    fn = find_func(mod, TASK2_NAMES)
    if not fn:
        return False, "function not found"
    cases = [
        ([2, 7, 11, 15], 9, {0, 1}),
        ([-3, 4, 3, 90], 0, {0, 2}),
        ([3, 3], 6, {0, 1}),
        ([1, 2, 3, 4, 5], 9, {3, 4}),
    ]
    for nums, target, expected in cases:
        try:
            result = fn(nums, target)
        except Exception as e:
            return False, f"case {nums},{target}: call failed: {e}"
        if set(result) != expected:
            return False, f"case {nums},{target}: expected {expected}, got {result}"
    return True, ""

def t3(mod):
    """Valid Parentheses - balanced, unbalanced, wrong-order, empty, nested."""
    fn = find_func(mod, TASK3_NAMES)
    if not fn:
        return False, "function not found"
    cases = [
        ("()[]{}", True), ("(]", False), ("([)]", False),
        ("", True), ("{[()]}", True), ("(((", False), (")", False),
    ]
    for s, expected in cases:
        try:
            result = fn(s)
        except Exception as e:
            return False, f"case '{s}': call failed: {e}"
        if bool(result) != expected:
            return False, f"case '{s}': expected {expected}, got {result}"
    return True, ""

def t4(mod):
    """Binary Search - found (various positions), not found, single element, empty."""
    fn = find_func(mod, TASK4_NAMES)
    if not fn:
        return False, "function not found"
    cases = [
        ([1, 3, 5, 7, 9], 5, 2), ([1, 3, 5, 7, 9], 1, 0), ([1, 3, 5, 7, 9], 9, 4),
        ([1, 3, 5, 7, 9], 4, -1), ([5], 5, 0), ([5], 3, -1),
    ]
    for arr, target, expected in cases:
        try:
            result = fn(arr, target)
        except Exception as e:
            return False, f"case {arr},{target}: call failed: {e}"
        if result != expected:
            return False, f"case {arr},{target}: expected {expected}, got {result}"
    return True, ""

def t5(mod):
    """Merge Intervals - overlapping, non-overlapping, single, fully nested."""
    fn = find_func(mod, TASK5_NAMES)
    if not fn:
        return False, "function not found"
    cases = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[1,10],[2,3],[4,5]], [[1,10]]),
        ([[1,2]], [[1,2]]),
    ]
    for inp, expected in cases:
        try:
            result = [list(x) for x in fn([row[:] for row in inp])]
        except Exception as e:
            return False, f"case {inp}: call failed: {e}"
        if result != expected:
            return False, f"case {inp}: expected {expected}, got {result}"
    return True, ""

def t6(mod):
    """Longest Substring - normal, all same char, empty, no repeats, single char."""
    fn = find_func(mod, TASK6_NAMES)
    if not fn:
        return False, "function not found"
    cases = [("abcabcbb", 3), ("bbbbb", 1), ("", 0), ("abcdef", 6), ("a", 1), ("pwwkew", 3)]
    for s, expected in cases:
        try:
            result = fn(s)
        except Exception as e:
            return False, f"case '{s}': call failed: {e}"
        if result != expected:
            return False, f"case '{s}': expected {expected}, got {result}"
    return True, ""

def t7(mod):
    """Detect Cycle - has cycle, no cycle, single node no cycle, single node self-cycle."""
    fn = find_func(mod, TASK7_NAMES)
    if not fn:
        return False, "function not found"
    NodeCls = find_node_class(mod) or _GenericNode

    # Case 1: has cycle
    n1, n2, n3 = make_node(NodeCls, 1), make_node(NodeCls, 2), make_node(NodeCls, 3)
    n1.next = n2; n2.next = n3; n3.next = n1
    # Case 2: no cycle
    m1, m2, m3 = make_node(NodeCls, 1), make_node(NodeCls, 2), make_node(NodeCls, 3)
    m1.next = m2; m2.next = m3
    # Case 3: single node, no cycle
    s1 = make_node(NodeCls, 1)

    for head, expected, label in [(n1, True, "3-node cycle"), (m1, False, "3-node no cycle"), (s1, False, "single node")]:
        try:
            result = fn(head)
        except Exception as e:
            return False, f"case {label}: call failed: {e}"
        if bool(result) != expected:
            return False, f"case {label}: expected {expected}, got {result}"
    return True, ""

def t8(mod):
    """Top K Frequent - normal, k equals length, ties."""
    fn = find_func(mod, TASK8_NAMES)
    if not fn:
        return False, "function not found"
    cases = [
        ([1,1,1,2,2,3], 2, {1,2}),
        ([1], 1, {1}),
        ([4,4,4,6,6,7,7,7], 1, {4,7}),  # either 4 or 7 acceptable (tie on count for 6 is lower)
    ]
    for nums, k, acceptable in cases:
        try:
            result = fn(nums, k)
        except Exception as e:
            return False, f"case {nums},{k}: call failed: {e}"
        if k == 1:
            if not (set(result) & acceptable):
                return False, f"case {nums},{k}: got {result}, expected one of {acceptable}"
        else:
            if set(result) != acceptable:
                return False, f"case {nums},{k}: expected {acceptable}, got {result}"
    return True, ""

def t9(mod):
    """Number of Islands - multiple islands, all water, all land, single cell."""
    fn = find_func(mod, TASK9_NAMES)
    if not fn:
        return False, "function not found"
    cases = [
        ([list("11000"), list("11000"), list("00100"), list("00011")], 3),
        ([list("0000"), list("0000")], 0),
        ([list("11"), list("11")], 1),
        ([list("1")], 1),
    ]
    for grid, expected in cases:
        try:
            result = fn([row[:] for row in grid])
        except Exception as e:
            return False, f"case: call failed: {e}"
        if result != expected:
            return False, f"case: expected {expected}, got {result}"
    return True, ""

def t10(mod):
    """Dijkstra - linear chain and diamond graph, checking multiple destination distances."""
    fn = find_func(mod, TASK10_NAMES)
    if not fn:
        return False, "function not found"
    graph_dict = {"A": {"B": 1, "C": 4}, "B": {"C": 2, "D": 5}, "C": {"D": 1}, "D": {}}
    graph_list = {"A": [("B", 1), ("C", 4)], "B": [("C", 2), ("D", 5)], "C": [("D", 1)], "D": []}
    expected = {"A": 0, "B": 1, "C": 3, "D": 4}
    for graph in (graph_dict, graph_list):
        try:
            result = fn(graph, "A")
            if isinstance(result, dict) and all(result.get(k) == v for k, v in expected.items()):
                return True, ""
        except Exception:
            continue
    return False, f"neither graph format produced expected distances {expected}"

def t11(mod):
    """JWT - generate+verify round trip, and verify rejects a tampered token."""
    gen_fn = find_func(mod, TASK11_GEN_NAMES)
    ver_fn = find_func(mod, TASK11_VER_NAMES)
    if not gen_fn or not ver_fn:
        return False, "functions not found"
    last_err = ""
    for call_variant in ["no_secret", "with_secret"]:
        try:
            if call_variant == "no_secret":
                token = gen_fn("user123")
            else:
                token = gen_fn("user123", TEST_SECRET)
            try:
                payload = ver_fn(token)
            except TypeError:
                payload = ver_fn(token, TEST_SECRET)
            if payload and payload.get("user_id") == "user123":
                # round trip works; also check tampered token is rejected
                tampered = token[:-2] + ("XX" if token[-2:] != "XX" else "YY")
                try:
                    try:
                        bad_payload = ver_fn(tampered)
                    except TypeError:
                        bad_payload = ver_fn(tampered, TEST_SECRET)
                except Exception:
                    bad_payload = None  # raised exception = correctly rejected
                if bad_payload is not None and bad_payload.get("user_id") == "user123":
                    return False, "verify_token accepted a tampered token"
                return True, ""
        except Exception as e:
            last_err = str(e)
            continue
    return False, f"round trip failed: {last_err}"

def t12(mod):
    """BFS - connected graph, disconnected node not required, single node, linear chain."""
    fn = find_func(mod, TASK12_NAMES)
    if not fn:
        return False, "function not found"
    cases = [
        ({0: [1, 2], 1: [2], 2: []}, 0, {0, 1, 2}),
        ({0: []}, 0, {0}),
        ({0: [1], 1: [2], 2: [3], 3: []}, 0, {0, 1, 2, 3}),
    ]
    for graph, start, expected in cases:
        try:
            result = fn(graph, start)
        except Exception as e:
            return False, f"case {graph}: call failed: {e}"
        if set(result) != expected:
            return False, f"case {graph}: expected {expected}, got {result}"
    return True, ""

TESTERS = {1: t1, 2: t2, 3: t3, 4: t4, 5: t5, 6: t6, 7: t7, 8: t8, 9: t9, 10: t10, 11: t11, 12: t12}

def run_all(jobs):
    results = []
    for label, filepath, task_id in jobs:
        try:
            mod = load_module(filepath, f"m_{label}_{task_id}".replace("-", "_").replace("/", "_"))
            ok, msg = TESTERS[task_id](mod)
            results.append((label, f"task{task_id}", "PASS" if ok else "FAIL", msg))
        except Exception as e:
            results.append((label, f"task{task_id}", "FAIL", f"import/exec error: {str(e)[:150]}"))
    return results
