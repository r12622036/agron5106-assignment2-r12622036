##### Adding two new functions

##This function takes one argument with two non-zero numeric numbers ("x" and "y").
##Python

def a2_q2(n):
    answer = {}
    answer["power_xy"] = pow (n["x"],n["y"]) 
    answer["power_yx"] = pow (n["y"],n["x"])
    answer["repeat_x_times"]= "x"*n["x"]
    answer["repeat_y_times"]=str(n["y"])*n["y"]
    return answer
