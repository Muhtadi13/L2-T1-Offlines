import numpy
import matplotlib.pyplot as plt


# Data = numpy.genfromtxt("latra.txt", dtype=str,encoding=None, skip_footer=1, skip_header=1)
# solub=Data[:,0]
# safe=Data[:,1]
# print(Data)

def f(b, X, Y):
    sz = X.size

    num1 = 0

    for i in range(sz):
        num1 += X[i] * Y[i] * numpy.exp(b * X[i])

    num2 = 0
    for i in range(sz):
        num2 += X[i] * numpy.exp(2 * b * X[i])

    num3 = 0
    for i in range(sz):
        num3 += Y[i] * numpy.exp(b * X[i])

    # sumY = numpy.sum(Y)

    num4 = 0

    for i in range(sz):
        num4 += numpy.exp(2 * b * X[i])

    a = num1 - ((num3 *num2) / num4)

    #print (num1,num2,num3,num4)

    return a


def GaussianElimination(A, B, pivot, showall):
    if showall == True:
        print("Original matrices are ")
        print(A)
        print(B)
    deter = numpy.linalg.det(A)
    numv = B.size
    ans = numpy.zeros((numv, 1))
    fl = 1

    for i in range(numv):

        if pivot == True:
            ind = i
            for j in range(i + 1, numv):
                if numpy.fabs(A[j][i]) > numpy.fabs(A[ind][i]):  # finding the greatest coefficient in column i
                    ind = j
            A[[i, ind]] = A[[ind, i]]
            B[[i, ind]] = B[[ind, i]]

        if numpy.fabs(A[i][i]) <= 0:
            print("Division by zero occurred.\nCan't apply Gaussian elimination.\nInfinite solution\n")
            fl = 0
            break

        for j in range(i + 1, numv):
            r = A[j][i] / A[i][i]
            for k in range(i, numv):
                A[j][k] = A[j][k] - r * A[i][k]
            B[j][0] = B[j][0] - r * B[i][0]
            if showall == True:
                print("operation in forward elimination " + str(i + 1) + " row " + str(j + 1))
                print(A)
                print(B)

    if numpy.fabs(A[numv - 1][numv - 1]) <= 1e-10:
        print("Infinite solution")
        fl = 0

    if fl == 1:

        for i in range(numv):
            ans[i][0] = B[i][0]
        # ans[numv-1]=B[numv-1][0]/A[numv-1][numv-1]

        for i in range(numv - 1, -1, -1):
            for j in range(i + 1, numv):
                ans[i][0] = ans[i][0] - A[i][j] * ans[j]  # obtaining answer with the help of other answers

            ans[i][0] = ans[i][0] / A[i][i]

        # print("Solution matrix in [x0 x1 x2 ... xn-1] format ")
        # ans=numpy.round(ans,4)
        # ans=format(ans,'.4f')
        # for i in range(numv):
        #     print(format(ans[i][0], '.4f'))

    if showall == True:
        print("Determinant of co_efficient matrix is ")
        print(numpy.round(deter, 4))

    return ans


def bisection(left, right, es, iter, X, Y):
    if f(left, X, Y) * f(right, X, Y) > 0:
        print("You have assumed incorrect left and right")
        # print(f(left, X, Y) * f(right, X, Y) )
        return -1

    it = 1
    fl = 1
    cond = True
    temp = left
    prev = left

    while cond:

        temp = (left + right) / 2

        if temp == 0:
            print("You have assumed incorrect left  and right")
            fl = 0
            break

        error = abs((temp - prev) / temp)

        # print("Iteration %d gives error = %0.8f %s" % (it, error * 100, '%'))

        if f(temp, X, Y) * f(left, X, Y) < 0:
            right = temp

        elif f(temp, X, Y) * f(left, X, Y) > 0:
            left = temp

        else:
            return temp

        it = it + 1
        if it > iter:
            fl = 0
            print("Increase iteration number")
            break
        cond = error > es
        prev = temp

    if fl == 1:
        return temp
    else:
        return -1


def expbisect(X, Y):
    b = bisection(-10,20, 0.005, 25, X, Y)

    num1 = 0

    sz = X.size

    for i in range(sz):

        num1 += Y[i] * numpy.exp(b*X[i])

    num2 = 0

    for i in range(sz):
        num2 += numpy.exp(2 * b * X[i])

    a = num1 / num2

    return a, b


# numpy.set_printoptions(precision=4)

# linear model

