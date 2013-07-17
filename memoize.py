

def memoize(f):
    storage = {}
    def wrapper(*args):
        key = tuple(args)
        if storage.has_key(key):
            return storage[key]
        else:
            result = f(*args)
            storage[key] = result
            return result
    return wrapper



def test_memoize():
    @memoize
    def silly(x):
        if x==0:
            return 0
        else:
            return silly(x-1) + 1

    assert silly(100)==100
    assert silly.func_closure[1].cell_contents[(100,)] == 100




    

