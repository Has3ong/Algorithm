numbers = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
    100: 'hundred', 1000: 'thousand'
}

def func(n):
    if n < 100:
        if n not in numbers:
            numbers[n] = numbers[n - n % 10] + numbers[n % 10]
        return numbers[n]

    if n < 1000:
        if n % 100 == 0:
            return numbers[n // 100] + numbers[100]
        return numbers[n // 100] + numbers[100] + 'and' + numbers[n % 100]

    return 'one' + numbers[1000]


ret = 0
for i in range(1, 1001):
    value = func(i)
    ret += len(value)

print(ret)