def total_salary(path):
    salaries = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                _, salary = line.split(",") # розділяємо рядок на ім'я та зарплату
                salaries.append(int(salary))
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return 0, 0 # не буде виводити довгу системну помилку, а просто 0
    except ValueError:
        print("Файл містить некоректні дані.")
        return 0, 0

    if not salaries:
        print("Файл порожній або не містить числових значень.")
        return 0, 0

    return sum(salaries), sum(salaries) / len(salaries)

total,average = total_salary("C:\\Users\\Unrea\\Desktop\\neoversity\\test_kod\\HW_Python\\hw6\\salary_file.txt")
print(f"Загальна сума заробітної плати: {total}\nСередня заробітна плата: {average}")