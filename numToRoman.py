s = int(input("s: "))

translation = {
    "1": "I",
    "5": "V",
    "10": "X",
    "50": "L",
    "100": "C",
    "500": "D",
    "1000": "M"
}

lista_s = list(map(int, str(s)))
wiekszy = []
mniejszy = []

for key, value in translation.items():
    if s > int(key):
        print("wiekszy od: ", key)
        wiekszy.append(key)
    else:
        print("mniejszy od: ", key)
        mniejszy.append(key)


print("pomiedzy: ", wiekszy[-1], mniejszy[0])