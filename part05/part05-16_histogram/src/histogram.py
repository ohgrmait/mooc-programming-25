# Write your solution here

def histogram(string: str):
    freq = {}
    for char in string:
        if char not in freq:
            freq[char] = string.count(char)
    for key, value in freq.items():
        print(f"{key} {"*" * value}")


if __name__ == "__main__":
    histogram("statistically")
