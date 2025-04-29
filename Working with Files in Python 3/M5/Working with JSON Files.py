import json

def read_print_json(fn, pretty, sort):
    try:
        with open(fn, 'r') as file:
            data = json.load(file)
            if pretty:
                if sort:
                    print(json.dumps(data, indent=4, sort_keys=True))
                else:
                    print(json.dumps(data, indent=4))
            else:
                if sort:
                    print(json.dumps(data, sort_keys=True))
                else:
                    print(json.dumps(data))
    except FileNotFoundError:
        print(f"Error: The file '{fn}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{fn}' is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_print_json('./Working with Files in Python 3/files_to_read/authors.json', pretty=True, sort=True)

def update_json_file(fn, arr_name, pos, key, val):
    try:
        with open(fn, 'r') as file:
            data = json.load(file)

        if arr_name in data and isinstance(data[arr_name], list):
            if 0 <= pos < len(data[arr_name]):
                data[arr_name][pos][key] = val
            else:
                print(f"Error: Position {pos} is out of bounds for the array '{arr_name}'.")
                return
        else:
            print(f"Error: The key '{arr_name}' does not exist or is not a list in the JSON file.")
            return

        with open(fn, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Successfully updated '{key}' at position {pos} in '{arr_name}'.")

    except FileNotFoundError:
        print(f"Error: The file '{fn}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{fn}' is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

update_json_file('./Working with Files in Python 3/files_to_read/authors.json', 'authors', 1, 'courses', 10)
read_print_json('./Working with Files in Python 3/files_to_read/authors.json', pretty=True, sort=True)

