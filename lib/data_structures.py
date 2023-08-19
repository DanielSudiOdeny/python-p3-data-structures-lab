spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    spicy_foods = [f["name"] for f in spicy_foods]
    return spicy_foods


print(get_names(spicy_foods))


def get_spiciest_foods(spicy_foods):
    spiciest_foods = [f for f in spicy_foods if f["heat_level"] > 5]
    return spiciest_foods


print(get_spiciest_foods(spicy_foods))


def print_spicy_foods(spicy_foods):
    spicy_foods = [
        f"{f['name']} ({f['cuisine']}) | Heat Level: {'🌶' * f['heat_level']}" for f in spicy_foods]
    for f in spicy_foods:
        print(f)


print(print_spicy_foods(spicy_foods))


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for f in spicy_foods:
        if (f["cuisine"] == cuisine):
            return f


print(get_spicy_food_by_cuisine(spicy_foods, "American"))


def print_spiciest_foods(spicy_foods):
    spiciest_foods = [
        f"{f['name']} ({f['cuisine']}) | Heat Level: {'🌶' * f['heat_level']}" for f in spicy_foods if f['heat_level'] > 5]

    for f in spiciest_foods:
        print(f)


print(print_spiciest_foods(spicy_foods))


def get_average_heat_level(spicy_foods):
    sum_heat = 0
    len_foods = len(spicy_foods)

    for f in spicy_foods:
        sum_heat += f["heat_level"]
        average_heat = sum_heat / len_foods
    return int(average_heat)


print(get_average_heat_level(spicy_foods))


def create_spicy_food(spicy_foods, spicy_food):
    updated_spicy_foods = spicy_foods.copy()
    updated_spicy_foods.append(spicy_food)
    return updated_spicy_foods


new_spicy_food = {"name": "Spicy_chicken",
                  "cuisine": "Kenyan",
                  "heat_level": 5,
                  }
print(create_spicy_food(spicy_foods, new_spicy_food))
