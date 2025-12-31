
import numpy

def GaussianElimination(A,B,pivot,showall):

    if showall== True :
        print("Original matrices are ")
        print(A)
        print(B)
    deter = numpy.linalg.det(A)
    numv=B.size
    fl=1

    for i in range(numv):



        if pivot==True :
            ind=i
            for j in range(i+1,numv):
                if numpy.fabs(A[j][i]) > numpy.fabs(A[ind][i]):  # finding the greatest coefficient in column i
                    ind=j
            A[[i,ind]]=A[[ind,i]]
            B[[i,ind]]=B[[ind,i]]

        # print(A)
        # print(B)


        if numpy.fabs(A[i][i])<=0 :
            print("Division by zero occurred.\nCan't apply Gaussian elimination.\nInfinite solution\n")
            fl=0
            break


        for j in range(i+1,numv):
            r = A[j][i] / A[i][i]
            for k in range(i,numv):
                A[j][k]=A[j][k]-r*A[i][k]
            B[j][0]=B[j][0]-r*B[i][0]
            if showall == True:
                print("operation in forward elimination "+str(i+1) +" row "+str(j+1))
                print(A)
                print(B)

    if numpy.fabs(A[numv - 1][numv - 1]) <= 1e-10:
        print("Infinite solution")
        fl = 0



    if fl==1:
        ans=numpy.zeros((numv,1))

        for i in range(numv):
            ans[i][0]=B[i][0]
        #ans[numv-1]=B[numv-1][0]/A[numv-1][numv-1]

        for i in range (numv-1,-1,-1):
            for j in range(i+1,numv):
                ans[i][0]=ans[i][0]-A[i][j]*ans[j]    # obtaining answer with the help of other answers

            ans[i][0]=ans[i][0]/A[i][i]


        print("Solution matrix in [x0 x1 x2 ... xn-1] format ")
        #ans=numpy.round(ans,4)
        #ans=format(ans,'.4f')
        for i in range(numv):
            print(format(ans[i][0],'.4f'))

    if showall == True:
        print("Determinant of co_efficient matrix is ")
        print(numpy.round(deter,4))

#print("Give number of variables :")
numv=int(input())

#print("give "+str(numv)+" ai co_efficients "+str(numv)+" times in a0*x1 + a1*x2 + a2*x3.....+ an-1*xn = an format")

# aug_mat =numpy.zeros((numv,numv+1))

A=numpy.zeros((numv,numv))
B=numpy.zeros((numv,1))

for i in range (numv):
    # for j in range(numv):
    A[i] = list(input().split())

#print("give "+str(numv)+" an constants in a0*x1+a1*x2+a2*x3.....+an-1*xn=an format")

for i in range (numv):
    B[i][0]= float(input())

# print(A)
# print(B)



# numpy.set_printoptions(precision=4)
GaussianElimination(A,B,False,True)


# print(A)
# print(B)








