first = int(input())
second = int(input())
third = int(input())

if first == second == third:
    print(3)
elif first != second == third:
    print(2)
else:
    print(0)
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

while True:
    for number in my_list:
        if number > 0:
            print(number)
        elif number < 0:
            print('stop')
        else:
            break


def get_matrix(n, m, v):
    matrix = []
    for i in range(n):
       row = []
    for j in range(m):
        row.append(v)
        matrix.append(row)
    return matrix


m = get_matrix(2, 2, 10)
print(m)

call = 0


def count_calls():
    global call
    call += 1


def string_info(word: str):
    size = len(word)
    up = word.upper()
    low = word.lower()
    count_calls()
    return size, up, low


def is_contains(name: str, name_list: list):
    if name in name_list:
        count_calls()
        return True
    else:
        count_calls()
        return False


print(string_info('test'))
print(is_contains('urban', ['URNAN', 'urban']))
print(call)


def send_email(messages, recipient, sender="university.help@gmail.com"):
    found = ['@', '.com', '.ru']
    if recipient and sender in found:
        print(f'Письмо успешно отправлено с адреса {sender} на {recipient} с сообщением {messages}')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif recipient != recipient:
        print('Нестандартный отправитель')
    else:
        print('-')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Это сообщение для проверки связи', 'urban.teacher@mail.ru')
