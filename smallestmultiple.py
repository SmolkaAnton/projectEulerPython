import time

def main():
    smallest = smallest_multiple()
    print("The smallest number that can be divided by each of the numbers from 1 to 20 without any remainder is:  ", smallest)
    
def smallest_multiple():
    #Able to cut down on the numbers we actually have to check
    check_list = [11, 13, 14, 16, 17, 18, 19, 20]
    for num in range(20, 999999999, 20):
        if all(num % n == 0 for n in check_list):
            return num
    return None

main()
