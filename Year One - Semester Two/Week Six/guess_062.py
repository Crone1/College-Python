
def find():
    low = bottom
    high = top

    while high != low:

        mid = (low + high) // 2

        x = guess(mid)

        if x == -1:
            low = mid + 1

        elif x == 0:
            return mid

        elif x == 1:
            high = mid
