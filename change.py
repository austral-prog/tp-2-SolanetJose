def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("\n" +"Vuelto")
    print("\n" +"Pesos:")
    exact=(money-expense)
    pesos=int(exact)
    print(pesos)
    print("Centavos:")
    centavos=(exact-pesos)
    print(int(centavos*100))
