def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
        inner_function()   #вызов функции inner_function внутри функции test_function результатов не дал
test_function()

try:
    inner_function()
except NameError as e:
    print("Ошибка: функция inner_function не может быть вызвана вне test_function.")
