from li.li_util import deep_get

d = {
    'a': 1,
    'map': {
        "m1": 'm1',
        "m2": 'm2'
    }
}

assert deep_get(d, ['a']) == 1
assert deep_get(d, ['map', "m1"]) == "m1"
assert deep_get(d, ['map', "m1", "m"]) == "m1"
