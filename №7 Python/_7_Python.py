
Magazine = {
    "Bob": {
        "Тираж": "10000",
        "Ціна": "200"
        },
    "National Geographic": {
        "Тираж": "500000",
        "Ціна": "300"
        },
    "Creative": {
        "Тираж": "5000",
        "Ціна": "150"
        },
    "The day": {
        "Тираж": "8000",
        "Ціна": "120"
        },
    "The night": {
        "Тираж": "1000",
        "Ціна": "30"
        },
}

def show(Magazine): 
    for i in Magazine:
        print("Журнал: ", i, "-",  Magazine[i])

def add(Magazine, key, quantity, price):
    Magazine[key] = {
        "Тираж": quantity,
        "Ціна": price
    }
    print(f"Добавлено журнал: {key}, який має тираж {quantity} і ціну {price}")

def Del(Magazine, key):
    del Magazine[key]
    print(f"Видалено журнал: {key}")

def sort(Magazine):
    Magazine = {k: Magazine[k] for k in sorted(Magazine)}
    print("Відсортований словник: ")
    for i in Magazine:
        print("Журнал: ", i, "-",  Magazine[i])

def exercise(Magazine):
    total_price = 0
    total_quantity = 0 
    for magazine, details in Magazine.items(): 
        price = int(details["Ціна"])
        quantity = int(details["Тираж"])
        if quantity < 10000:
            total_quantity += 1
            total_price += price
    if total_quantity == 0: 
        return "Немає журналів з тиражем менше 10 000"
    else:
        return total_price / total_quantity

while True:
    print("Натисніть '1', щоб вивести асортимент журналів")
    print("Натисніть '2', щоб добавити журнал")
    print("Натисніть '3', щоб видалити журнал")
    print("Натисніть '4', щоб переглянути словник за відсортованими ключами")
    print("Натисніть '5', щоб дізнатися середню вартість журналів, тираж яких менше 10 000 примірників")
    print("Натисніть '0', щоб вийти")

    a = input("\nВаш вибір: ")

    if a == "1":
        show(Magazine)
    elif a == "2":
        key = input("Введіть назву журналу: ")
        quantity = input("Введіть тираж журналу: ")
        price = input("Введіть ціну журналу: ")
        add(Magazine, key, quantity, price)
    elif a == "3":
        key = input("Введіть назву журналу, який бажаєте видалити: ")
        Del(Magazine, key)
    elif a == "4":
        sort(Magazine)
    elif a == "5":
        print("Середня вартість:", exercise(Magazine))
    elif a == "0":
        break
    else:
        print("Некоректне введення, спробуйте знову\n")
    print("\n")
    
