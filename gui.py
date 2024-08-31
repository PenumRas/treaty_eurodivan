import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from logic import create_document
from guarantee import create_guarantee

def on_save():
    try:
        number_dogovoru = entry_number_dogovoru.get()
        name_buyer = entry_name_buyer.get()
        item_for_buy = entry_item_for_buy.get()
        adress = entry_adress.get()
        phone = entry_phone.get()
        vidstan_dostavku = distance_var.get()
        description = entry_description.get("1.0", tk.END).strip()
        quantity = int(quantity_var.get())
        price = float(entry_price.get())
        avans = float(entry_avans.get())
        manufacturer = manufacturer_var.get()

        if not all([number_dogovoru, name_buyer, item_for_buy, adress, phone, description, quantity, price, avans, manufacturer]):
            messagebox.showerror("Помилка", "Будь ласка, заповніть всі поля.")
            return

        vidstan_dostavku = 0 if vidstan_dostavku == "Київ" else 1

        # Визначення шляху для збереження файлів
        base_path = r"E:\Робота Гугл Диск\.shortcut-targets-by-id\0BwGxeScX7t3cdEZCcTh3UmMzSDQ\клиенты\Выписанные договора без предоплаты"
        folder_name = f'{number_dogovoru}_{name_buyer}_{item_for_buy}'
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Створення основного документа
        create_document(number_dogovoru, name_buyer, item_for_buy, adress, phone, vidstan_dostavku, description, quantity, price, avans, folder_path)

        # Створення додаткових файлів на основі вибору користувача
        if check_guarantee.get():
            create_guarantee(number_dogovoru, description, manufacturer, folder_path)

        messagebox.showinfo("Успіх", "Документ(и) успішно створено.")
    except ValueError as e:
        messagebox.showerror("Помилка", f"Невірний формат даних: {e}")
    except Exception as e:
        messagebox.showerror("Помилка", f"Сталася помилка: {e}")

# Створення GUI
root = tk.Tk()
root.title("Створення документа")

# Додавання полів вводу
labels = ['Номер договору', 'Ім’я покупця', 'Найменування товару', 'Адреса', 'Телефон', 'Доставка', 'Опис', 'Кількість', 'Ціна', 'Аванс']
entries = []

for i, text in enumerate(labels):
    tk.Label(root, text=text).grid(row=i, column=0, padx=10, pady=5, sticky="e")

# Введення даних
entry_number_dogovoru = tk.Entry(root)
entry_number_dogovoru.grid(row=0, column=1, padx=10, pady=5, sticky="w")

entry_name_buyer = tk.Entry(root)
entry_name_buyer.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Введення даних та виробника
entry_item_for_buy = tk.Entry(root)
entry_item_for_buy.grid(row=2, column=1, padx=10, pady=5, sticky="w")

manufacturer_var = tk.StringVar()
manufacturer_options = ["РИЧ", "Комфорто", "Анкер", "Амерс", "Фаворіс"]
manufacturer_menu = ttk.Combobox(root, textvariable=manufacturer_var, values=manufacturer_options)
manufacturer_menu.grid(row=2, column=2, padx=10, pady=5, sticky="w")
manufacturer_menu.set(manufacturer_options[0])  # Встановити значення за замовчуванням

entry_adress = tk.Entry(root)
entry_adress.grid(row=3, column=1, padx=10, pady=5, sticky="w")

entry_phone = tk.Entry(root)
entry_phone.grid(row=4, column=1, padx=10, pady=5, sticky="w")

# Випадковий список для "Відстань"
distance_var = tk.StringVar()
distance_options = ["Київ", "Україна"]
distance_menu = ttk.Combobox(root, textvariable=distance_var, values=distance_options)
distance_menu.grid(row=5, column=1, padx=10, pady=5, sticky="w")
distance_menu.set("Київ")

# Велике текстове поле для опису
entry_description = scrolledtext.ScrolledText(root, width=40, height=10)
entry_description.grid(row=6, column=1, padx=10, pady=5, sticky="w")

# Випадковий список для "Кількість"
quantity_var = tk.IntVar()
quantity_options = [i for i in range(1, 11)]
quantity_menu = ttk.Combobox(root, textvariable=quantity_var, values=quantity_options)
quantity_menu.grid(row=7, column=1, padx=10, pady=5, sticky="w")
quantity_menu.set(1)

entry_price = tk.Entry(root)
entry_price.grid(row=8, column=1, padx=10, pady=5, sticky="w")

entry_avans = tk.Entry(root)
entry_avans.grid(row=9, column=1, padx=10, pady=5, sticky="w")

# Чекбокси для створення додаткових документів
check_guarantee = tk.BooleanVar()
tk.Checkbutton(root, text="Гарантія", variable=check_guarantee).grid(row=10, column=0, padx=10, pady=5, sticky="w")

# Інші чекбокси можна додати за потреби

# Кнопка збереження
btn_save = tk.Button(root, text="Зберегти", command=on_save)
btn_save.grid(row=11, column=1, pady=10, sticky="e")

root.mainloop()
