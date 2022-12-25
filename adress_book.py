from collections import UserDict





class Field:
    pass

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

class Name(Field):
    def __init__(self, name):
        self.name = name

class Record:
    def __init__(self, name: Name, *phones):
        self.name = name
        self.phones = list(phones)

    def add_phone(self, phone_number: Phone):
        self.phones.append(phone_number)

    def change_phone(self, phone_number_old: Phone, phone_number_new: Phone):
        self.phones.remove(phone_number_old)
        self.phones.append(phone_number_new)

    def del_phone(self, phone_number: Phone):
        self.phones.remove(phone_number)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.name] = record


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    phone1 = Phone('0987654321')
    rec = Record(name, phone)
    rec.add_phone(phone1)
    print(type(rec.phones))
    ab = AddressBook()
    print(ab.data)
    ab.add_record(rec)
    print(ab[name.name].phones)
    

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].phone == '1234567890'

    print('All Ok)')

p = Name
p.name = 'Bob'
print(f'My name {p.name}')
