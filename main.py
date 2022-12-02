def get_user_input():
    numbers = []
    n = int(input("Enter number of elements : "))
    for i in range (0,n):
        elements = int(input())
        numbers.append(elements)

    print(numbers)
    return numbers

def  find_min_max(q):
    minval = q[0]
    minval = q[0]
    for i in q :
        if i < q[0]:
            minval = i
        if i > q[0]:
            maxval = i
    print ("The minimum value in the array is : "+str(minval))
    print("The maximum value in the array is : " + str(maxval))
    values = [minval,maxval]
    return values
def find_average(q):
    sum = 0.0
    for i in range (0, len(q)):
        sum +=q[i]
    average = sum / len(q)
    print ("The average of all the numbers in the array is " + str(average))
    return average
if __name__ == "__main__":
    q = get_user_input()
    find_min_max(q)
    find_average(q)