from pathlib import Path


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


file_path = Path(__file__).parent / "salary_file.txt"
total,average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}\nСередня заробітна плата: {average}")
