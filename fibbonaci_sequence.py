def numOfSequence(num):
    count = 0
    num1 = 1
    num2 = 0
    while count != num:
        count+=1 
        temp = num1
        num1 = num2+num1
        num2 = temp
        print(num1+num2)

numOfSequence(5) # change 5 to whatever you want, sets how many times it calculates the sequence

