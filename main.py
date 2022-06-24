with open("database.txt", "r") as db_file:
	DB = eval(db_file.read())


access = False

def main():
	print('OK')

def registration():
	name = input('Имя: ')
	age = input('Возраст: ')
	username = input('Логин: ')
	password = input('Пароль: ')
	DB[username] = [password, name, age]
	with open("database.txt", "w") as db_file:
		db_file.write(str(DB))
	print('Пользователь успешно зарегистрирован!')

def login():
	username = input('Введите логин: ')
	password = input('Введите пароль: ')
	if username in DB and DB[username][0] == password:
		return True

print('Добро пожаловать!')
f = int(input('Выбери действие:\n1: Регистрация\n2: Вход\n3: Выход\n>> '))
if f == 1:
	registration()
	access = True

elif f == 2:
	running = True
	while running:
		if login():
			access = True
			running = False
		else:
			print("Неверный логин или пароль\nПопробуйте ещё раз")
elif f == 3:
	exit()


if access:
	print('Доступ разрешен')
	print('OK')
	print(DB)