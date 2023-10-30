from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

names_source = sorted(['Александра Бичан', 'Александра Крук', 'Алёна Леванхе ', 'Аля Волкова', 'Анастасия Адаменко',
                       'Анастасия Манько', 'Анастасия Синявская', 'Анастасия Солонович ', 'Ангелина Латыш',
                       'Ангелина Ярошевич', 'Анна Кононович', 'Анна Лучиц', 'Анна-Мария Савицкая', 'Анюта Труш',
                       'Аня Кевра', 'Аня Крапивенцева', 'Аполлинария Мартыненко', 'Валерия Белоус', 'Валерия Имховик',
                       'Валерия Муляр', 'Валерия Певзнер', 'Вероника Алексиевич', 'Вика Соболева', 'Виктория Кудина',
                       'Виктория Новогран', 'Виктория Татур', 'Виктория Юнцевич ', 'Виолетта Халево', 'Даниил Луцевич',
                       'Дарья Бурчик', 'Дарья Денисенко', 'Дарья Косарим', 'Дарья Липская', 'Дарья Шатило',
                       'Даша Гальковская', 'Даша Дрик', 'Даша Ёлкина', 'Даша Кадовб', 'Дарья Маршалкина',
                       'Диана Виршич', 'Диана Разуева', 'Екатерина Мироненко', 'Екатерина Супрон',
                       'Елизавета Бойко', 'Елизавета Рейман', 'Злата Позняк', 'Илья Лепёха', 'Ирина Лемнёва ',
                       'Каролина Рубаник', 'Катя Азовцева', 'Кристина Гулякевич', 'Ксения Хвасько', 'Ксюша Будилович',
                       'Ксюша Витковская', 'Ксюша Жогальская', 'Ксюша Харченко', 'Лиза Валялкина', 'Лиза Матияс',
                       'Лиза Сацук', 'Лолита Иванова', 'Максим Пилат', 'Мария Денисевич', 'Мария Пахоменко',
                       'Матвей Давыдов', 'Маша Цибульская', 'Настя Дерех', 'Наташа Басалай', 'Полина Авдеева',
                       'Полина Бочарова', 'Полина Ключенович', 'Полина Коваль', 'Полина Масейко', 'Полина Пашкова',
                       'Полина Столярчук', 'Полина Хлань', 'Роман Горченок', 'Саша Золотухо ', 'Соня Баранова',
                       'Станислав Никончук', 'Таня Авгесова', 'Таня Заболотникова', 'Таня Макаренко', 'Ульяна Горовец',
                       'Ульяна Дубовик', 'Ульяна Миськевич', 'Юлия Зварыч', 'Яна Кисель', 'Яна Смольская',
                       'Ярослав Никулин', 'Andrey Kanash', 'Ilyha Tsuprik ', 'Katsiaryna Sabaliuk'])

options = webdriver.ChromeOptions()
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari'
    '/537.36')
driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver.exe", options=options)

driver.implicitly_wait(20)

driver.get("https://vk.com/login")

username = driver.find_element(By.ID, "index_email")
username.send_keys("+111111111")
button_login = driver.find_element(By.CLASS_NAME, "FlatButton__in")
time.sleep(1)
button_login.click()

driver.implicitly_wait(20)
password = driver.find_element(By.NAME, 'password')
time.sleep(2)
driver.implicitly_wait(20)
try:
    password.clear()
    password.send_keys("1111111111")
    password.send_keys(Keys.RETURN)
except selenium.common.exceptions.StaleElementReferenceException:
    password = driver.find_element(By.NAME, 'password')
    password.clear()
    password.send_keys("11111111")
    password.send_keys(Keys.RETURN)

driver.implicitly_wait(30)
post_url = "https://vk.com/club218025223"
driver.get(post_url)

button_open_post = driver.find_element(By.XPATH, "//a[contains(@class, 'PostHeaderSubtitle__link')]")
button_open_post.click()

post = driver.find_element(By.XPATH, "//div[contains(@id, 'wk_content')]")
comments = post.find_elements(By.XPATH, ".//div[contains(@class,'reply_content')]")
driver.execute_script("arguments[0].scrollIntoView();", comments[-1])
comments = post.find_elements(By.XPATH, ".//div[contains(@class,'reply_content')]")

