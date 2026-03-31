import json
import os


def get_data_from_json(file_name: str):
    ext = ".json"
    encoding = "utf-8"
    read_mode = "r"
    current_path = os.getcwd()
    path_file = os.path.join(current_path, file_name + ext)

    with open(path_file, read_mode, encoding=encoding) as file:
        data = json.load(file)

    return data


def create_enumerated_list_from_dict(data: dict):
    return [f"{i}. {name.capitalize()}" for i, name in enumerate(data, start=1)]

def verify_machine_capacity(cData: dict, resources_data: dict):

    ingredients = cData["ingredients"]

    for key in ingredients:
        if resources_data[key] < ingredients[key]:
            print(f"out of {key} please refill it\n")
            input("Press enter to continue: ")
            return False
    return True
    
    
    

def coffeeProcess(selection: str, cookbook_data: dict, resources_data: dict) -> None:
    clear_screen()
    
    coffeeData = cookbook_data[selection]
    
    if not verify_machine_capacity(coffeeData, resources_data):
        return

def clear_screen() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        print("\033[2J\033[H", end="")

def print_menu(selections: str) -> None:
    print(
        f"""
Coffee Machine.

{selections}
"""
    )


coins_data = get_data_from_json("coins")
cookbook_data = get_data_from_json("cookbook")
resources_data = get_data_from_json("resources")
menu_selections = get_data_from_json("selections")

secret_word = "off"
coffee_selection = "\n".join(create_enumerated_list_from_dict(cookbook_data))

while True:
    print_menu(coffee_selection)
    user_selection = input("Selection: ")

    if user_selection.lower() == secret_word:
        break

    try: 
        coffeeProcess(menu_selections[user_selection], cookbook_data, resources_data)
    except KeyError:
        clear_screen()
        print("Invalid Selection")
