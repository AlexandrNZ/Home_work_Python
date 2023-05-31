phone_book: list[dict[str,str]] = []
path = 'Урок 9. Работа с табличными данными\phone.txt'

def open_pb():
    global phone_book, path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        phone_book.append({'name':contact[0], 'phone':contact[1], 'comment':contact[2]})
   
   
   
def save_pb():
    global phone_book, path
    data = []
    for contact in phone_book:
        contact = ':'.join([value for value in contact.values()])
        data.append(contact)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join (data))
     
   
def get_pd() -> list[dict[str,str]]:
    global phone_book
    return phone_book


def add_contact(contact: dict[str, str]):
    global phone_book
    phone_book.append(contact)
    return contact.get('name')



def del_contact(index: int):
    return phone_book.pop(index-1).get('name')


    