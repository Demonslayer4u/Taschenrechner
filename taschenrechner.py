def start():
  print("Taschenrechner")
  rechnen()
  
def menu():
  exityn = input("exit? (y/n): ")
  if exityn == "y":
    exit()
  elif exityn == "n":
    rechnen()
  else:
    menu()
    
  

def rechnen():
    rechnung = input("Geben Sie eine Rechnung ein (z.B. 2+3): ")
    ergebnis = eval(rechnung)
    print("Das Ergebnis ist:", ergebnis)
        
rechnen()