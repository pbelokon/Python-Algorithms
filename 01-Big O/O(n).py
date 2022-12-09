 # O(n) is always going to be a straight line, it is what is called proportional 
def print_items(n):
    for i in range(n):
        print(i)

print_items(10)
                  
# This below ran n + n = 2n times it can be written like O(2n) but can be simplified to O(n)
# It is because we always drop constants 
def print_itemsTwo(n):
    for i in range(n):
        print(i)

    for j in range(n): 
        print(j)

print_itemsTwo(10)

# Drop Constant
# In this  example I run n * n or O(n^2), for loop within a for loop 
# If we have a loop within a loop with in a loop n * n * n you may think that it will be O(n^3)
# This would be wrong we always simplify it to O(n^2)
def print_itemsThree(n):
    for i in range(n):
        for j in range (n):
            print(i, j)

print_itemsThree(10)
# O(n^2) line is much more stipes which means it is a lot less efficient than O(n)


# Drop non  dominants
def print_itemsFour(n):
    for i in range(n):
        for j in range (n): # O(n^2)
            print(i, j)
        
        for k in range(n): # O(n)
            print(k)

print_itemsFour(10)
# O(n^2 + n) the number of operation of n ^ 2 is much greater so it is dominant while n does not have a significant 
# impact so we drop it O(n^2)