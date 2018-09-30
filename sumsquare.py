

def main():
    square = sum_square()
    print(square)
    sum = square_sum()
    print(sum)
    difference = sum-square
    print("the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is: ", difference)

def sum_square():
    sum = 0
    for i in range(1,101):
        sum+=(i*i)
    return sum

def square_sum():
    sum_natural = 0
    for i in range(1,101):
        sum_natural+=i
    sum = sum_natural*sum_natural
    return sum

main()
