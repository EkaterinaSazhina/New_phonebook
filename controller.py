import text
import view
import model

def find_contact():
    word = view.input_data(text.input_search_word)
    result = model.find_contact(word)
    view.show_contacts(result, text.contacts_not_found(word))

def contact_not_found_choice() -> bool:
    while True:
        choice = view.input_data(text.choice_word)
        if choice == '1':
            return True
        elif choice == '0':
            return False
        else:
            view.print_message("Некорректный выбор. Пожалуйста, повторите попытку.")

def find_contact_flow():
    while True:
        word = view.input_data(text.input_search_word)
        result = model.find_contact(word)
        if result:
            view.show_contacts(result, text.contact_not_found)
            break
        else:
            view.print_message(text.contact_not_found)
            if not contact_not_found_choice():
                break

def start_app():
    while True:
        choice = view.main_menu()
        if choice == 0:
            view.print_message(text.good_bay)
            break
        elif choice == 1:
            model.open_file()
            view.print_message(text.load_successful)
            view.print_message(text.main_menu)
        elif choice == 2:
            pb = model.phone_book
            view.show_contacts(pb, text.empty_phone_book)
        elif choice == 3:
            contact = view.add_contact(text.new_contact)
            model.new_contact(contact)
            view.print_message(text.contact_action_successful("added", contact[0]))
        elif choice == 4:
            find_contact()
        elif choice == 5:
            find_contact_flow()
            choice_to_change = view.input_data(text.input_id_change_contact)
            if choice_to_change.isdigit():
                c_id = int(choice_to_change)
                if c_id in model.phone_book:
                    c_contact = view.add_contact(text.new_contact, model.phone_book[c_id])
                    model.change_contact(c_id, c_contact)
                    view.print_message(text.contact_action_successful("changed", c_contact[0]))
                else:
                    view.print_message(text.contact_not_found)
            else:
                view.print_message("Некорректный ID контакта!")
        elif choice == 6:
            find_contact()
            c_id = int(view.input_data(text.input_id_delete_contact))
            name = model.delete_contact(c_id)[0]
            view.print_message(text.contact_action_successful("deleted", name))
        elif choice == 7:
            model.save_file()
            view.print_message(text.save_successful)
