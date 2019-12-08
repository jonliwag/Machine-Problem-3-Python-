import numpy as np

# since the inuput should be in a nx2 matrix:
print('\n NOTE: for the input, please use the format ,f(np.array([[x1,y1],[x2,y2]]))')  

# defining the function to be evaluated
def f(pts):
    
    x = pts[:,0]
    y = pts[:,1]
    
#  using for loop in range of how many pair of points in the array
    for n in range(len(pts)):
        
#  to get least squares polynomial fit         
        U = np.polyfit(x, y, n)

#  to evaluate the polynomial from given values
        S = np.polyval(U, x)    

#  getting the norm of the matrix
        T = np.linalg.norm(y - S)    
        e = [n, T]
        
        if n == 0:        
            w = e
            
        elif w[1] >= w[1]:        
            z = e[0]
            
    best = np.polyfit(x, y, z)
    
    print('\n coefficients of polynomial to approximate the data: ', best)
    