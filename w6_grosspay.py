hrs = input("Enter Hours:")
rate = input("Enter Rate per hour")
def computepay(h, r):
    hrs = float(h)
    rate = float(r)
    if hrs > 40:
        gross_pay = 40*rate + ((hrs-40)*rate*1.5)
    else:
        gross_pay = hrs*rate
    return gross_pay


p = computepay(hrs,rate)
print("Pay", p)
