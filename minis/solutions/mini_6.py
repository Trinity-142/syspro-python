def flatten(arr, depth=float('inf')):
    """Flattens a list of lists."""
    if depth < 0:
        return [arr]
    res = []
    for i in arr:
        if isinstance(i, list):
            res.extend(flatten(i, depth - 1))
        else:
            res.append(i)
    return res
