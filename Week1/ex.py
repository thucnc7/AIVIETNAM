import math
import random
def regressionLossFunction(num_samples , loss_name ):
    
    if not isinstance(num_samples,int) or num_samples <= 0 :
        print("Number of samples must be a integer number")
        return None
    
    if(loss_name not in ["MSE","MAE","RMSE"]) :
        print("Regression loss function not supported .")
        return None
    
    sum = 0 
    
    
    for i in range(num_samples + 1):

        temp = abs(random.uniform(0,10) - random.uniform(0,10))
        if(loss_name in ["MSE","RMSE"]):
            temp *= temp
        sum += temp
        print(temp)
        
        
    res = sum / num_samples    
    
    if(loss_name == "RMSE"):
        res = math.sqrt(res)
    return res

print(regressionLossFunction(10 , "MSE"))