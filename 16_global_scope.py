a = 10


def fun():
    global a
    a = 20
    print(a)


fun()
print("After Global Used")
print(a)
