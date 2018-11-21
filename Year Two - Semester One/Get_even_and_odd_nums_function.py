def get_evenodd_list():
    import sys
    odds = []
    evens = []
    nums = sys.stdin.readlines()
    for num in nums:
        num = int(num.strip())
        if num  == -1:
            break
        if num % 2 == 0:
            evens.append(num)
        elif num % 2 != 0:
            odds.append(num)
    return (odds, evens)