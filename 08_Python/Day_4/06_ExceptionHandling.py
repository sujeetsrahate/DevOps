try:
    print(10+'50')
    print('50'+10)
    print(50/0)
except TypeError :
    print("This is typeError")

except ValueError :
    print("This is ValueError")

except ZeroDivisionError :
    print("ZeroDivisionError")

finally:
    print("this is finally block")