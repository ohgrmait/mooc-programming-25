# Write your solution here

def new_person(name: str, age: int) -> tuple:
    if name == "":
        raise ValueError(f"The name was an empty string: {name}")
    if " " not in name or len(name) > 40:
        raise ValueError(f"The name is too short or too long: {name}")
    if age < 0 or age > 150:
        raise ValueError(f"The age is a negative number or too big: {age}")
    return (name, age)
