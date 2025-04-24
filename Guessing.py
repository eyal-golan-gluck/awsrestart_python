import random

v_check = ""
while v_check.lower() != "exit":
    v_check = input("Press and key to play, or \"exit\" to quit. ")
    if v_check.lower() == "exit":
         print("Have a nice day.")
         break
    else:
        v_rand = random.randint(1, 20)
        v_try = 0
        v_cnt = ""
        while not(v_cnt.isnumeric()):
            v_cnt = input("Please decide the number of guesses you have to find my secret number: ")
        v_cnt = int(v_cnt)
        while v_try < v_cnt:
            v_guess = ""
            while not(v_guess.isnumeric()):
                v_guess = input("Try now to guess our number: ")
            v_guess = int(v_guess)
            if v_guess < v_rand:
                print("Too low!")
            else:
                if v_guess > v_rand:
                    print("Too high!")
                else:
                    print("Correct! You guessed it!")
                    break
            v_try += 1
        if v_guess != v_rand:
            print(f"Game over! {v_cnt} attempts exceeded, the correct number was {v_rand}.")