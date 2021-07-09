
def get_data():
    cook_book = dict()

    with open("recipies.txt", "r", encoding='utf-8') as file:
        for line in file:
            menu_item = line.strip()
            ingredient_quantity = int(file.readline().strip())
            ingredient_list = []
            for item in range(ingredient_quantity):
                data_list = file.readline().strip().split(' | ')
                ingredient_list.append({'ingredient_name': data_list[0], 'quantity': data_list[1], 'meagure': data_list[2]})
                cook_book[menu_item] = ingredient_list
            x = file.readline()
    return cook_book


print(get_data())
cook_book = get_data()


def shop_list(dishes: list, number_of_person: int, cook_book):
    shopping_dict = {}
    for dish in dishes:
        ingredients_list = cook_book[dish]
        for ingredient_dict in ingredients_list:
            ingredient = ingredient_dict['ingredient_name']
            if ingredient in shopping_dict.keys():
                shopping_dict[ingredient]['quantity'] = int(ingredient_dict['quantity']) * number_of_person
            else:
                shopping_dict[ingredient] = {
                    'meagure': ingredient_dict['meagure'],
                    'quantity':int(ingredient_dict['quantity']) * number_of_person}

    return shopping_dict

print(shop_list(['Фахитос', 'Омлет'], 2, cook_book))

