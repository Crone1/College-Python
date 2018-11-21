def get_odd_list():
    import sys
    nums = sys.stdin.readlines()
    odds = []
    for num in nums:
        num = int(num.strip())
        if num == -1:
            break
        if num % 2:
            odds.append(num)
            
    return odds