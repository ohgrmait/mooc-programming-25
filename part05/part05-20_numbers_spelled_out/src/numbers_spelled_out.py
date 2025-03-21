# Write your solution here

def dict_of_numbers() -> dict:
    numbers = {}
    ones = [
        "zero", "one", "two", "three",
        "four", "five", "six", "seven",
        "eight", "nine"
    ]
    tens = [
        "ten", "twenty", "thirty",
        "forty", "fifty", "sixty",
        "seventy", "eighty", "ninety"
    ]
    elevens = [
        "eleven", "twelve", "thirteen",
        "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"
    ]
    for i in range(100):
        if i >= 0 and i <= 9:
            numbers[i] = ones[i]
        elif i >= 11 and i <= 19:
            numbers[i] = elevens[i-11]
        elif i >= 21 and i <= 29:
            numbers[i] = f"{tens[1]}-{ones[i-20]}"
        elif i >= 31 and i <= 39:
            numbers[i] = f"{tens[2]}-{ones[i-30]}"
        elif i >= 41 and i <= 49:
            numbers[i] = f"{tens[3]}-{ones[i-40]}"
        elif i >= 51 and i <= 59:
            numbers[i] = f"{tens[4]}-{ones[i-50]}"
        elif i >= 61 and i <= 69:
            numbers[i] = f"{tens[5]}-{ones[i-60]}"
        elif i >= 71 and i <= 79:
            numbers[i] = f"{tens[6]}-{ones[i-70]}"
        elif i >= 81 and i <= 89:
            numbers[i] = f"{tens[7]}-{ones[i-80]}"
        elif i >= 91 and i <= 99:
            numbers[i] = f"{tens[8]}-{ones[i-90]}"
        elif i % 10 == 0:
            numbers[i] = tens[i//10-1]
    return numbers

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
