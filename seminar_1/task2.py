
if __name__ == '__main__':
    input_str = input("Введите стороны треугольника a, b и c, разделенные пробелами: ")
    a, b, c = input_str.split()
    sideList = [int(a), int(b), int(c)]
    result = None
    for i in range(3):
        bufferList = sideList[:]
        bufferEl = bufferList.pop(i)
        if bufferEl > sum(bufferList):
            result = f"Треугольник со сторонами {a, b, c} не существует"
            break
        elif bufferEl == sum(bufferList)/2:
            result = f"Треугольник со сторонами {a, b, c} равносторонний"
            break
        elif bufferList[0] == bufferList[1]:
            result = f"Треугольник со сторонами {a, b, c} равнобедренный"
            break
    if result == None:
        print(f"Треугольник разносторонний!")
    else:
        print(result)



