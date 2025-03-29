# Write your solution here

def week_info_valid(week_info: str) -> bool:
    week_no = week_info.split(" ")[1]
    try:
        if isinstance(int(week_no), int):
            return True
    except:
        return False

def lottery_info_valid(lottery_info: str) -> bool:
    lotteries = lottery_info.split(",")
    if len(lotteries) != 7:
        return False
    try:
        for lottery in lotteries:
            if not isinstance(int(lottery), int):
                return False
            if int(lottery) < 1 or int(lottery) > 39:
                return False
            if lotteries.count(lottery) > 1:
                return False
        return True
    except:
        return False

def filter_incorrect():
    with open("lottery_numbers.csv") as lottery_numbers, open("correct_numbers.csv", "w") as correct_numbers:
        for row in lottery_numbers:
            row = row.replace("\n", "")
            parts = row.split(";")
            week_info = parts[0]
            lottery_info = parts[1]
            if week_info_valid(week_info) and lottery_info_valid(lottery_info):
                correct_numbers.write(f"{row}\n")

if __name__ == "__main__":
    filter_incorrect()
