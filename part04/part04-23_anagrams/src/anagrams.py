# Write your solution here

def anagrams(string1: str, string2: str) -> bool:
    return sorted(list(string1)) == sorted(list(string2))

if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False
