ds=[]
print("="*50)
print(" "*10,"QUẢN LÍ BÃI XE - SMART PAKING")
print("="*50)
while True:
    dict_ds={
    "id":int(),
    "plate":"",
    "type":"",
    "entry_time":""
    }
    print("-"*50)
    print("""
    1. Check-in (Đăng kí xe vào)
    2. Báo cáo tồn kho (Hiển thị danh sách)
    3. Tìm kiếm xe (Theo biển số)
    4. Check-out (Xử lí xe ra & Tính phí)
    5. Thoát chương trinh """
    )
    print("-"*50)
    try:
        nhap=int(input("Nhập lựa chọn của bạn(1-5):"))
        if 1>nhap or nhap>5:
            print("xin hãy nhập 1 trong 5 lựa chọn")
    except:
        print("xin hãy nhập lựa chọn của bạn!!!")
        continue
    if nhap==1:
        bien_xe=input("Nhập biển số xe:")
        if not bien_xe:
            print("Không được bỏ trống biển số")
            break
        xe=input("Nhập loại xe:")
        if not xe:
            print("Không được bỏ trống loại xe")
            break
        try:
            gio=int(input("Nhập giờ vào:"))
            if not 0<=gio<=23:
                print("xin hãy nhập đúng giờ!!!")
                break
        except:
            print("lỗi xin hãy nhập đúng giờ vào!!!")
        dict_ds["plate"]=bien_xe
        dict_ds["type"]=xe
        dict_ds["entry_time"]=gio
        ds.append(dict_ds)
        for a in range(len(ds)):
            dict_ds["id"]=1+a
    if nhap==2:
        if ds==[]:
            print("[Thông báo: Bãi xe hiện đang trống!]")
            continue
        print(
        f"{"ID":<10}"
        f"{"| Biển số xe":<20}"
        f"{"| Loại xe":<15}"
        f"{"| Giờ xe vào":<15}"
            )
        print("-"*60)
        for i in range(len(ds)):
            print(
                f"{ ds[i]['id']:<10}"
                f"| { ds[i]['plate']:<18}"
                f"| { ds[i]['type']:<13}"
                f"| { ds[i]['entry_time']}"
                )
    if nhap==3:
        check=input("Nhập biển số xe cần tìm:") 
        for check_xe in ds:
            if check==check_xe['plate']:
                print("Thông tin chi tiết:",check_xe)
                break
        else:
                print(f"[Lỗi]: Không tìm thấy biển số {check} trong hệ thống!")  
    if nhap==4:
        nhap_bien_so=input("Nhập biển số xe cần ra:")
        for check_xe_ra in ds:
                if nhap_bien_so==check_xe_ra['plate']:
                    break
        else:        
                print(f"[Lỗi]: Không tìm thấy biển số {nhap_bien_so} trong hệ thống!")
                continue
        nhap_gio_ra=int(input("Nhập giờ ra:"))
        for time in ds:
            if nhap_bien_so in time:
                if nhap_gio_ra < time[nhap_bien_so]["entry_time"]:
                    print("Lỗi: Giờ ra không thể nhỏ hơn giờ vào!")
                    continue
            for xe in ds:
                    if nhap_bien_so==xe['plate']:
                        print("Tổng phí phải trả:",(nhap_gio_ra-xe['entry_time'])*1500)
                        ds=[item for item in ds if item["plate"]!=nhap_bien_so]       
                        print(f"[Thành công]: Đã xóa xe ID {xe["id"]} thành công!") 
    if nhap==5:
        print("Cảm ơn và hẹn gặp lại!!!")
        break           
        
        
        
        
        
