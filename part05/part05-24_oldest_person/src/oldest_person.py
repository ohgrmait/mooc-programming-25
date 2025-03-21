# Write your solution here

def oldest_person(people: list) -> str:
    oldest_age = people[0][1]
    oldest_person = people[0][0]
    for person in people:
        if person[1] < oldest_age:
            oldest_age = person[1]
            oldest_person = person[0]
    return oldest_person

if __name__ == "__main__":
    people_list = [
        ('Emily', 2014), ('Arthur', 1977), ('Ernest', 1985),
        ('Mary', 1953), ('Ellen', 1997)
    ]
    result = oldest_person(people_list)
    print(result)
    # p1 = ("Adam", 1977)
    # p2 = ("Ellen", 1985)
    # p3 = ("Mary", 1953)
    # p4 = ("Ernest", 1997)
    # people = [p1, p2, p3, p4]

    # print(oldest_person(people))
