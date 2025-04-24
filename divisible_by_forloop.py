v_div = int(input("Please enter a divisor for detecting no-remainder division numbers: "))
v_start = int(input("Please enter range start num: "))
v_end = int(input("Please enter range end num: "))
for v_itr in range(v_start, v_end):
    if v_itr%v_div == 0:
        print(f"{v_itr} is divisible by {v_div}")
    v_itr += 1