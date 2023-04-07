def read_txt():
    with open('book.txt', 'r', encoding='utf-8') as f:
        return f.read()


def show_data() -> None:
    # with open('book.txt', 'r', encoding='utf-8') as f:
        print(read_txt())


def add_date() -> None:
    fio = input('Введите ФИО: ')
    tel_number = input('Введите телефон: ')
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'{fio} || {tel_number}\n')
    print('Успешно!')

def find_date():
    data = input('Введите данные для поиска: ')
    with open('book.txt', 'r', encoding='utf=8') as f:
        tel_book = f.read()
    print(serch(tel_book, data))
        
def serch(book: str, info: str) -> str:
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])

def editing():
    text = read_txt().split('\n')
    print(f'{list(enumerate(text))}')
    choice = int(input('Выберите строку которую хотите изменить: '))
    fio1 = input('Введите ФИО: ')
    tel_number1 = input('Введите телефон: ')
    text[choice] = f'{fio1} || {tel_number1}'
    print(text)
    with open('book.txt', 'w', encoding='utf=8') as f:
        f.writelines( text[i]+'\n' for i in range(len(text)))
        print('Документ успешно изменен')


def del_elem():
    text = read_txt().split('\n')
    print(f'{list(enumerate(text))}')
    choice = int(input('Выберите строку которую хотите удалить: '))
    text.pop(choice)
    with open('book.txt', 'w', encoding='utf=8') as f:
        f.writelines(text[i]+'\n' for i in range(len(text)))
        print('Документ успешно изменен')


while True:
    print('1.Вывод 2.Добавление 3.Поиск 4.Изменить 5.Удалить 0.Выход')
    mode = input()
    if mode == '1':
        show_data()
    elif mode == '2':
        add_date()
    elif mode == '3':
        find_date()
    elif mode == '4':
        editing()
    elif mode == '5':
        del_elem()
    elif mode == '0':
        break
    else:
        print('Не коректный ввод, попробуйте еще раз!')
    