

from pathlib import Path


def get_cats_info(path):

    cats_list = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue

                try:
                    cat_id, name, age = line.split(",")
                except ValueError:
                    print(f"Пропущено некоректний запис (очікується id,ім'я,вік): {line.strip()}")
                    continue

                cat_id = cat_id.strip()
                name = name.strip()
                age = age.strip()

                if not cat_id or not name or not age.isdigit():
                    print(f"Пропущено некоректний запис (порожнє поле або вік не число): {line.strip()}")
                    continue

                cat_dic = {}
                cat_dic["id"] = cat_id
                cat_dic["name"] = name
                cat_dic["age"] = age
                cats_list.append(cat_dic)

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return []

    if not cats_list:
        print("Файл порожній або не містить коректних даних.")


    return cats_list

file_path = Path(__file__).parent / "cats_file.txt"
cats_info = get_cats_info(file_path)
print(cats_info)


