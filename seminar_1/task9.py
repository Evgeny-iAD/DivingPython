# задача №9 Таблица умножения.

def formatEl(el):
    if len(str(el)) == 2:
        return f"{el}"
    else:
        return f" {el}"

def calcTab(j, i):
    return f"{j} X {formatEl(i)}= {formatEl(j * i)}"

if __name__ == '__main__':
    for i in range(2,11):
        for j in range(2,6):
            print(calcTab(j,i), end="     ")
        print(" ")
    print("\n")
    for i in range(2,11):
        for j in range(6,10):
            print(calcTab(j,i), end="     ")
        print(" ")

