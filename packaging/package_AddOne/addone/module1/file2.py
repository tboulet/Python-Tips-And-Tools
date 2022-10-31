from addone.file1 import add_one

def recursive_add_one(x, n):
    if n == 1:
        return add_one(x)
    else:
        return recursive_add_one(x, n-1) + 1
        