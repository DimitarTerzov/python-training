text = ""
while text.lower() != "quit":
    text = input("Please enter a chemical formula (or 'quit' to exit): ")
    if text.lower() == "quit":      # QUIT, quit, QUIt, quiT or ....
        print("...exiting program")
    elif text == "H2O":
        print("Water")
    elif text == "NH3":
        print("Amonia")
    elif text == "CH4":
        print("Methane")
    else:
        print("Unknown compound")
        
        