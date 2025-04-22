code1 = input("Please enter a letters-only string: ")
code2 = input("Please enter a letters-only string: ")
code3 = input("Please enter a letters-only string: ")
numA = input("Please enter a digits-only string: ")
numB = input("Please enter a digits-only string: ")
if code1.isalpha() and code2.isalpha() and code3.isalpha():
    v_combined = code1.lower()+"-"+code2.lower()+"-"+code3.lower()
    v_reversal = code1.lower()+code2.lower()+code3.lower()
else:
    print("Invalid codeword")
    exit
if numA.isnumeric() and numB.isnumeric():
    numA=int(numA)
    numB=int(numB)
    numA += numB
    numB = numA-numB
    numA -= numB
else:
    print("Invalid numbers")
    exit
print(f"Secret code: {v_combined}")
print(f"Secret Number: {(numA*numB) - numA + numB}")
print(f"Swapped Values: A={numA}, B={numB}")
print(f"Average of Originals: {(numA+numB)/2}")
print(f"Combined Length: {len(v_combined)}")
# Line of code below will use 2 python features:
# slice functionality, for reading a string in reverse, the [::-1] operator
# and comparison for implicitly returning a boolean value into a variable
v_palindrome = code1.lower()+code2.lower()+code3.lower() == v_reversal[::-1]
print(f"Palindrome: {v_palindrome}")