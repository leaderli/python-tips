def deep_get(d, keys, reversed=True):
    if reversed:
        keys.reverse()

    while keys:
        key = keys.pop()
        d = d.get(key, {})

    return d
