
ans = None


def start():
    print("Taschenrechner")
    berechne()



def berechne():

    #variabeln definieren
    A = None
    B = None
    global ans

    #zahlen&op abfragen
    a = input()
    op = input()
    b = input()


    #zahl oder text erkennung&umwandlung a
    try:
        a = int(a)
        A = a
    except ValueError:
        a = str(a)
        if a == "ans":
            try:
                A = ans
            except NameError:
                print("ans noch nicht belegt")
                start()

        else:
            print("Syntax-Error")
            start()

    #zahl oder text erkennung&umwandlung b
    try:
        b = int(b)
        B = b
    except ValueError:
        b = str(b)
        if b == "ans":
            try:
                B = ans
            except NameError:
                print("ans noch nicht belegt")
                start()

        else:
            print("Syntax-Error")
            start()

    #rechnung durch erkennung d rechenzeichens
    if op == '+':
        ergebnis = A + B
    elif op == '-':
        ergebnis = A - B
    elif op == '*':
        ergebnis = A * B
    elif op == '/':
        #teilung d 0
        if B == 0:
            print("Math-Error")
            start()
        else:
            ergebnis = A / B

    else:
        print("Syntax-Error")
        start()


    #ans wird gespeichert
    ans = ergebnis

    #ergebnis wird ausgegeben
    print("Ergebnis:", ergebnis)
    


start()

#test


