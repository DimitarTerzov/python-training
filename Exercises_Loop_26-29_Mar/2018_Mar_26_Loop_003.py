text = ""
while text != "qiut":
    text = input("Please enter a chemical formula (or 'qiut' to exit): ")
    if text == "quit":
        print("...exiting program")
    elif text == "QUIT":
        print("...EXITING PROGRAM")
    elif text == "H2O":
        print("Water")
    elif text == "NH3":
        print("Ammonia")
    elif text == "CH4":
        print("Methane")
    else:
        print("Unknown compound")