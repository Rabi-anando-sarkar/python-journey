def sum_all(*args):
    return sum(args)

def sum_all_two(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(1,2))
print(sum_all_two(3,2,3))
