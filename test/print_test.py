from li import li_log


table = [['a', 'b', 'c'],
         ['aaaaaaaaaa', 'b', 'c'],
         ['a', 'bbbbbbbbbb', 'c'],
         ['a', 'bbbbbbbbbb' * 10, 'c']]

# for t in table:
#     a, b, c = t;
#
#     # print(len(a), len(b), len(c))
#
#     print("{:<10} {:<10} {:<10} {:<0}".format(a, b, c, None))

# print("{:<%s} %d" % (1, 22))

li_log.format_table(table)

# print('{}{}'.format(1,2))
# print('{}{}'.format(1))
table.append(1)
li_log.format_table(table)
# print(li_log.formatted_table([]))
# print(li_log.formatted_table(()))

# print((0,) * 10)
# a = [x for x in range(2)]
# print("{:<10} {:<10} {:<10} {:<0}".format(*a))
# print("%s %s" % tuple(a))
# print("%s %s" % (1,2,3))
# print("{:<%d} %d" % tuple(a))
