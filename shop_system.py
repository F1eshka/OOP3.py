import os

FILE_NAME = "orders.txt"


def load_orders():
    """Читает файл и возвращает список словарей (заказов)."""
    orders = []
    if not os.path.exists(FILE_NAME):
        return orders
    
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 4:
                orders.append({
                    "id": parts[0],
                    "name": parts[1],
                    "qty": parts[2],
                    "price": parts[3]
                })
    return orders

def save_orders(orders):
    """Перезаписывает файл обновленным списком заказов."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for o in orders:
            f.write(f"{o['id']}|{o['name']}|{o['qty']}|{o['price']}\n")


def add_order():
    orders = load_orders()
    print("\n--- Добавление заказа ---")
    oid = input("Введите номер заказа (ID): ")
    
    for o in orders:
        if o['id'] == oid:
            print("Ошибка: Заказ с таким номером уже существует!")
            return

    name = input("Название товара: ")
    qty = input("Количество: ")
    price = input("Цена: ")
    
    orders.append({"id": oid, "name": name, "qty": qty, "price": price})
    save_orders(orders)
    print("Заказ добавлен.")

def view_orders():
    orders = load_orders()
    print("\n--- Список заказов ---")
    if not orders:
        print("Список пуст.")
    else:
        print(f"{'ID':<10} {'Товар':<20} {'Кол-во':<10} {'Цена':<10}")
        print("-" * 50)
        for o in orders:
            print(f"{o['id']:<10} {o['name']:<20} {o['qty']:<10} {o['price']:<10}")

def find_order():
    oid = input("\nВведите ID для поиска: ")
    orders = load_orders()
    found = False
    for o in orders:
        if o['id'] == oid:
            print(f"Найден: {o['name']} - {o['qty']} шт. по {o['price']} грн")
            found = True
            break
    if not found:
        print("Заказ не найден.")

def update_order():
    oid = input("\nВведите ID заказа для обновления: ")
    orders = load_orders()
    found = False
    for o in orders:
        if o['id'] == oid:
            print(f"Текущие данные: {o['name']} (Кол-во: {o['qty']}, Цена: {o['price']})")
            o['qty'] = input("Новое количество: ")
            o['price'] = input("Новая цена: ")
            found = True
            break
    
    if found:
        save_orders(orders)
        print("Данные обновлены.")
    else:
        print("Заказ не найден.")

def delete_order():
    oid = input("\nВведите ID заказа для удаления: ")
    orders = load_orders()
    new_orders = [o for o in orders if o['id'] != oid]
    
    if len(new_orders) < len(orders):
        save_orders(new_orders)
        print("Заказ удален.")
    else:
        print("Заказ не найден.")

def main():
    while True:
        print("\n=== УПРАВЛЕНИЕ ЗАКАЗАМИ ===")
        print("1. Добавить заказ")
        print("2. Просмотреть все")
        print("3. Найти по номеру")
        print("4. Обновить заказ")
        print("5. Удалить заказ")
        print("6. Выход")
        
        choice = input("Ваш выбор: ")
        
        if choice == '1': add_order()
        elif choice == '2': view_orders()
        elif choice == '3': find_order()
        elif choice == '4': update_order()
        elif choice == '5': delete_order()
        elif choice == '6': break
        else: print("Неверный ввод!")

if __name__ == "__main__":
    main()