#Print positive numbers from list of numbers 

list1 = [12 , -7 , 5 , 64 , -14] 
list2 = [12 , 14 , -95 , 3]

print(list1)
for n1 in list1: 

    if n1 >= 0: #condition checking
       print(n1, end = " ") 

print("\n",list2)       
for n2 in list2:
    
    if n2 >= 0: 
       print(n2, end = " ") 
