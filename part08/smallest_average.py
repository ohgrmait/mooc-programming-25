# Write your solution here

def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
    people = [person1, person2, person3]
    lowest_avg = ((people[0]["result1"]
                   + people[0]["result2"]
                   + people[0]["result3"]) / 3)
    lowest_avg_person_dict = people[0]
    for person in people:
        avg = ((person["result1"]
                + person["result2"]
                + person["result3"]) / 3)
        if avg < lowest_avg:
            lowest_avg = avg
            lowest_avg_person_dict = person
    return lowest_avg_person_dict

if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
    
    print(smallest_average(person1, person2, person3))
