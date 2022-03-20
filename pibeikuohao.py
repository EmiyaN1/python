# from C\Users\emiya\Desktop\python\test\AAA.py import f
# f = open(r"C:\Users\emiya\Desktop\python\test\AAA.py", mode='r')
# import sys  不同文件夹下的调用
# sys.path.append(r'C\Users\emiya\Desktop\python')
# import BBB
import AAA  # 同一个文件夹下的调用

s = AAA.Stack()
print(not s.isEmpty())
