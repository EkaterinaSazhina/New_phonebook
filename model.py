phone_book = {}
path = 'phonebook.txt'
SEPARATOR = ' '

def open_file():
    global phone_book
    with open(path, 'r', encoding='UTF-8') as file:
        phone_book = {i: item for i, item in
                      enumerate(list(map(lambda x: x.strip().split(SEPARATOR), file.readlines())), 1)}


def next_id():
    global phone_book
    return (max(phone_book) + 1) if phone_book else 1

def search_contact(search_field: str, search_value: str) -> list[dict]:
    found_contacts = []
    for contact in phone_book:
        if contact[search_field].lower().find(search_value.lower()) != -1:
            found_contacts.append(contact)
    return found_contacts

def new_contact(contact: list[str]):
    global phone_book
    phone_book[next_id()] = contact

def find_contact(word: str) -> dict[int, list[str]]:
    global phone_book
    result = {}
    for u_id, contact in phone_book.items():
        if word.lower() in str(contact).lower():
            result[u_id] = contact
    return result

def change_contact(contact_id, new_contact):
    if contact_id in phone_book:
        phone_book[contact_id] = new_contact
        with open(path, 'w', encoding='utf-8') as file:
            for contact in phone_book.values():
                file.write(' '.join(contact) + '\n')
    else:
        view.print_message("Contact not found")

def find_contacts_by_name(name):
    found_contacts = [contact for contact in phone_book.values() if contact['name'] == name]
    return found_contacts

def delete_contact(c_id: int) -> list[str]:
    global phone_book
    return phone_book.pop(c_id)


def save_file():
    global phone_book
    data = []
    for contact in phone_book.values():
        data.append(SEPARATOR.join(contact))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)
