def get_user_input():
    numbers = []
    n = int(input("Enter number of elements : "))
    for i in range (0,n):
        elements = int(input())
        numbers.append(elements)

    print(numbers)
    return numbers

def  find_min_max(q):
    numbers = q
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
if __name__ == "__main__":
    q = get_user_input()
    find_min_max(q)
