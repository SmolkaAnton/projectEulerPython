#Finds the sum of all multiples for 3 and 5 between 1 and a user input
input = int(input("Input a number: "))
sum=0
count = 1
while(count<input):
    if(count%3==0 or count%5==0):
        sum+=count
    count+=1

print("The sum is: ", sum)
