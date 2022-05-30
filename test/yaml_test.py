import getopt
import sys

import yaml


def main():
    opts, args = getopt.getopt(sys.argv[1:], 'l:', [])

    for opt, argv in opts:
        print(opt, argv)

    document = """
      a: 1
      b:
        c: 3
        d: 5
      e: 4
    """

    y1 = yaml.load(document, Loader=yaml.Loader)
    print(y1)
    document = """
      a: 2
      b:
        d: 4
      c: 100
    """
    y2 = yaml.load(document, Loader=yaml.Loader)
    print(y2)

    print({**y1, **y2})

    c = {}
    c.update(y1)
    c.update(y2)
    print(c)
    print('--------------------->')


if __name__ == "__main__":
    main()
