# Write your solution here

def factorials(n: int) -> dict:
    my_dict = {}
    for i in range(1, n+1):
        fact = 1
        num = i
        while num > 0:
            fact *= num
            num -= 1
        my_dict[i] = fact
    return my_dict

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
