def load_recipes(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break
            num_ingredients = int(f.readline().strip())
            ingredients = []
            for _ in range(num_ingredients):
                line = f.readline().strip()
                name, quantity, measure = [part.strip() for part in line.split('|')]
                ingredients.append({
                    'ingredient_name': name,
                    'quantity': float(quantity),
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
    return cook_book


def print_recipe_list(cook_book):
    print("Доступные рецепты:")
    for dish in cook_book:
        print(f"- {dish}")


def get_ingredients_for_dish(cook_book, dish_name):
    return cook_book.get(dish_name)

# Задача 2
def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        ingredients = get_ingredients_for_dish(cook_book, dish)
        if ingredients:
            for item in ingredients:
                name = item['ingredient_name']
                quantity = item['quantity'] * person_count
                measure = item['measure']
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
    return shop_list

# Задача 3
def combine_files(file_list, output_filename):
    files_info = []
    for filename in file_list:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            files_info.append((filename, len(lines), lines))
    files_info.sort(key=lambda x: x[1])

    with open(output_filename, 'w', encoding='utf-8') as out_file:
        for filename, line_count, lines in files_info:
            out_file.write(filename + '\n')
            out_file.write(str(line_count) + '\n')
            out_file.writelines(lines)

recipes_file = 'recipes.txt'
cook_book = load_recipes(recipes_file)
print_recipe_list(cook_book)

# Задача 2
dishes_to_cook = ['Запеченный картофель', 'Омлет']
persons = 2
shop_list = get_shop_list_by_dishes(cook_book, dishes_to_cook, persons)
print("\nСписок покупок:")
for ingredient, info in shop_list.items():
    print(f"{ingredient}: {info['quantity']} {info['measure']}")

# Задача 3
import glob

files = glob.glob('*.txt')

output_file = 'combined_result.txt'
combine_files(files, output_file)
print(f"Итоговый файл: {output_file}")