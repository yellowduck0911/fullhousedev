ten = input("nhập tên khách hàng:")
khoang_cach = int(input("nhập quãng đường(km):"))
gio = int(input("nhập giờ xuất phát(0-23):"))
loai_xe = input("nhập loại xe (4 cho, 7 cho):")
mua=input("trời có mưa không (co/khong):")
if ten =="":
        print("Tên khách hàng không hợp lệ!")
if khoang_cach <0:
        print("Quãng đường không hợp lệ!") 
if gio <0 or gio >23:
    print("Giờ xuất phát không hợp lệ!")
if loai_xe != "4 cho" and loai_xe != "7 cho":
        print("Loại xe không hợp lệ!")
if mua != "co" and mua != "khong":
        print("Trời mưa không hợp lệ!")        

if ten !="" and khoang_cach >=0 and 0<=gio <=23 and (loai_xe == "4 cho" or loai_xe == "7 cho") and (mua == "co" or mua == "khong"):
        print("----kêt quả----")
        print("Tên khách hàng:",ten)
        print("Quãng đường:",khoang_cach,"km")
        print("loai xe:",loai_xe)
        print(
        """  
        """
        )
        if loai_xe == "4 cho":
            print("giá cước cơ bản:",round(khoang_cach*12000,1),"VND")
        elif loai_xe == "7 cho":
            print("giá cước cơ bản:",round(khoang_cach*15000,1),"VND")
        if (6<=gio <=9 or 16<=gio <=19) and loai_xe=="4 cho":
            print("phụ thu giờ cao điểm:",round(khoang_cach*12000*(10/100),1),"VND")
        elif (6<=gio <=9 or 16<=gio <=19) and loai_xe=="7 cho":
            print("phụ thu giờ cao điểm:",round(khoang_cach*15000*(10/100),1),"VND")        
        if mua == "co":
            print("phụ thu trời mưa:",khoang_cach*5000,"VND")
        if loai_xe=="4 cho" and ((6<=gio <=9 or 16<=gio <=19) or mua=="co"):
            print("tổng cước:",khoang_cach*12000+khoang_cach*12000*(10/100)+khoang_cach*5000,"VND")
        if loai_xe=="7 cho" and ((6<=gio <=9 or 16<=gio <=19) or mua=="co"):
            print("tổng cước:",khoang_cach*15000+khoang_cach*15000*(10/100)+khoang_cach*5000,"VND")
        print(
        """ 
        """
        )
        if khoang_cach < 5:
            chuyen_ngan=print("loại chuyến đi:chuyến ngắn")
        if 5 <= khoang_cach <= 15:
            chuyen_trung_binh=print("loại chuyến đi:chuyến trung bình")
        if khoang_cach > 15:
            chuyen_dai=print("loại chuyến đi:chuyến dài")        
        if khoang_cach>15:
            print("Ưu tiên đièu xe:Ưu tiên tài xế nhiều kinh nghiệm")
        if khoang_cach<5:
            print("Ưu tiên đièu xe:Ưu tiên tài xế gần nhất")
        if 5<=khoang_cach<=15:
            print("Ưu tiên đièu xe:Bình thường")
        if loai_xe=="4 cho" and ((6<=gio <=9 or 16<=gio <=19) or mua=="co"and(khoang_cach*12000+khoang_cach*12000*(110/100)+khoang_cach*5000)>150_000):
            print("Mức cước:cao")
        elif loai_xe=="4 cho" and ((6<=gio <=9 or 16<=gio <=19) or mua=="co"and(khoang_cach*12000+khoang_cach*12000*(110/100)+khoang_cach*5000)<150_000):
            print('Mức cước:thấp')
        if loai_xe=="7 cho" and ((6<=gio <=9 or 16<=gio <=19) or mua=="co"and(khoang_cach*15000+khoang_cach*15000*(110/100)+khoang_cach*5000)>150_000):
            print("Mức cước:cao")
        elif loai_xe=="7 cho" and ((6<=gio <=9 or 16<=gio <=19) or mua=="co"and(khoang_cach*15000+khoang_cach*15000*(110/100)+khoang_cach*5000)<150_000):
            print("Mức cước:thấp")