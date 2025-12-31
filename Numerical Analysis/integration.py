import numpy
import matplotlib.pyplot as plt

Cme=5e-4

def func(x):
    return -(6.73*x+6.725e-8+Cme*7.26e-4)/((3.62e-12)*x+x*Cme*3.908e-8)


segment=int(input())

# Trapezoidal rule
def trapezoidalIntegration(x0,xn,n):

    h=(xn-x0)/n

    sum=func(x0)+func(xn)

    for i in range (1,n):
        xi=x0+i*h
        sum=sum+2*func(xi)

    result=(sum*h)/2

    #print(result)
    # if n!=1:
    #     err = 0
    #     errper = 0
    #     err = result - prev
    #     errper = numpy.fabs(err) / result
    #     print(str(errper*100)+"%")
    # prev = result

    return result

#end of trapezoidal rule


#simpsons method
def singlesimpsonMethod(x0,xn,n):
    a=x0
    h = (xn - x0) / n
    result=0

    for i in range(1, n, 2):

        xi = a + h
        b= xi + h
        sum = func(a) + 4 * func(xi)+func(b)

        sum=(sum*h)/3
        result=result+sum

        a=b


    return result


def multiplesimpsonIntegration(x0,xn,n):

    h = (xn - x0) / n

    sum = func(x0) + func(xn)

    for i in range(1, n):
        xi = x0 + i * h
        if i%2 ==0:
            sum = sum + 2 * func(xi)
        else :
            sum = sum + 4 * func(xi)

    result = (sum * h) / 3

    # print(result)
    # if n != 2:
    #     err = 0
    #     errper = 0
    #     err = result - prev
    #     errper = numpy.fabs(err) / result
    #     print(str(errper * 100) + "%")
    # prev = result

    return result

#end of simpsons 1 3rd rule



x0=1.22e-4
x1=0.75*x0
x2=0.25*x0


prev=0

print("Using Trapezoid rule ")
for i in range (1,segment+1):
    result=trapezoidalIntegration(x1,x2,i)
    print("Result for segment " + str(i))
    print(result)

    if i!= 1:
        err = result - prev
        errper = numpy.fabs(err) / result
        print("Error in segment " + str(i))
        print(str(errper * 100) + "%")
    print()
    prev = result



print("Using simpsons rule")

for j in range(1, segment + 1):
    result=singlesimpsonMethod(x1,x2,2*j)
    print("Result for segment "+str(2*j))
    print(result)
    if j != 1:
        err = result - prev
        errper = numpy.fabs(err) / result
        print("Error in segment "+str(2*j))
        print(str(errper * 100) + " %")
    print()
    prev = result


list=[1.22e-4,1.20e-4,1.0e-4,0.8e-4,0.6e-4,0.4e-4,0.2e-4]
x=numpy.array(list)
y=numpy.zeros(x.size)

y[0]=x[0]

for i in range (1,x.size):
    y[i]=multiplesimpsonIntegration(x[0],x[i],10)


plt.plot(x,y,label='plot of sample points')
plt.scatter(x,y,color='cyan')

plt.legend(loc="best")

plt.xlabel("Concentration(moles/cc)")
plt.ylabel("Time(seconds)")
plt.grid()
plt.show()






