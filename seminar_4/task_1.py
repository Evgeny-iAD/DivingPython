# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». Напишите функцию, которая при запуске
# заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) на None. Значения не удаляются,
# а помещаются в одноимённые переменные без s на конце."""

def replace_variables():
    # Создание переменных
    variable1s = 10
    variable2s = "Hello"
    variables = [variable1s, variable2s]
    s = "World"

    # Замена содержимого переменных
    updated_vars = {}
    for var_name, var_value in locals().items():
        if var_name.endswith("s") and var_name != "s" and len(var_name) > 1:
            var_without_s = var_name[:-1]
            updated_vars[var_without_s] = var_value
            locals()[var_name] = None

    # Обновление словаря locals()
    locals().update(updated_vars)


    print(variable1)  # Вывод: 10
    print(variable2)  # Вывод: Hello
    print(variables)  # Вывод: [10, 'Hello']
    print(s)          # Вывод: World


replace_variables()



