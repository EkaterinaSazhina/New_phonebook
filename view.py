import text


def main_menu() -> int:
    print(text.main_menu)
    return get_choice()

def get_choice() -> int:
    while True:
        choice = input(text.enter_number)
        if choice.isdigit() and 0 <= int(choice) <= len(text.main_menu) - 1:
            return int(choice)
        print(f'Введите пункт меню от 0 до {len(text.main_menu) - 1}')


def print_message(message: str):
    print('\n' + '~' * len(message))
    print(message)
    print('~' * len(message) + '\n')

def show_contacts(p_book: dict[int,list[str]], error_message: str):
    max_size = list(map(lambda x: len(max(x, key=len)), list(zip(*p_book.values()))))
    if p_book:
        print('\n' + '~' * (sum(max_size) + 7))
        for n, contact in p_book.items():
            print(f'{n:>3}, {contact[0]:<{max_size[0]}} {contact[1]:<{max_size[1]}} {contact[2]:<{max_size[2]}} {contact[3]:<{max_size[3]}}')
        print('~' * (sum(max_size) + 7) + '\n')
    else:
        print_message(error_message)


def find_contact():
    search_field, search_value = view.search_parameters()
    found_contacts = model.search_contact(search_field, search_value)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        view.print_contacts(found_contacts)


def add_contact(message: list[str], contact: list[str] = None):
    contact = contact if contact else ['', '', '','']
    for n, mes in enumerate(message):
        field = input(mes)
        contact[n] = field if field else contact[n]
    return contact

def input_data(message: str) -> str:
    return input(message)


def change_contact_flow():
    name_to_search = view.input_data("Введите имя контакта для изменения: ")
    found_contacts = model.find_contacts_by_name(name_to_search)

    if not found_contacts:
        view.print_message("Контакт не найден!")
    else:
        view.print_message("Найдены следующие контакты:")
        for contact in found_contacts:
            view.show_contact_info(contact)

        choice = view.input_data('Введите ID контакта, который хотите изменить: ')
        if choice.isdigit() and int(choice) in model.phone_book:
            c_contact = view.add_contact(text.new_contact, model.phone_book[int(choice)])
            model.change_contact(int(choice), c_contact)
            view.print_message(text.contact_action_successful("changed", c_contact[0]))
        else:
            view.print_message("Введенный ID контакта не существует!")


