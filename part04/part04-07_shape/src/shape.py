# Copy here code of line function from previous exercise and use it in your solution

def line(integer, string):
    if string == "":
        print("*" * integer)
    else:
        print(string[0] * integer)

def shape(size1, char1, size2, char2):
    i = 0
    while i < size1:
        line(i + 1, char1)
        i += 1
    j = 0
    while j < size2:
        line(size1, char2)
        j += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")