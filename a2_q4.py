#This function will divide the input into two groups of equal sizes, where the difference between the sums of each group is minimised
def diff_num(x:list):
    group_1=[]
    group_2=[]
    length_x = len(x)
    for i in range(length_x//2):
        group_1.append(x[i])
    for i in range(length_x//2,length_x):
        group_2.append(x[i])