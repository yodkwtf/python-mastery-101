def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            #convert args into something mutable   
            newargs = []        
            for (a, t) in zip(args, types):
                # zip((1,2) , (3,4)) -> (1,3) & (2,4)
               newargs.append( t(a)) #feel free to have more elaborated convertion
            return f(*newargs, **kwargs)
        return new_func
    return decorator

@enforce(str, int)
def repeat_msg(msg, times):
	for time in range(times):
		print(msg)

# repeat_msg("hello", '5')

@enforce(float, float)
def divide(a,b):
	print(a/b)
divide('1', '4')
