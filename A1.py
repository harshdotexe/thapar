#ADITYA GARG 102053015

import math

def heuristic(matrix,p):
    sumEucaledian=0
    sumManhattan=0
    sumMinkowiski=0
    for i in range(8):
      sumEucaledian +=math.sqrt((matrix[3][i]-matrix[1][i])**2 + (matrix[4][i]-matrix[2][i])**2  )
      sumManhattan  +=abs(matrix[3][i]-matrix[1][i])+ abs(matrix[4][i]-matrix[2][i])
      sumMinkowiski +=((abs(matrix[3][i]-matrix[1][i])**p)+ (abs(matrix[4][i]-matrix[2][i])**p))**(1/p)
    
    print(sumEucaledian,sumManhattan,sumMinkowiski)
def main():      
    initial=[[2,0,3],[1,8,4],[7,6,5]]
    goal=[[1,2,3],[8,0,4],[7,6,5]]
    posmatrix = [[0 for i in range(8)] for j in range(5)]
    posmatrix[0]=[1,2,3,4,5,6,7,8]
    p=3  #Minkowski power
    
    for i in range(0,3):
        for j in range(0,3):
            
            if initial[i][j]!=0:
                posmatrix[1][initial[i][j]-1 ]=i
                posmatrix[2][initial[i][j]-1 ]=j
                
            if goal[i][j]!=0:
               posmatrix[3]   [goal[i][j] -1]=i
               posmatrix[4]   [goal[i][j] -1]=j
    
    heuristic(posmatrix,p)

if __name__=="__main__":
    main()