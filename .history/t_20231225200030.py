def react(*func, start, debug=len, time: int = 1):
    in_argv = start
    for i in range(time):
        for i in range(len(func)):
            for j in range(i+1):
                in_argv = func[j](in_argv)
                try:
                    debug(in_argv,func[j].__name__)
                except:
                    pass
    return in_argv


def a(i):
    return i + 1


def b(i):
    return i * 2


def c(i):
    return i ** 2


print(react(a, b, c, start=5, time=2,debug=print))
