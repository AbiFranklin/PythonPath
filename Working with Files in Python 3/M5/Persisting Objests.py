import pickle

class Person:
    age = 45
    name = "John Doe"
    kids = ["Jane", "Doe"]
    employers = {'AWS' : 2022, 'Google' : 2023}
    shoe_sizes = (8.5, 9.0, 9.5)

def serialize(obj):
    pickled = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"Serialized object: {pickled}")
    return pickled

def deserialize(pickled_obj):
    try:
        obj = pickle.loads(pickled_obj)
        print(f"Deserialized object: {obj}")
        return obj
    except Exception as e:
        print(f"An error occurred during deserialization: {e}")
        return None
    
def deserialize_employers(pickled_obj):
    try:
        obj = pickle.loads(pickled_obj)
        if isinstance(obj, Person) and hasattr(obj, 'employers'):
            print(f"Deserialized employers: {obj.employers}")
            return obj.employers
        else:
            print("The deserialized object does not have the 'employers' attribute.")
            return None
    except Exception as e:
        print(f"An error occurred during deserialization: {e}")
        return None
    
def obj_to_file(obj, filename):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(obj, file, protocol=pickle.HIGHEST_PROTOCOL)
        print(f"Object successfully serialized and saved to '{filename}'.")
    except Exception as e:
        print(f"An error occurred while saving the object: {e}")

def file_to_obj(filename):
    try:
        with open(filename, 'rb') as file:
            obj = pickle.load(file)
        print(f"Object successfully deserialized from '{filename}'.")
        print(obj)
        return obj
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except pickle.UnpicklingError:
        print(f"Error: The file '{filename}' is not a valid pickle file.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    

serialize(Person())
deserialize(serialize(Person()))
deserialize_employers(serialize(Person()))

obj_to_file(Person(), './Working with Files in Python 3/files/person.pkl')
file_to_obj('./Working with Files in Python 3/files/person.pkl')