import pickle

class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0
        self.is_unpacking = False  # Додано атрибут is_unpacking

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] += 1
        return attributes

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.is_unpacking = True  # Позначаємо, що об'єкт розпаковувався

# Приклад використання:

# persons = Contacts("user_class.dat", contacts)
# persons.save_to_file()
# person_from_file = persons.read_from_file()
# print(persons.is_unpacking)  # False
# print(person_from_file.is_unpacking)  # True