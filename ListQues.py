"""
Create a list having elements 1,2,3,4,5.
Write function for following opeartions :
1. Swap any 2 elements of which indexes are passed eg 0, 4 --> 5,2,3,4,1
2. Maximum value of that list ---> 5
3. Minimum value of that list --> 2
4. Check if list is sorted in ascending order. --> True
"""

# create a list 1,2,3,4,5
my_list = [1,2,3,4,5]

# 1. swap any 2 element of which indexes are passed

    #create a function to make the swap action
def swap(swap_list, ele_one, ele_two):
    swap_list[ele_one], swap_list[ele_two] = swap_list[ele_two], swap_list[ele_one]
    return swap_list

print(my_list)

val_one = input("Enter val 1 \n") #index of 1st element
val_two = input("Enter val 2 \n") #index of 2nd element
print(swap(my_list,int (val_one),int (val_two)))
print(my_list)


# 2. maximum value of the list
print("max value of list: ",max(my_list))

# 3. minimum value of the list
print("min value of list: ",min(my_list))


# 4. check if list is sorted in ascending order
if my_list.sort() is my_list:
    print("True")
else:
    print("False")




