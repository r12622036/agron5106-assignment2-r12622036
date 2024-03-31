##First task 
##Categorizing Companies by Fluctuations of 10%, 20%, or More Than 20%
##To sort the companies based on different fluctuations, we need to have a function that calculates the fluctuations between today's and yesterday's stock rates. Both rates should represent the closing rates at the end of the market session.
#data given should be in this form 
#data={"company_x":(yesterday_y,today_y),"company_y":(yesterday_y,today_y),"company_z":(yesterday_y,today_y)}

def dailytask_1(data:dict):
    result={}
    for x,(yesterday_y,today_y) in data.items():
        fluctuation = round(((today_y - yesterday_y)/yesterday_y)*100,2)
        if abs(fluctuation) <= 10:
            result[x]={"Fluctuation":fluctuation,"Category":"0-10%"}
        elif abs(fluctuation) > 10 and abs(fluctuation) <= 20:
            result[x]={"Fluctuation":fluctuation,"Category":"10-20%"}
        else:
            result[x]={"Fluctuation":fluctuation,"Category":"Above 20%"}
    return result

        


