import math
def excercise1(tp , fp , fn):

    dic = [tp,fp,fn]

    if any(not isinstance(v,int) for v in (tp,fp,fn)) :
        notIntDic = [ v for v in dic if not isinstance(v,int)]
        print(" and ".join(str(v) for v in notIntDic)," must be int.")
    if any( v <= 0 for v in (tp,fp,fn)) :
        lowerThanZero = [v for v in dic if v <= 0]
        print(" and ".join(str(v) for v in lowerThanZero), "must be greater than zero")

    Precision = (tp)/(tp + fp)
    Recall = tp/(tp + fn)
    F1_score = 2 * Precision * Recall / (Precision + Recall)

    return Precision,Recall,F1_score
def is_number(x):
    try:
        float(x)
    except ValueError:
        return False
    return True
def activeFuntion(x , st):
    if(not is_number(x)):
        print("x must be a number ")
        return None
    if(st not in ["sigmoid","relu","elu"]):
        print(f"{st} is not supported")
        return None
    match st:
        case "sigmoid" :
            return 1 / ( 1  + math.exp(-x))
        case "relu" :
            return x if x > 0 else 0
        case "elu":
            a = 0.01
            return a*(math.exp(x) -1 ) if x <= 0 else x
        

print(excercise1(1 , 2 ,5))
print(activeFuntion(1.5,"sbigmoid"))