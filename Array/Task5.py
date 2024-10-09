from array import *
Val = array('i',(1,2,3,4,4,5,6,7))
Val.extend([1,2,3,4])
print('before sorting the elemnets',Val)
# SOrting the elemnts which are available in the Array
for ind in range(len(Val)):
    for ind1 in range(ind+1,len(Val)):
        if Val[ind]>Val[ind1]:
            Val[ind],Val[ind1]=Val[ind1],Val[ind]
print('After sorting the elemnts',Val)