import sys
from pathlib import Path
from colorama import Fore, Style, init

init()  

COLOR_BLUE = Fore.BLUE
COLOR_RED = Fore.RED
COLOR_RESET = Style.RESET_ALL


def display_direction(path: Path, indent: str = " ", prefix: str = " ") -> None:
    if path.is_dir():

        print(indent + prefix + COLOR_BLUE + str(path.name) + COLOR_RESET)

        try:
            children = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
        except PermissionError:
            print(indent + "      └── " + COLOR_RED + "[немає доступу]" + COLOR_RESET)
            return

        for index, child in enumerate(children):

            is_last = index == len(children) - 1
            
            display_direction(child, indent + "    ", "  └── " if is_last else "  ├── ")
    else:
        print(indent + prefix + str(path.name))


if __name__ == "__main__":
   
    if len(sys.argv) > 1:
        sours = Path(sys.argv[1])
    else:
        sours = Path("picture")

   
    if not sours.exists():
        print(COLOR_RED + f"Помилка: шлях '{sours}' не існує" + COLOR_RESET)
    elif not sours.is_dir():
        print(COLOR_RED + f"Помилка: '{sours}' — це не директорія" + COLOR_RESET)
    else:
        display_direction(sours.resolve())  
