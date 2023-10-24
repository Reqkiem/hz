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


print(cook_book)