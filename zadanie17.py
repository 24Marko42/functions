def mirror(arr):
    # mirrored_part = arr.reverse()
    # arr = arr + mirrored_part
    arr = arr + arr[::-1]
    return arr


arr = [1, 2]

print(mirror(arr))
