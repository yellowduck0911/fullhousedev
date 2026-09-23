ds=[]
print("-"*50)
print(" "*8,"QUẢN LÝ KHO HÀNG - GROCERY STORE")
print("-"*50)
def menu():
        print("""
          1. Xem danh sách hàng tồn kho
          2. Nhập thêm hàng mới
          3. Cập nhật số lượng tồn kho theo ID
          4. Thoát chương trình
          """)
        print("-"*50)
def show_inventory(ds):
        if ds==[]:
            print("Kho hàng hiện đang trống!")
            return
        else:
            print("--DANH SÁCH TỒN KHO--")
            print(
                f"{"ID":<10}"
                f"{"Tên hàng hóa":<20}"
                f"{"Số lượng tồn kho":<15}"
            )
            for i in ds:
                print(
                    f"{i['id']:<10}"
                    f"| {i["name"]:<18}"
                    f"| {i["quantity"]:<13}"
                )
def add_store(ds,dict_ds):
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
            return
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
def update(ds,dict_ds):
        print("--NHẬP SỐ LƯỢNG TÔN KHO--")
        check_hang=input("Nhập mã hàng háo cần sửa:")
        for check in ds:
            if check_hang in check["id"]:
                print(f"Tìm thấy hàng hóa:{check["name"]} (Số lượng hiện tại: {check['quantity']})")
                update=int(input("Nhập số lượng mới:"))
                check["quantity"]=update
                print("Cập nhật số lượng hàng thành công!")
                break
        else:
                print(f"không tìm thấy hàng hóa có mã {check_hang}!")
        print("Cảm ơn bạn đã sử dụng chương trình!")
        print("[Chương trình kết thúc]")
def main():
        menu()
        while True:
            menu()
            try:
                  nhap=int(input("Mời bạn chọn chức năng(1-4):"))
            except:
                  print("Hãy nhập vào kí tự số!!")
            if nhap<1 or nhap>4:
                  print("Hãy nhập 1 trong 4 lựa chọn!!")
                  continue
            if nhap==1:
                show_inventory(ds)
            if nhap==2:
                add_store(ds,dict_ds=dict)
            if nhap==3:
                update(ds,dict_ds=dict)
            if nhap==4:
                break
main()
        
    
        
    
