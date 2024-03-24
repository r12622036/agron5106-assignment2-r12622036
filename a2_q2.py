##### Selecting Language , Changing Function Name

##This function takes one argument with two non-zero numeric numbers ("x" and "y").
##Python

def a2_q2(n):
    answer = {}
    answer["sum"] = n["x"] + n["y"]
    answer["difference"] = n["x"] - n["y"]
    answer["product"] = n["x"] * n["y"]
    answer["ratio"] = n["x"] / n["y"]
    return answer
