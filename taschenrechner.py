ans = None
syntaxerror = 0
matherror = 0
a = None
b = None
op = None
A = None
B = None
ergebnis = None


def start():
    global syntaxerror
    global matherror
    syntaxerror = 0
    matherror = 0
    print("Taschenrechner")
    abfrage()


def menu():
    global syntaxerror
    global matherror
    syntaxerror = 0
    matherror = 0

    #menu
    menuyn = input("Exit? (y/n)")
    if menuyn == "y":
        exit()
    elif menuyn == "n":
        abfrage()
    else:
        menu()

def abfrage():
    global a
    global b
    global ergebnis
    global op
    global ans

    a = None
    b = None


    # zahlen&op abfragen
    a = input("Erste Zahl:")
    op = input("Rechenzeichen (+ - * / =):")
    #print(op)
    if op == "=":
        umwandeln()
    else:
        b = input("Zweite Zahl:")
        umwandeln()



def umwandeln():
    global ans
    global syntaxerror
    global a
    global b
    global op
    global A
    global B
    global ergebnis

    A = None
    B = None



    # zahl oder text erkennung&umwandlung a
    try:
        a = float(a)
        A = a
        print("A changed successful ...")
        if op == "=":
            ergebnis = A
            ans = A
            ergebnisausgabe()
    except ValueError:
        a = str(a)
        print("A changed successful ...")
        if a == "ans":
            A = ans
            if op == "=":
                ergebnis = A
                ans = A
                ergebnisausgabe()
        else:
            syntaxerror = 1
            ergebnisausgabe()



    # zahl oder text erkennung&umwandlung b
    try:
        b = float(b)
        B = b
        print("B changed successful ...")
        rechnen()
    except ValueError:
        b = str(b)
        if b == "ans":
            B = ans
            print("B changed successful ...")
            rechnen()
        else:
            syntaxerror = 1
            ergebnisausgabe()




def rechnen():
    global ans
    global syntaxerror
    global matherror
    global a
    global b
    global op
    global A
    global B
    global ergebnis

    # rechnung durch erkennung d rechenzeichens
    try:
        op = str(op)

        if op == "+":
            ergebnis = A + B
        elif op == "-":
            ergebnis = A - B
        elif op == "*":
            ergebnis = A * B
        elif op == "/":
            # teilung d 0
            if B == 0:
                matherror = 1
                ergebnisausgabe()
            else:
                ergebnis = A / B
                ergebnisausgabe()
        else:
            syntaxerror = 1
            ergebnisausgabe()

        ergebnisausgabe()

    except ValueError:
        syntaxerror = 1
        ergebnisausgabe()


def ergebnisausgabe():
    global ergebnis
    global syntaxerror
    global matherror
    global ans

    # ans wird gespeichert
    ans = ergebnis
    print("ans changed successful ...")

    if ergebnis == None:
        syntaxerror = 1


    if syntaxerror == 0 and matherror == 0:
        if B == None:
            print("Ergebnis(", A, ")=", ergebnis)
        else:
            print("Ergebnis(", A, op, B,")=", ergebnis)
    elif syntaxerror == 1 and matherror == 0:
        print("Syntax-Error")
    elif syntaxerror == 0 and matherror == 1:
        print("Math-Error")
    elif syntaxerror == 1 and matherror == 1:
        print("Syntax-Error & Math-Error")

    menu()

start()