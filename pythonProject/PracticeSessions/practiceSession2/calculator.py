n1=int(input("enter number 1\n"))
n2=int(input("enter number 2\n"))
print(
        "enter foloowing rules\n+ for addition\n- for subtraction\n* for multiplication\n / for division\n exit for exit the program")


while True:
    inp = input()

    if (inp == "+"):
        print("answer is ", n1 + n2)
        # break
    elif (inp == "-"):
        print("answer is ", n1 - n2)
        # break
    elif (inp == "*"):
        print("answer is ", n1 * n2)
    elif (inp == "/"):
        print("answer is ", float(n1 / n2))
    elif (inp == "exit"):
        break


