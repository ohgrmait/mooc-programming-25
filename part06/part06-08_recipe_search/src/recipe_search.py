# Write your solution here

def get_recipe_data(filename: str) -> list:
    # Return all aspects of the file in a list
    recipe_data = []
    with open(filename) as new_file:
        for row in new_file:
            recipe_data.append(row.strip())
    recipe_data.insert(0, "")
    return recipe_data

def get_recipe_list(filename: str) -> list:
    # Return all aspects of the recipe data in a dict
    recipes = []
    recipe_data = get_recipe_data(filename)
    i = 0
    while i < len(recipe_data):
        recipe = {}
        if recipe_data[i] == "":
            recipe["name"] = recipe_data[i+1]
            recipe["prep_time"] = int(recipe_data[i+2])
            ingredients = []
            recipes.append(recipe)
            i += 3
        else:
            ingredients.append(recipe_data[i])
            i += 1
        recipe["ingredients"] = ingredients
    return recipes

def search_by_name(filename: str, word: str) -> list:
    # Search for recipes based on the name of the recipe
    recipes = get_recipe_list(filename)
    des_recipes = []
    for recipe in recipes:
        if word.lower() in recipe["name"].lower():
            des_recipes.append(recipe["name"])
    return des_recipes

def search_by_time(filename: str, prep_time: int) -> list:
    # Search for recipes based on the preparation time
    recipes = get_recipe_list(filename)
    des_recipes = []
    for recipe in recipes:
        if prep_time >= recipe["prep_time"]:
            des_recipes.append(f"{recipe["name"]}, preparation time {recipe["prep_time"]} min")
    return des_recipes

def search_by_ingredient(filename: str, ingredient: str) -> list:
    # Search for recipes based on the ingredients
    recipes = get_recipe_list(filename)
    des_recipes = []
    for recipe in recipes:
        if ingredient in recipe["ingredients"]:
            des_recipes.append(f"{recipe["name"]}, preparation time {recipe["prep_time"]} min")
    return des_recipes

if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in found_recipes:
        print(recipe)
