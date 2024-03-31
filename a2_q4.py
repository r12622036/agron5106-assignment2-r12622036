#This function will divide the input into two groups of equal sizes, where the difference between the sums of each group is minimised
#Adding the difference equation into the diff_num function 
#Adding the return as the previous function didn't have any return 
def diff_num(x:list):
    group_1=[]
    group_2=[]
    length_x = len(x)
    for i in range(length_x//2):
        group_1.append(x[i])
    for i in range(length_x//2,length_x):
        group_2.append(x[i])
    diff= abs(sum(group_1)-sum(group_2))
    return group_1,group_2,diff 