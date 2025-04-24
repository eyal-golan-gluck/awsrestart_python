v_check = ""
while v_check.lower() != "exit":
    v_check = input("Please enter either a number to check parity, or just \"exit\" to quit. ")
    if v_check.isnumeric():
        v_check = int(v_check)
        print(v_check)
        v_check = str(v_check)
    else:
        if v_check.lower() == "exit":
            print("Have a nice day.")
            break