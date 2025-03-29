# Write your solution here

def find_words_with_dot(search_term: str, word: str) -> bool:
    for i in range(len(word)):
        if search_term[i] != "." and word[i] != search_term[i]:
            return False
    return True

def find_words(search_term: str) -> list:
    words = []
    with open("words.txt") as file:
        for row in file:
            word = row.strip().lower()
            if "." in search_term:
                if len(search_term) == len(word):
                    if find_words_with_dot(search_term, word):
                        words.append(word)
            elif "*" in search_term:
                if search_term.index("*") == 0:
                    if word.endswith(search_term[1:]):
                        words.append(word)
                elif search_term.index("*") == len(search_term)-1:
                    if word.startswith(search_term[:-1]):
                        words.append(word)
            elif search_term == word:
                words.append(word)
    return words

if __name__ == "__main__":
    # print(find_words("*vokes"))
    # print(find_words("ca*"))
    # print(find_words("*ane"))
    print(find_words("cat"))
