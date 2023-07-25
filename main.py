## -- BankAccountManager -- ##
import sqlite3 as sq
connection = sq.connect('users.db')
sql = connection.cursor()
# sql.execute('CREATE TABLE user_info (user_name TEXT, user_num TEXT, user_balance INTEGER, user_dep INTEGER);')

def user_reg(name, num):
    sql.execute(f'INSERT INTO user_info (user_name, user_num) VALUES ("{name}", "{num}");')
    connection.commit()
    print(sql.execute(f'SELECT * FROM user_info WHERE user_num="{num}";').fetchall())
def add_sum(name , sum):
    money = sql.execute(f'SELECT user_balance FROM user_info WHERE user_name="{name}";').fetchall()[0][0]
    sql.execute(f'UPDATE user_info SET user_balance={money + sum} WHERE user_name="{name}";')
    connection.commit()
def add_dep(name , sum):
    sql.execute(f'UPDATE user_info SET user_dep={sum} WHERE user_name="{name}";')
    connection.commit()
    print(sql.execute(f'SELECT user_name, user_num, user_balance FROM user_info WHERE user_name="{name}";').fetchone())
def dell_sum(name , sum):
    money = sql.execute(f'SELECT user_balance FROM user_info WHERE user_name="{name}";').fetchall()[0][0]
    sql.execute(f'UPDATE user_info SET user_balance={money - sum} WHERE user_name="{name}";')
    connection.commit()
    money = sql.execute(f'SELECT user_balance FROM user_info WHERE user_name="{name}";').fetchall()[0][0]
    print(f'С вашего баланса списали {sum}, осталось {money}')

while True:
    global_choice = int(input('1 - Регистрация <><><> 2 - Вход в аккаунт\n'))
    if global_choice == 1:
        user_name = str(input('Введите ФИО: '))
        user_num = str(input('Введите свой номер с (+): '))
        user_reg(user_name, user_num)
        print('Вы успешно зарегистрировались!')
    elif global_choice == 2:
        user_name = str(input('Введите своё ФИО: '))
        user_info = str(sql.execute('SELECT user_name FROM user_info;').fetchall())
        if user_name in user_info:
            print('Успешный вход!')
            user_choice = int(input('1 - Пополнить<><>2 - Cнять<><>3 - Депозиn\n'))
            if user_choice == 1:
                sum = int(input('Введите сумму на которую вы хотите пополнить: '))
                add_sum(user_name, sum)
            elif user_choice == 2:
                print(sql.execute(f'SELECT user_name, user_num, user_balance FROM user_info WHERE user_name="{user_name}";').fetchall())
                minus_sum = int(input('Введите сумму снятия: '))
                dell_sum(user_name, minus_sum)
            elif user_choice == 3:
                dep_choice = int(input('1 - вклад под 1%, 2 - Показ за 12, 24, 36 месяц: '))
                if dep_choice == 1:
                    money = sql.execute(f'SELECT user_balance FROM user_info WHERE user_name="{user_name}";').fetchall()[0][0]
                    dep = int(input('Введите сумму для вклада под 1%: '))
                    dell_sum(user_name, dep)
                    add_dep(user_name, dep)
                elif dep_choice == 2:
                    dep = sql.execute(f'SELECT user_dep FROM user_info WHERE user_name="{user_name}";').fetchall()[0][0]
                    print(f'За 12 месяц депозит составляет - {dep / 100 * 12}')
                    print(f'За 24 месяц депозит составляет - {dep / 100 * 24}')
                    print(f'За 36 месяц депозит составляет - {dep / 100 * 36}')
                else:
                    print('Выбирайте [1 или 2] ')
            else:
                print('Выбирайте [1 или 2 или 3]')
        else:
            print('Вы еще не зарегистрированы !')
    else:
        print('<><>Выбирайте 1 или 2<><>')

