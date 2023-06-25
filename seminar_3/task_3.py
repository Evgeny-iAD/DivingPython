"""3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10
самых частых. Не учитывать знаки препинания
и регистр символов. За основу возьмите любую статью из википедии или из документации к языку."""


def calc_word(processed_list):
    buffer = []
    result = {}
    max_key_value = {}
    for element in processed_list:
        if not element in buffer:
            buffer.append(element)
    for el in buffer:
        count = processed_list.count(el)
        result[el]=count
    for i in range(10):
        key_max_value = max(result, key=result.get)
        max_key_value[key_max_value]=result.pop(key_max_value)
    return max_key_value

if __name__ == '__main__':
    with open("text.txt", "r", encoding="utf-8") as file:
        content = file.read()

    data_list = [word.strip() for word in content.split(" ")]
    processed_list = [word.replace(",", "").replace(".", "").replace("«", "").replace("»", "").replace("—", "") for word in data_list]
    processed_list = [word for word in processed_list if word != ""]

    calc_w = calc_word(processed_list)
    print(f"Наиболее популярные 10 слов в тексте:")
    for element in calc_w:
        print(f"    '{element}' повторяется {calc_w[element]} раз")
