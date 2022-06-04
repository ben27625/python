print("Chương trình kiểm tra năm nhuận ")
year = int(input("Mời bạn nhập số năm"))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Là năm nhuận")
else:
    print("Năm" , year, "không nhuận")