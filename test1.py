num = int(input("输入分子："))
den = int(input("输入分母："))
def gcd(num,den):
    if num%den==0:
        num=num/den
        den = den / den
    else:
        num = num
        den = den
    return print(num,"/",den)
gcd(num,den)