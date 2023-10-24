cook_book = {}
with open('1512.txt', encoding='utf-8') as src_file:
    key = ''
    for line in src_file:
        line = line.strip()
        if line.isdigit():
            continue
        elif line and '|' not in line:
            cook_book[line] = []
            key = line
        elif line and '|' in line:
            name, qt, msure = line.split(" | ")
            cook_book.get(key).append(dict(ingredient_name=name, quantity=int(qt), measure=msure))


def get_shop_list_by_dishes(dishes, person_count):
    ingredients = dict()
    for dish_name in dishes:
        if dish_name in cook_book:
            for ingredient in cook_book[dish_name]:
                meas_quan_list = dict()
                if ingredient['ingredient_name'] not in ingredients:
                    meas_quan_list['measure'] = ingredient['measure']
                    meas_quan_list['quantity'] = ingredient['quantity'] * person_count
                    ingredients[ingredient['ingredient_name']] = meas_quan_list
                else:
                    ingredients[ingredient['ingredient_name']]['quantity'] = ingredients[ingredient['ingredient_name']]['quantity'] + \
                                                                     ingredient['quantity'] * person_count
        else:
            print(f'\n"Такого блюда нет в списке!"\n')

    return ingredients


if __name__ == '__main__':
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))