import json
import os


def get_data_from_json(file_name: str):
    ext = ".json"
    encoding = "utf-8"
    read_mode = "r"
    path_file = os.path.join(current_path, file_name + ext)

    with open(path_file, read_mode, encoding=encoding) as file:
        data = json.load(file)

    return data


def create_enumerated_list_from_dict(data: dict):
    return [f"{i}. {name.capitalize()}" for i, name in enumerate(data, start=1)]


def print_menu(selections: str) -> None:
    print(
        f"""
Coffee Machine.

{selections}
"""
    )


current_path = os.getcwd()
coins_data = get_data_from_json("coins")
cookbook_data = get_data_from_json("cookbook")
resources_data = get_data_from_json("resources")
secret_word = "off"
coffee_selection = "\n".join(create_enumerated_list_from_dict(cookbook_data))

while True:
    print_menu(coffee_selection)
    user_selection = input("Selection: ")

    if user_selection.lower() == secret_word:
        break
