main_menu = ('Меню: \n1 - Открыть файл\n2 - Показать контакты\n3 - Создать контакт\n4 - Найти контакт\n\
5 - Изменить контакт\n6 - Удалить контакт\n7 - Сохранить файл\n0 - Выйти из приложения\n')

enter_number = ('Выберите пункт меню или нажмите 0 для выхода: ')

good_bay = 'До свидания!'

empty_phone_book = 'Телефонная книга пуста или не открыта!'
new_contact = ['Введите имя или Enter для пропуска: ',
               'Введите фамилию Enter для пропуска: ',
               'Введите номер телефона Enter для пропуска: ',
               'Введите комментарий Enter для пропуска: ']

input_search_word = 'Введите символы или цифры для поиска контакта: '

contact_not_found = 'Контакты не найдены'
def contacts_not_found(word: str) -> str:
    return f'Контакты содержащие {word} не найдены!'

input_id_change_contact = 'Введите ID контакта, который хотите изменить или ENTER для выхода в  главное меню: '

choice_word = "Введите '1' для ввода корректных данных или '0' для выхода в меню: "
def contact_action_successful(action: str, name: str) -> str:
    if action == "added":
        return f'Контакт {name} успешно добавлен!'
    elif action == "changed":
        return f'Контакт {name} успешно изменен!'
    elif action == "deleted":
        return f'Контакт {name} успешно удален!'

input_id_delete_contact = 'Введите ID контакта, который хотите удалить: '
load_successful = 'Телефонная книга успешно загружена!'
save_successful = 'Телефонная книга успешно сохранена!'