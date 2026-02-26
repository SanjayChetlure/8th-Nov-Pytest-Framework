from datetime import datetime


def m1():
    s1=datetime.now()
    s2=s1.strftime("%Y-%m-%d_%H-%M")
    print(s2)

m1()