def linear_regression(X, Y):
    num1 = 0

    sz = X.size

    for i in range(sz):
        num1 += X[i] * Y[i]

    num2 = 0
    for i in range(sz):
        num2 += X[i]

    num3 = 0
    for i in range(sz):
        num3 += Y[i]

    # sumY = numpy.sum(Y)

    num4 = 0

    for i in range(sz):
        num4 += X[i] * X[i]

    a1 = (cnt * num1 - num2 * num3) / (cnt * num4 - num2 ** 2)
    a0 = num3 / cnt - a1 * (num2 / cnt)

    return a0, a1


def linear_function(x, a0, a1):
    return a0 + a1 * x


# linear end
# special linear
def speciallinear_regression(X, Y):
    num1 = 0

    sz = X.size

    for i in range(sz):
        num1 += X[i] * Y[i]

    num4 = 0

    for i in range(sz):
        num4 += X[i] * X[i]

    m = num1 / num4

    return m


def speciallinear_function(x, m):
    return m * x


# special linear end

# saturation model

def saturation_model(X, Y):
    new_X = Y / X
    (a, b) = linear_regression(new_X, Y)

    b = -b

    return a, b


def saturation_func(x, a, b):
    return (a * x) / (b + x)


# saturation end

# power model

def power_model(X, Y):
    new_X = numpy.log(X)
    new_Y = numpy.log(Y)

    (a, b) = linear_regression(new_X, new_Y)

    a = numpy.exp(a)
    return a, b


def power_func(x, a, b):
    return a * pow(x, b)


# power end

# expo model


def exponential_model(X, Y):
    new_Y = numpy.log(Y)
    (a, b) = linear_regression(X, new_Y)
    a = numpy.exp(a)

    return a, b


def expo_function(x, a, b):
    return a *x* numpy.exp(b * x)


# expo end

# polynomial start


def polynomial_model(X, Y):
    A = numpy.zeros((numv, numv))
    B = numpy.zeros((numv, 1))

    C = numpy.zeros(2 * numv)

    for ind in range(cnt):
        nw = 1
        for i in range(2 * numv):
            C[i] += nw
            nw *= X[ind]

    for ind in range(cnt):
        nw = 1
        for i in range(numv):
            B[i][0] += nw * Y[ind]
            nw *= X[ind]

    for i in range(numv):
        for j in range(numv):
            A[i][j] = C[i + j]

    ans = GaussianElimination(A, B, True, False)
    return ans


def poly_function(x, ans):
    a = 0
    nw = 1
    for i in range(numv):
        a += ans[i][0] * nw
        nw *= x
    return a


# poly end


X_s = numpy.array([0.1,0.2,0.4,0.6,0.9,1.3,1.5,1.7,1.8])
Y_s = numpy.array([0.75,1.25, 1.45, 1.25, 0.85, 0.55, 0.35, 0.28, 0.18])
new_Ys=Y_s/X_s

# X_s = numpy.array([1900.0, 1910.0, 1920.0, 1930.0, 1940.0, 1950.0, 1960.0, 1970.0, 1980.0, 1990.0, 2000.0])
# Y_s = numpy.array([10.3, 13.5, 13.9, 14.2, 11.6, 10.3, 9.7, 9.6, 14.1, 19.8, 31.1])


# X_s = numpy.array([0.75, 2, 2.5, 4, 6, 8, 8.5])
# Y_s = numpy.array([0.8, 1.3, 1.2, 1.6, 1.7, 1.8, 1.7])

# X_s = numpy.array([15, 19, 25, 39, 44, 46, 49, 54, 67, 79, 81, 84, 88, 90, 99])
# Y_s = numpy.array([200, 234, 285, 375, 440, 470, 564, 544, 639, 750, 830, 854,
#                           901, 912, 989])


cnt = X_s.size

# cnt=int(input())
#
# X_s=numpy.zeros(cnt)
# Y_s=numpy.zeros(cnt)
#
#
# for i in range (cnt):
#     X_s[i]=float(input())
#
# for i in range (cnt):
#     Y_s[i]=float(input())
numv=1
#numv = int(input())
numv += 1
#ans = polynomial_model(X_s, Y_s)



(a, b) = expbisect(X_s, new_Ys)
#(a,b)=exponential_model(X_s,new_Ys)
print("(alpha,beta)=")
print((a, b))

plt.close('all')
x = numpy.linspace(0,2.5, 10000)

plt.plot(x, expo_function(x, a, b), label="plot of function")
plt.scatter(X_s, Y_s, color='red')

#(9.661785859642901, -2.4733087657046346)

print("solution to testcases are")
test=numpy.array([1.6,2.0])
print(expo_function(test, a, b))

plt.scatter(test,expo_function(test, a, b),color='green')

plt.legend(loc="best")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()
