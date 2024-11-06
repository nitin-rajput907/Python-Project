def average(*number):
    sum = 0
    for i in number:
        sum = sum +i
        print("the average is: ",sum / len(number))



average (2, 3, 5, 6,  2)