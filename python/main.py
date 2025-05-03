import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x ** 3 - 0.18 * (x ** 2) + 4.752e-4


def d(x):
    return 3 * (x ** 2) - 0.36 * x


plt.close('all')
x = np.linspace(-0.099, 0.199, 10000)
plt.plot(x, f(x), label="plot of function")

plt.legend(loc="best")

plt.xlabel("Depth")
plt.ylabel("f(x)")
plt.grid()
plt.show()


def bisection(left, right, es, iter):
    if f(left)*f(right) > 0:
        print("You have assumed incorrect left and right")
        return "no"

    it = 1
    fl = 1
    cond = True
    temp = left
    prev =left

    while cond:

        temp = (left + right) / 2

        if temp == 0:
            print("You have assumed incorrect left  and right")
            fl = 0
            break

        error = abs((temp - prev) / temp)

        print("Iteration %d gives error = %0.8f %s" % (it, error * 100, '%'))

        if f(temp) * f(left) < 0:
            right = temp

        elif f(temp) * f(left) > 0:
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
        return "no"

print("Bisection Method : ")
left = 0.05    # float(input("Enter left estimate "))
right = 0.07  # float(input("Enter right estimate "))
esb = 0.005  # float(input("Enter highest error "))
iterb = int(input("Enter maximum iteration "))

ansb = bisection(left, right, esb, iterb)
if ansb == "no":
    print("Can't find root")
else:
    print("Root attained by Bisection method is %0.5f" % ansb)


def newtonraphson(init, es, iter):
    if abs(d(init)) <= 0.0000:
        print("give another initial value ")
        return "nothing"
    it = 1
    fl = 1
    cond = True
    temp = 0
    while cond:

        temp = init - f(init) / d(init)
        if temp == 0:
            print("Division by zero occurred ")
            fl=0
            break

        error = (abs(temp - init) / temp)
        print("Iteration %d gives error = %0.8f %s" % (it, error * 100, '%'))

        it = it + 1
        if it > iter:
            print("Increase iteration number")
            fl = 0
            break

        cond = error > es
        init = temp

    if fl == 1:
        return temp
    else:
        return "nothing"


print("Newton-Raphson Method : ")
init = 0.05  # float(input("Enter approximate root "))
es = 0.005  # float(input("Enter highest error "))
iter = int(input("Enter maximum iteration "))

ans = newtonraphson(init, es, iter)

if ans == "nothing":
    print("Can't find root")
else:
    print("Root attained by Newton-Raphson method is %0.5f" % ans)
