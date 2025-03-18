# Write your solution here

def list_of_stars(integers: list):
    for integer in integers:
        print("*" * integer)

if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])
