# Write your solution here

def invert(dictionary: dict):
    for key, value in dictionary.copy().items():
        dictionary.pop(key)
        dictionary[value] = key

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