names = []
for i in range(len(comments)):
    a = comments[i].text
    name = comments[i].text.split("\n")
    if ("сегодня" in a or "вчера" in a or "назад" in a or len(name) == 1) and (
            "ответила" not in a or "ответил" not in a):
        names.append(name[0])

names = sorted(list(set(names)))

names_check = []
for i in names:
    names_check.append(i.lower())

driver.get('https://onlinetestpad.com/ru/account/login?ReturnUrl=/')  # get the login link

email_input = driver.find_element("id", "txtEmail")
email_input.clear()
email_input.send_keys("sofiyasiarheyeva@gmail.com")  # login

password_input = driver.find_element("id", "txtPassword")
password_input.clear()
time.sleep(2)
password_input.send_keys("SofiaTest987654321")  # password
password_input.send_keys(Keys.ENTER)
link = input()
driver.get(link)

get_all_data_button = driver.find_element(By.XPATH,
                                          "//select[contains(@class, 'form-control form-control-sm pull-left ng-untouched ng-pristine ng-valid')]")
get_all_data_button.click()

get_100_button = get_all_data_button.find_element(By.XPATH,
                                                  '//*[@id="dpagemain"]/div[2]/div[2]/div[2]/div/test-selector/test-statistics-container/test-statistics/test-stat-table/div/stat-table/div[1]/div/div[1]/div[1]/table/tbody/tr/td[1]/select/option[5]')
get_100_button.click()

names_otp = driver.find_element(By.XPATH,
                                '//*[@id="dpagemain"]/div[2]/div[2]/div[2]/div/test-selector/test-statistics-container/test-statistics/test-stat-table/div/stat-table/div[1]/div/div[1]/div[2]/table')

names_otp_text = (names_otp.text.split('\n'))
name_grade = {}
dict_check = []
counter_dict = 0
for i in names_otp_text:
    i = i.split(' ')
    if (i[1].lower() + ' ' + i[2].lower() in names_check) or (i[2].lower() + ' ' + i[1].lower() in names_check):
        qw = i[2].title() + ' ' + i[1].title()
        if qw in names:
            name_grade[qw] = int(float((i[-1])))
            dict_check.append(qw)
        else:
            qw = i[1].title() + ' ' + i[2].title()
            name_grade[qw] = int(float((i[-1])))
            dict_check.append(qw)
        counter_dict += 1
name_grade_list = []

for i in name_grade.items():
    name_grade_list.append(i)

name_grade_list = sorted(list(set(name_grade_list)), key=lambda x: x[0])

print(*name_grade_list, sep='\n')

names_source_dict = {}

name_grade_list = sorted(list(set(name_grade_list)), key=lambda x: x[0])

print(len(name_grade_list))
for i in names:
    if i not in dict_check:
        print(i.upper())

print(len(names))

driver.get("https://vk.com/login")

try:
    username = driver.find_element(By.ID, "index_email")
    username.send_keys("+375445854947")
    button_login = driver.find_element(By.CLASS_NAME, "FlatButton__in")
    time.sleep(1)
    button_login.click()

    driver.implicitly_wait(20)
    password = driver.find_element(By.NAME, 'password')
    time.sleep(2)
    driver.implicitly_wait(20)
    try:
        password.clear()
        password.send_keys("recrecrec15K")
        password.send_keys(Keys.RETURN)
    except selenium.common.exceptions.StaleElementReferenceException:
        password = driver.find_element(By.NAME, 'password')
        password.clear()
        password.send_keys("recrecrec15K")
        password.send_keys(Keys.RETURN)
except:
    pass

driver.implicitly_wait(30)
post_url = "https://vk.com/club218025223"
driver.get(post_url)

button_open_post = driver.find_element(By.XPATH, "//a[contains(@class, 'PostHeaderSubtitle__link')]")
button_open_post.click()

post = driver.find_element(By.XPATH, "//div[contains(@id, 'wk_content')]")
comments_for_likes = post.find_elements(By.XPATH,
                                        ".//div[contains(@class,'reply_wrap _reply_content _post_content clear_fix')]")
for i in comments_for_likes:
    for j in dict_check:
        if j in i.text:
            i.click()
            like_button = i.find_element(By.XPATH, ".//div[contains(@class, 'like_button_icon')]")
            like_button.click()
            pass

driver.quit()
