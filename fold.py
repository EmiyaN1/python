N = int(input("输入对折次数："))


def fold(self):
    if self == 0:
        return 1
    elif self == 1:
        self = self * 2
        return self
    else:
        self = fold(self - 1) * 2
        return self


a = fold(N)
print(a*0.0001)
