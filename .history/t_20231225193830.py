def react(*func,start,debug:function):
    in_argv=start
    for i in range(len(func)):
        for j in range(i):
            in_argv=func[j](in_argv)


    