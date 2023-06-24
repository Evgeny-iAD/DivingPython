"""2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов."""

def format_things_print(things):
    result = ''
    for i, element in enumerate(things):
        result += f" {element}"
        result += ",\n" if (i % 5 == 0) and (i != 0) else ", "
    return result[:-2]

if __name__ == '__main__':
    input_data = ['test', '555', 'test', 'TTT', 'test', '555', 'O', 'test',
                  'test', 'OL', 'test', '555', 'test', 'TTT', 'test', 'GG',]

    buffer = []
    result = []
    for element in input_data:
        if not element in buffer:
            buffer.append(element)
    for el in buffer:
        input_data.remove(el)
        is_present = el in input_data
        if is_present != False: result.append(el)
    print(f"Дублирующиеся элементы: {format_things_print(result)}")






