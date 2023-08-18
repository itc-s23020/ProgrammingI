def show_begin_end(func):
    def wrapper(*args, **kwargs):
        print("==begin")
        result = func(*args, **kwargs)
        print("==end")
        return result

    return wrapper


# デコレータを使って関数を定義する


@show_begin_end
def add_numbers(a, b):
    result = a + b
    return result
