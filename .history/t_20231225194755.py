def react(*func, start, debug, time: int = 1):
    in_argv = start
    for i in range(time):
        for i in range(len(func)):
            for j in range(i):
                in_argv = func[j](in_argv)
                try:
                    debug(in_argv)
                except:
                    pass
    return in_argv
