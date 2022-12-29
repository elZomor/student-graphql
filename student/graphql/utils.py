def login_required(func):
    def inner1(*args, **kwargs):
        print("before Execution")
        print(args)

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1
