# Write your solution here

def first_word(sentence):
    return sentence[:sentence.find(" ")]

def second_word(sentence):
    if sentence.find(" ", sentence.find(" ")+1) == -1:
        return sentence[sentence.find(" ")+1:]
    return sentence[sentence.find(" ")+1: sentence.find(" ", sentence.find(" ")+1)]

def last_word(sentence):
    string = ""
    index = len(sentence) - 1
    while index >= 0:
        if sentence[index] == " ":
            break
        string = sentence[index] + string
        index -= 1
    return string

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
    print(second_word("first second"))
