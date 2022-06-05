 điếm số ngày trong tháng ")
month = int(input("Nhập vào một tháng : "))
if month in (1,3,5,7,8,10,12):
    print("Tháng ", month, "Có 31 ngày ")
elif month in (4,6,9,11):
    print("Tháng ", month, "Có 30 ngày")
elif month == 2:
    year = int(input("Mời bạn nhập vào năm"))
    if (year%4 == 0 and year % 100 != 0 ) or year % 400 == 0:
        print("Tháng ", month,"Có 29 ngày ")
    else:
        print("Tháng ", month, "Có 28 ngày ")
else:# Điếm số ngày trong tháng

print("Chương trình
    print("Tháng ", month, "Không hợp lệ")

