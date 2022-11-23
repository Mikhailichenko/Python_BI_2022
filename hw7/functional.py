def sequential_map (*args):
    *functions , numbers = args
    for func in functions:
        numbers = map(func, numbers)
    return list(numbers)


def sequential_map_wc (*args):
    *functions , numbers = args
    my_chain = func_chain(*functions)
    return my_chain(numbers)


def consensus_filter (*args):
    *functions , numbers = args
    for func in functions:
        numbers = filter(func, numbers)
    
    return list(numbers)


def conditional_reduce (condition, func_red, *args):
    numbers = list(filter(condition, args[0]))
    ans = numbers[0]
    for i in range(1, len(numbers)):
        ans = func_red(ans, numbers[i])
    return ans


def func_chain(*args):
    def new_chain(numbers):
        ans = args[0](numbers)
        for i in range(1, len(args)):
            ans = args[i](ans)
        return ans
    return new_chain






