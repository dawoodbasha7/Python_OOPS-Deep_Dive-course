import random


def numbers(*args):
    nums = [random.randint(1,args[0]) for i in range(args[1])]
    return nums


l1 = numbers(100, 5)
l2 = numbers(100, 5)
l3 = numbers(100, 5)

print("zipping:")
print("first method if all the variables are lists: ",(l1+l2+l3))

l1 = list(numbers(100, 5))
l2 = tuple(numbers(100, 5))
l3 = set(numbers(100, 5))

print(type(l1))
print(type(l2))
print(type(l3))

print("if all the variables are different (like above) concatenation doesnt work. ")
print("Other method using '[*l1, *l2, *l3]': ", [*l1, *l2, *l3])
print("-" * 15)


*t, = numbers(50, 5)
print(t)

*t, u = numbers(50, 5)
print(f"t: {t}, u:{u}")

*t, u = numbers(50, 4)
print(f"t: {t}, u:{u}")