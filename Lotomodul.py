import random, os, json

#запис даних від користувача
def record():
    pname = str(input('Введіть свій нік: '))
    filename = pname + ".txt"
    player = readrec(filename)
    panswer = None
    if player:
        print("Твої параметри: ", 'кількість чисел: ', player[1],"максимальне розігруване число: ", player[2]," кількість спроб: ",player[3])
        panswer = input("Чи хочеш змінити свої данні? (y/n)")
    if not player or panswer=="y":
        while True:
            try: 
                qnumber = int(input("Введіть розігрувану кількість чисел: "))
                maxnumber = int(input("Введіть максимальне розігруване число: "))
                if qnumber > maxnumber:
                    print("Ви ввели некоректне число, повторіть введення.")
                    continue
                if qnumber < 1 or maxnumber < 1:
                    print("Ви ввели некоректне число, повторіть введення.")
                    continue
                if qnumber == maxnumber:
                    print("Розігрувана кількість чисел не може співпадати з максимально розігрувальним числом, повторіть введення.")
                    continue
                pchance = int(input("Введіть кількість спроб: "))
                break
            except ValueError:
                print("Ви ввели некоректне число, повторіть введення: ")
                continue
    player = [pname, str(qnumber), str(maxnumber), str(pchance)]
    saverec(filename, player)  
    return player[0:1] + [int(x) for x in player[1:4]]

# читання данних користувача
def readrec(filename):
    if os.path.isfile(filename):
        file=open(filename, "r")
        line=file.readline()
        file.close()
        if line:
            return line.split(";")
    return False

# запис данних користувача
def saverec(filename, player):
    file=open(filename, "w")
    file.write(";".join(player))
    file.close()

#генерування чисел у список
def choice(qnumber,maxnumber):
    rnlist = []
    i = 0
    while i < qnumber:
        rnumber=random.randint(1,maxnumber)
        if rnlist.count(rnumber) == 0:
            rnlist.append(rnumber)
            i= i + 1
    return rnlist

#введення чисел і спроб користувачем
def pnumber(pchance,qnumber,maxnumber):
    plist = set()
    s=0
    while s < qnumber:
        try:
            savenumber = int(input("Введіть числo %s: "%(s+1)))
        except ValueError:
            print("Ви ввели некоректне число, повторіть введення: ")
            continue

        if 0 < savenumber <= maxnumber and savenumber not in plist:
                plist.add(savenumber)
                s = s + 1
    return plist
        
#результати
def result(rnlist,plist):
    correctnumber = rnlist & plist
    if correctnumber:
        print("Кількість співпадінь: %s" % len(correctnumber))
        correctnumber = ", ".join(map(str, correctnumber))
        print("Числа які співпали:%s" % correctnumber)
    else:
        print("Нажаль, Ви не вгадали. Пощастить наступного разу.")
    return len (correctnumber)

# Розігруванні числа  
def wnumber(rnlist):
    print ("Розігруванні числа:", rnlist)


    
# читання всіх данних гри
def readrecjson(filename):
    pinfo = []
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            pinfo = json.load(file)
    return pinfo

# запис всіх данних гри
def saverecjson(filename, pinfo):
    with open(filename, 'w') as file:
        json.dump(pinfo, file)
