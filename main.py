# a function that takes a list and target parameter and loops until target is found
# multiple variables: middle, start, end, steps
# increase the steps each time a split is done
# conditions to track target position


def binary_search(list, target):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start <= end):
        #print line that shows the steps
        print("Step",steps, ":", str(list[start:end+1]))

        steps = steps+1
        #middle determines middle of list
        middle = (start + end) // 2
        #returns middle value if it matches target value
        if target == list[middle]:
            return middle
        #shortens the list if the target value is less than middle value
        #makes middle value in the list the end value and removes rest of list that does not match
        if target < list[middle]:
            end = middle - 1
        #makes the start of the list equal to the top half of the list if either of the preivous conditions are met
        #the bottom half of the list is removed
        else:
            start = middle + 1
    #Condition checker return statement
    return -1


#TEST CASE
my_list = [1,2,3,4,5,6,7,8,9,10,11,32,12]
target = 8
print("Target:", target)

binary_search(my_list, target)
