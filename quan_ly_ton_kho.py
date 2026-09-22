ds=[]
print("-"*50)
print(" "*8,"QUẢN LÝ KHO HÀNG - GROCERY STORE")
while True:
    print("-"*50)
    print("""
          1. Xem danh sách hàng tồn kho
          2. Nhập thêm hàng mới
          3. Cập nhật số lượng tồn kho theo ID
          4. Thoát chương trình
          """)
    print("-"*50)
    try:
        nhap=int(input("Mời bạn chọn chức năng(1-4):"))
    except:
        print("Hãy nhập vào kí tự số!!")
    if nhap<1 or nhap>4:
        print("Hãy nhập 1 trong 4 lựa chọn!!")
        continue
    if nhap==1:
        if ds==[]:
            print("Kho hàng hiện đang trống!")
        else:
            print("--DANH SÁCH TỒN KHO--")
            print(
                f"{"ID":<10}"
                f"{"Tên hàng hóa":<20}"
                f"{"Số lượng tồn kho":<15}"
            )
            for i in range(len(ds)):
                print(
                    f"{ds[i]['id']:<10}"
                    f"| {ds[i]["name"]:<18}"
                    f"| {ds[i]["quantity"]:<13}"
                )
    elif nhap==2:
        print("--NHẬP HÀNG HÓA MỚI--")
        ma_hang=input("Nhập mã hàng hóa (ID):")
        while True:
            if ma_hang=="":
                input("Mã hàng không được để trống! Nhập lại:")
            else:
                break
        ten_sp=input("Hãy nhập tên hàng hóa:")
        while True:
            if not ten_sp:
                print("tên sản phẩm không được để trống!")
            else:
                break
        try:
            so_luong=int(input("Nhập số lượng tồn kho:"))
        except:
            print("Số lượng hàng hóa là một số!")
        while True:
                if so_luong<=0:
                    input("Số lượng phải lớn hơn 0! Nhập lại:")
                else:
                    break
        dict_ds={
                        "id":ma_hang,
                        "name":ten_sp,
                        "quantity":so_luong
                    }
        ds.append(dict_ds)
        print("Thêm hàng hóa vào thành công!")
    elif nhap==3:
        print("--NHẬP SỐ LƯỢNG TÔN KHO--")
        check_hang=input("Nhập mã hàng háo cần sửa:")
        for check in ds:
            if check_hang in check["id"]:
                print(f"Tìm thấy hàng hóa:{dict_ds["name"]} (Số lượng hiện tại: {dict_ds['quantity']})")
                update=int(input("Nhập số lượng mới:"))
                dict_update={"quantity":update}
                dict_ds.update(dict_update)
                print("Cập nhật số lượng hàng thành công!")
                break
        else:
                print(f"không tìm thấy hàng hóa có mã {check_hang}!")
    elif nhap==4:
        print("Cảm ơn bạn đã sử dụng chương trình!")
        print("[Chương trình kết thúc]")
        break
    
        
    