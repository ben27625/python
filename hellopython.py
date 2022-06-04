# # print("Mời nhập init :")
# # s = int(input("Mời bạn nhập :"))
# # print("*" * 16)
# print("Xuất" * 12)
#
#
# print("{0}x")


# Tính chu vi diện tích hình tròn
import math

try:
    r = float(input("Mời bạn nhập bán kính hình tròn :"))
    cv= 2*math.pi*r
    dt = r**2
    print("Chu vi = ", cv)
    print("Diện tích", dt)
except:
    print("Lỗi rồi")