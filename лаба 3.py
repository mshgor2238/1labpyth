import sys
import timeit

# === Задание 01 ===
items_list = ["Кабель", "Мышь", "Клавиатура", "Монитор", "Ноутбук", "Принтер"]
items_tuple = ("Кабель", "Мышь", "Клавиатура", "Монитор", "Ноутбук", "Принтер")
print(items_list, type(items_list), id(items_list))
items_list = "Веб-камера"
print(items_list, id(items_list))
print(items_tuple, type(items_tuple), id(items_tuple))
new_items_tuple = ("Кабель", "Веб-камера", "Клавиатура", "Монитор", "Ноутбук", "Принтер")
print(new_items_tuple, id(new_items_tuple))

# === Задание 02 ===
raw_articles = [
    "A-100", "A-132", "A-100", "A-154", "A-181",
    "A-132", "A-200", "A-215", "A-181", "A-300", "A-100", "A-215"
]
unique_articles = set(raw_articles)
print(len(raw_articles), raw_articles)
print(len(unique_articles), unique_articles)

# === Задание 03 ===
for size in [1_000, 10_000, 100_000]:
    test_list = list(range(size))
    test_set = set(range(size))
    t_list_in = timeit.timeit(lambda: (size - 1) in test_list, number=10_000)
    t_set_in = timeit.timeit(lambda: (size - 1) in test_set, number=10_000)
    t_list_out = timeit.timeit(lambda: -1 in test_list, number=10_000)
    t_set_out = timeit.timeit(lambda: -1 in test_set, number=10_000)
    print(size, round(t_list_in, 6), round(t_set_in, 6), round(t_list_out, 6), round(t_set_out, 6))

# === Задание 04 ===
products_dict = {
    "A-100": "Кабель USB-C",
    "A-132": "Клавиатура",
    "A-154": "Монитор",
    "A-181": "Мышь беспроводная",
    "A-200": "Ноутбук",
    "A-215": "Принтер"
}
print(products_dict["A-154"])
sample_data = [f"item_{i}" for i in range(100)]
print(sys.getsizeof(list(sample_data)))
print(sys.getsizeof(tuple(sample_data)))
print(sys.getsizeof(set(sample_data)))
print(sys.getsizeof({k: i for i, k in enumerate(sample_data)}))

# === Итоговое задание (Вариант 4) ===
warehouse_info = ("Северный", "ул. Заводская, 8", "20.10.2026")
deliveries = ["P-41", "P-42", "P-43", "P-44", "P-45", "P-46"]
accepted_articles = {"A-100", "A-132", "A-154", "A-181", "A-200", "A-215"}
catalog = {
    "A-100": "Кабель USB-C",
    "A-132": "Клавиатура",
    "A-154": "Монитор",
    "A-181": "Мышь беспроводная",
    "A-200": "Ноутбук",
    "A-215": "Принтер"
}

print(f"Склад: «{warehouse_info}», {warehouse_info}, инвентаризация {warehouse_info}")
print("Поставки в порядке поступления:", ", ".join(deliveries))
print("Принятые артикулы:", ", ".join(sorted(accepted_articles)))
print("Товары:", "; ".join(f"{k} - «{v}»" for k, v in catalog.items()))

deliveries.append("P-47")
print("После добавления поставки:", ", ".join(deliveries))
print("Товар с артикулом A-154 принят:", "да" if "A-154" in accepted_articles else "нет")
print(f"Название товара A-132: «{catalog['A-132']}»")
