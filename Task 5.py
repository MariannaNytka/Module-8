import pickle

class Person:
    def __init__(self, name, email, phone, favorite):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

class Contacts:
    def __init__(self, filename, contacts=None):
        self.filename = filename
        self.contacts = contacts if contacts else []
        self.count_save = 0  # Атрибут count_save за замовчуванням 0

    def save_to_file(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, 'rb') as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        state = self.__dict__.copy()  # Отримуємо поточний стан об'єкта
        state['count_save'] += 1  # Збільшуємо значення count_save на одиницю
        return state

# Створимо об'єкти Person
person1 = Person("Alice", "alice@example.com", "123-456-7890", True)
person2 = Person("Bob", "bob@example.com", "098-765-4321", False)

# Створимо об'єкт Contacts з об'єктами Person
contacts = Contacts("user_class.dat", [person1, person2])

# Збережемо об'єкт Contacts до файлу
contacts.save_to_file()

# Прочитаємо об'єкт Contacts з файлу
first = contacts.read_from_file()

# Збережемо об'єкт Contacts ще раз
first.save_to_file()

# Прочитаємо об'єкт Contacts з файлу ще раз
second = first.read_from_file()

# Збережемо об'єкт Contacts ще раз
second.save_to_file()

# Прочитаємо об'єкт Contacts з файлу ще раз
third = second.read_from_file()

# Виведемо значення атрибуту count_save
print(contacts.count_save)  # 0
print(first.count_save)  # 1
print(second.count_save)  # 2
print(third.count_save)  # 3



