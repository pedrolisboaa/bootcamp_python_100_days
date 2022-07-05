# def somar_geral(*args):
#     total = 0
#     x = sum([x for x in args])
#     return x
#
#
# print(somar_geral(1, 2, 3, 4, 5))

def test(*args):
    print(args)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)







