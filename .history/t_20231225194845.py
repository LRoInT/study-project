def react(*func, start, debug=lambda x:x, time: int = 1):
    in_argv = start
    for i in range(time):
        for i in range(len(func)):
            for j in range(i):
                in_argv = func[j](in_argv)
                debug(in_argv)
    return in_argv
