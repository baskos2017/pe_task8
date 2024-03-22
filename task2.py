import json

try:
    with open('links.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    data = []

while True:
    select = input('1 - Додати посилання\n2 - Отримати посилання по назві\n3 Вихід\n')
    if select == '1':
        link = input('Введіть посилання:\n')
        description = input('Введіть назву:\n')
        links_dict = {
            'link': link,
            'description': description
        }
        data.append(links_dict)
        with open('links.json', 'w') as f:
            json.dump(data, f, indent=4)
    elif select == "2":
        description = input('Введіть назву:\n')
        found = False
        for item in data:
            if item['description'] == description:
                print(f"Знайдено посилання: {item['link']}")
                found = True
                break
        if not found:
            print('Посилання з такою назвою не знайдено.')
    elif select == '3':
        break

