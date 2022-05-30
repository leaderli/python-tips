import yaml

document = """
  a: 1
  b:
    c: 3
    d: 4
"""

y = yaml.load(document, Loader=yaml.Loader)
print(y)
