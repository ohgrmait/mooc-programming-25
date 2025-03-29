# Write your solution here

def filter_solutions():
    with open("solutions.csv") as file:
        open("correct.csv", "w").close()
        open("incorrect.csv", "w").close()
        for row in file:
            parts = row.split(";")
            if eval(parts[1]) == int(parts[2]):
                with open("correct.csv", "a") as correct_file:
                    correct_file.write(row)
            else:
                with open("incorrect.csv", "a") as incorrect_file:
                    incorrect_file.write(row)
    
if __name__ == "__main__":
    filter_solutions()
