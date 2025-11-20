for num in range(1, 1001):
    digits = str(num)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    if num == total:
        print(num)