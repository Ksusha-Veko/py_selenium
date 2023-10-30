import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 1 - configure ChromeDriver options
options = webdriver.ChromeOptions()
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 '
    'Safari/537.36')
driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver.exe", options=options)
driver.implicitly_wait(20)

try:
    # 2 - get the main menu link
    driver.get('https://onlinetestpad.com/ru/account/login?ReturnUrl=/')

    # 3 - find email input field, clear it, and send email keys
    email_input = driver.find_element("id", "txtEmail")
    email_input.clear()
    email_input.send_keys("EXAMPLE@gmail.com")

    driver.implicitly_wait(5)

    # 4 - find password input field, clear it, and send password keys
    password_input = driver.find_element("id", "txtPassword")
    password_input.clear()
    password_input.send_keys("password")

    # 5 - click ENTER and finish logging in
    password_input.send_keys(Keys.ENTER)

    # 6 - navigating through the site to find the questions folder
    profile_button = driver.find_element("xpath", "//a[contains(@class,'navbar-avatar')]//i[@class='icon-arrowdown']")
    profile_button.click()
    profile_button.click()

    test_button = driver.find_element("xpath",
                                      "//a[contains(@href,'https://app.onlinetestpad.com/tests')]")
    test_button.click()
    driver.implicitly_wait(5)

    folder_sort_menu_button = driver.find_element("xpath",
                                                  "//td[contains(@class,'filter-view')]//span[@class='dropdown-toggle']"
                                                  )
    folder_sort_menu_button.click()
    driver.implicitly_wait(5)
    folder_sort_button = driver.find_element("xpath",
                                             "/html/body/app-root/basic/div[1]/div[3]/div[2]/div[2]/div["
                                             "2]/div/tests-list/div[1]/otp-service-items/div[1]/table/tbody/tr/td["
                                             "1]/div/div/a[3]")
    folder_sort_button.click()

    exact_folder_button = driver.find_element("xpath",
                                              "/html/body/app-root/basic/div[1]/div[3]/div[2]/div[2]/div["
                                              "2]/div/tests-list/div[1]/otp-service-items/div["
                                              "2]/otp-service-items-folders/div[1]/div/ul/li["
                                              "8]/otp-service-items-folders-item/a/span[1]/i")
    exact_folder_button.click()

    # 7 - getting the exact test link in the tests folder
    exact_test_link = driver.find_element("xpath", "//a[contains(@href, '/tests/ka74zl66eegi2')]")
    exact_test_link.click()

    # 8 - parsing the questions
    exact_test_questions = driver.find_element("xpath", "/html/body/app-root/basic/div[1]/div[3]/div[2]/div[2]/div["
                                                        "2]/div/test-selector/test-dashboard/div/div[1]/div[1]/div["
                                                        "1]/div[3]/a")
    exact_test_questions.click()

    # 9 - parsing questions of A-type (tests with multiple options), ordering, and sorting them
    questions_A = driver.find_elements("xpath", "//span[contains(@class,'qtext')]")

    question_names_A = []
    for i in questions_A:
        question_names_A.append(i.text)

    question_options_A = driver.find_elements("xpath", "//div[contains(@class,'item otp-row-1')]")
    question_options_text_A = []
    for i in question_options_A:
        if len(i.text.strip().split()) != 0:
            question_options_text_A.append(i.text)
    # 10 - parsing questions of B1-type (questions with short answer), ordering, and sorting them
    questions_B1 = driver.find_elements("xpath", "//div[contains(@class,'lst1')]")
    question_options_text_B1 = []
    for i in questions_B1:
        if len(i.text.strip().split()) != 0:
            question_options_text_B1.append(i.text.strip("\n \n1 \n2 \n3 \n4").split("1"))
    for i in range(len(question_options_text_B1)):
        for j in range(len(question_options_text_B1[i])):
            question_options_text_B1[i][j] = question_options_text_B1[i][j].strip("1 2 3 \n4 6 7 8 9 0 5")

    # 11 - parsing answers of B1-type (questions with short answer) and sorting them
    questions_B2 = driver.find_elements("xpath", "//div[contains(@class,'lst2')]")
    question_options_text_B2 = []
    for i in questions_B2:
        if len(i.text.strip().split()) != 0:
            question_options_text_B2.append(i.text.strip("\n  '\n2' '\n3' '\n4' '\n2\n3\n4'").split("\n"))
    for i in range(len(question_options_text_B2)):
        for j in range(len(question_options_text_B2[i])):
            if len(question_options_text_B2[i][j]) > 2:
                question_options_text_B2[i][j] = question_options_text_B2[i][j].strip("\n '\n\n\n'")

    # 12 - printing sorted A-type questions
    k = 0
    for i in range(len(question_names_A)):
        print(i + 1)
        print(question_names_A[i])
        print(*question_options_text_A[k:k + 5], sep='\n')
        print()
        print("Не подходит:")
        k += 5
        print()

    # 13 - printing sorted B-type questions and their answers
    B_questions_answers = (list(zip(question_options_text_B1, question_options_text_B2)))
    for i in B_questions_answers:
        for j in i:
            for k in j:
                if len(k) > 2:
                    print(k)
            print()
        print()

# 14 - handling any exceptions
except Exception as ex:
    print(ex)
# 15 - closing the driver
finally:
    driver.close()
    driver.quit()