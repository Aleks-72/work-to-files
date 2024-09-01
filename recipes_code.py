from  pprint import pprint
import os

# Запись книги рецептов из файла в словарь
with open('recipes.txt', 'r', encoding='UTF-8', newline="") as f:
    lines = f.readlines()
    cook_book = {}
    ingredients = []
    position_name = 1
    position_quantity = 2
    position_ingredients = 3
    position = 1
    for line in lines:
        line = line.strip()
        if line == '':
            continue
        elif position == position_name:
            name = line
            position = position_quantity
        elif position == position_quantity:
            quantity_inrgedients = int(line)
            position = position_ingredients
        elif position == position_ingredients:
            if quantity_inrgedients > 1:
                ingredients.append(line)
                quantity_inrgedients -= 1
            elif quantity_inrgedients == 1:
                ingredients.append(line)
                cook_book[name] = [{'ingredient_name':ingredient[0:ingredient.find('|')].strip(),'quantity':ingredient[ingredient.find('|')+1:ingredient.rfind('|')].strip(), 'measure':ingredient[ingredient.rfind('|')+1:].strip()} for ingredient in ingredients]
                ingredients = []
                position = position_name
            else:
                print(f"Ошибка при составлении рецепта {name}")
        else:
            print("Ошибка при чтении Книги рецептов")

# Создание списка покупок:
def get_shop_list_by_dishes(dishes: list, person_count: int):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            recipe = cook_book[dish]
        else:
            print(f'В книге рецептов отсутствует блюдо {dish}. Ингридиенты данного блюда не будут добавлены в список покупок.')
        for ingredient in recipe:
            if ingredient['ingredient_name'] in shop_list:
                quantity_inrgedients  = shop_list[ingredient['ingredient_name']]['quantity'] + (int(ingredient['quantity'])*person_count)
                shop_list[ingredient['ingredient_name']] = {'measure':ingredient['measure'], 'quantity':quantity_inrgedients}
            else:
                shop_list[ingredient['ingredient_name']] = {'measure':ingredient['measure'], 'quantity':int(ingredient['quantity'])*person_count}
    pprint(shop_list)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Паста'], 2)

# Работа с файлами
path = 'files'
files = ['1.txt', '2.txt', '3.txt'] # если файлы известны
files = os.listdir(path) # если имена файлов неизвестны, в данном случае без разницы использовать готовый список или воспользоваться данной функцией
result_file = []
for file in files: 
    path_file = path+'\\'+file
    with open(path_file, 'r', encoding='UTF-8', newline="") as f:
        text_file = f.readlines()
        dict_file = {}
        dict_file['file_name'] = file.strip()
        dict_file['file_text'] = text_file
        dict_file['file_lenght'] = len(text_file)
        result_file.append(dict_file)
result_file.sort(key=lambda e: e['file_lenght'])

with open('result_file.txt', 'w', encoding='UTF-8', newline="") as f:
    for record in result_file:
        f.write(record['file_name'] + '\n')
        f.write(str(record['file_lenght']) + '\n')
        for line in record['file_text']:
            f.write(line.strip('\n') + '\n')
