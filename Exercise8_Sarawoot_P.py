usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "yoyky" and passwordInput == "0113":
    print("----- Welcome -----")
    print("----- Yoyky Shop -----")
    print("1.Snack 20 (THB) : ")
    print("2.Sparkling Water 15 (THB) : ")
    userSelect = int(input(">>>"))
    if userSelect == 1:
        numberInput = int(input("How Many : "))
        price = 20
        print(numberInput * price, "THB")
    elif userSelect == 2:
        numberInput = int(input("How Many : "))
        price = 15
        print(numberInput * price, "THB")
