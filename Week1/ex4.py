def approx_sin(x , n):
    res = 0
    element = x    
    for i in range(n + 1):
        res += element
        element = element * x * x / (( 1 + ((i + 1) * 2)) * (((i+1) * 2)  )  )
        element = -element
    return res

def approx_cos(x , n):
    res = 0
    element = 1    
    for i in range(n + 1):
        res += element
        element = element * x * x / ((((i + 1) * 2)) * (((i+1))*2  - 1)  )
        element = -element
    return res

def approx_sinh(x , n):
    res = 0
    element = x    
    for i in range(n + 1):
        res += element
        element = element * x * x / (( 1 + ((i + 1) * 2)) * (((i+1) * 2)  )  )
    return res

def approx_cosh(x , n):
    res = 0
    element = 1    
    for i in range(n + 1):
        res += element
        element = element * x * x / ((((i + 1) * 2)) * (((i+1))*2  - 1)  )
    return res

print(approx_sin(3.14,10))
print(approx_cos(3.14,10))
print(approx_sinh(3.14,10))
print(approx_cosh(3.14,10))
