def identify_pair(data, objective):
    """Search through data to find pair matching objective"""
    tracker = {}
    for position, item in enumerate(data):
        seek = objective - item
        if seek in tracker:
            return [tracker[seek], position]
        tracker[item] = position
    return None
