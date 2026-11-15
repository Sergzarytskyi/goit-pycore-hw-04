

def get_cats_info(path):
    
    cats_list = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():  
                    continue
                cat_dic = {}
                cat_id, name, age = line.split(",")
                cat_dic["id"] = cat_id
                cat_dic["name"] = name
                cat_dic["age"] = age.strip()
                cats_list.append(cat_dic)

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return []  

    if not cats_list:
        print("Файл порожній або не містить коректних даних.")
        
          
    return cats_list

cats_info = get_cats_info("hw6_2/cats_file.txt")
print(cats_info)

