#Prints all even fibonacci numbers whose sum does not exceed 4,000,000

count = 0
sum = 0
n1 = 1
n2 = 2

while(n1<=4000000):
    #print(n1, end=", ")
    if(n1%2==0):
        sum+=n1
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count+=1
    
print("The sum of the even terms whose Fibonacci sequence whose values do not exceed four million is: ", sum)
