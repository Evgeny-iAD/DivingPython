"""Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
 где ключ — значение переданного аргумента, а значение — имя аргумента.
  Если ключ не хешируем, используйте его строковое представление."""

def create_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        key_str = str(key) if hashable(key) else repr(key)
        result[key_str] = value
    return result

def hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

if __name__ == '__main__':
    params_dict = create_dict(a=10, b='hello', c=[1, 2, 3])
    print(params_dict)

