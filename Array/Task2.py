from array import * 
example = array('i',(1,2,3,4,5))
print(example)
# We are accessing by using the for loop
for i in example:
    print(i)
# In this below program iam accessing particular element and iam replacing with the new value
for i in range(len(example)):
    if example[i]==5:
        example[i]= 10
    print(example[i])
#After replacing the new element printing the array
print(example)