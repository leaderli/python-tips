def deep_get(d, keys, reverse=True):
    if reverse:
        keys.reverse()

    while keys:
        key = keys.pop()
        d = d.get(key, {})

    return d
