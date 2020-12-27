from collections import defaultdict


def parse_recipes(lines):
    all_ingredients = set()
    all_allergens = set()
    recipe_to_allergens = dict()
    ingredient_to_possible_allergens = defaultdict(set)
    for recipe in lines:
        ingredients_r, allergens_r = recipe.split(' (contains ')
        ingredients = set(ingredients_r.split())
        allergens = set(allergens_r[:-1].split(', '))
        all_ingredients |= ingredients
        all_allergens |= allergens
        recipe_to_allergens[tuple(ingredients)] = allergens
        for ingredient in ingredients:
            ingredient_to_possible_allergens[ingredient] |= allergens
    return all_allergens, all_ingredients, ingredient_to_possible_allergens, recipe_to_allergens


def part1(all_allergens, all_ingredients, recipe_to_allergens):
    ingredient_to_non_possibles = {i: set() for i in all_ingredients}
    seen_ingredients = defaultdict(int)

    for ingredients, allergens in recipe_to_allergens.items():
        ingredients = set(ingredients)
        for i in ingredients:
            seen_ingredients[i] += 1
        for other_ingredient in all_ingredients - ingredients:
            ingredient_to_non_possibles[other_ingredient] |= allergens

    ans = 0
    for i in ingredient_to_non_possibles:
        if ingredient_to_non_possibles[i] == all_allergens:
            ans += seen_ingredients[i]
    print('part1', ans)

    return ingredient_to_non_possibles


def part2(ingredient_to_possible_allergens, ingredient_to_non_possibles):
    taken_allergens = set()
    while True:
        stop = True
        for ingredient, possible_allergens in ingredient_to_possible_allergens.items():
            ingredient_to_possible_allergens[ingredient] -= ingredient_to_non_possibles[ingredient]
            if len(ingredient_to_possible_allergens[ingredient]) == 1:
                taken_allergens |= ingredient_to_possible_allergens[ingredient]
            elif len(ingredient_to_possible_allergens[ingredient]) > 1:
                ingredient_to_possible_allergens[ingredient] -= taken_allergens
                stop = False

        if stop:
            break
    dangerous_list = [
        (ingredient, list(allergens)[0])
        for ingredient, allergens in ingredient_to_possible_allergens.items()
        if len(allergens) == 1
    ]
    dangerous_list = sorted(dangerous_list, key=lambda tup: tup[1])
    ans = ','.join([i for (i, _) in dangerous_list])
    print('part2', ans)


def day21():
    lines = [line.strip() for line in open('input.txt')]

    all_allergens, all_ingredients, ingredient_to_possible_allergens, recipe_to_allergens = parse_recipes(lines)
    ingredients_to_non_possibles = part1(all_allergens, all_ingredients, recipe_to_allergens)
    part2(ingredient_to_possible_allergens, ingredients_to_non_possibles)


if __name__ == '__main__':
    day21()
