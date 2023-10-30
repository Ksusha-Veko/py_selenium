from sys import stdin


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(password):
    if len(password) < 9:
        raise LengthError
    elif not (any(i.isalpha() and i.upper() == i for i in password)) or not (
            any(i.isalpha() and i.lower() == i for i in password)):
        raise LetterError
    elif not any(i.isdigit() for i in password):
        raise DigitError
    return "Success!"


for i in stdin:
    try:
        print(is_good_password(i.strip()))
        break
    except Exception as e:
        print(str(type(e)).split(".")[-1].rstrip("> ' \n"))


"""Назовем пароль хорошим, если

    его длина равна 99 или более символам
    в нем присутствуют большие и маленькие буквы любого алфавита
    в нем имеется хотя бы одна цифра

Напишите программу, которая требует ввода нового пароля до тех пор, пока не будет введен хороший.

Формат входных данных
На вход программе подается произвольное количество паролей, каждый на отдельной строке. Гарантируется, что среди них присутствует хороший.

Формат выходных данных
Для каждого введенного пароля программа должна вывести текст:

    LengthError, если длина введенного пароля меньше 99 символов
    LetterError, если в нем все буквы имеют одинаковый регистр либо отсутствуют
    DigitError, если в нем нет ни одной цифры
    Success!, если введенный пароль хороший

После ввода хорошего пароля все последующие пароли должны игнорироваться."""