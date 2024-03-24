##### Adding a new function called "xth_alphabet_repeat_y_times"

##This function takes one argument with two non-zero numeric numbers ("x" and "y").
##Python

def a2_q2(n):
    answer = {}
    answer["power_xy"] = pow (n["x"],n["y"]) 
    answer["power_yx"] = pow (n["y"],n["x"])
    answer["repeat_x_times"]= "x"*n["x"]
    answer["repeat_y_times"]=str(n["y"])*n["y"]
    for key, value in (n):
        if key == "x":
            xth_alphabet = chr(ord('a')+value-1)
        elif key == "y":
            result = xth_alphabet * value
    answer["xth_alphabet_repeat_y_times"]= result
    return answer
