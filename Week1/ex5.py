def CanBac(x , hat):
    return x**(1/hat)
def MeanDifferenceOfnthRootError(y , y_hat , n , p) :
    res = CanBac(y,n) - CanBac(y_hat,n)
    res = res**(p);
    return res;
print(MeanDifferenceOfnthRootError(100,99.5,2,1))
    
    