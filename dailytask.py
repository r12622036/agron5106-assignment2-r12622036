##Second task 
##Make buy or sell decisions based on the fluctuations
##To make the decision, there are rules we need to follow
#if the company are in category "0-10%", whether the fluctuation is positive or negative, the decision will be buying in 
#if the company are in category "10-20%", for negative fluctuation:"buy in", for positive fluctuation:"hold"
#if the company are in category "Above 20%" for negative flucuation:"sell", for positive fluctuation:"hold"
#data should be in the form given by the return of first function  

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

def decisions(data:dict):
    decisions = {}
    for x, info in data.items():
        fluctuation = info["Fluctuation"]
        category = info["Category"]
        if category == "0-10%":
            decisions[x] = "Buy"
        elif category == "10-20%":
            if fluctuation < 0:
                decisions[x] = "Buy"
            else: 
                decisions[x] = "Hold"
        else:
            if fluctuation < 0:
                decisions[x] = "Sell"
            else:
                decisions[x] = "Hold"
    return decisions
        


