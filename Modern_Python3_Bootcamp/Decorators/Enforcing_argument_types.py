

def enforce(*types):
    def decorator(func):
        def new_func(*args, **kwargs):
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append(t(a))
            return func(*newargs, **kwargs)
        return new_func
    return decorator


@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)
        
        
repeat_msg("hello", "3")