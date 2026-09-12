tong=[]
luu_mssv=[]
luu_ten=[]
luu_tuoi=[]
luu_toan=[]
luu_ly=[]
luu_hoa=[]
print("-"*50)
print("  chào mừng bạn đến với app quản lí sinh viên!")
print("-"*50)
print("""
        1.thêm sinh viên mới
        2.xem thông tin sinh viên
        3.xóa sinh viên
        4.tạo bảng xếp hạngg
        0.thoát chương trình
        """
        )
while True:
    nhap=int(input("vui lòng chọn chức năng mà bạn muốn:"))
    if nhap==1:
            mssv=int(input("MSSV:"))
            ten=input("tên:")
            tuoi=int(input("tuổi:"))
            toan=float(input("toán:"))
            ly=float(input("lý:"))
            hoa=float(input("hóa:"))
            luu_mssv.append(mssv)
            luu_ten.append(ten)
            luu_tuoi.append(tuoi)
            luu_toan.append(toan)
            luu_ly.append(ly)
            luu_hoa.append(hoa) 
            tong_diem=toan+ly+hoa
            tong.append(tong_diem)
    if nhap==2:
            print(
                f"{"mssv":<13}"
                f"{"họ và tên":<17}"
                f"{"tuổi":<10}"
                f"{"toán":<10}"
                f"{"lý":<10}"
                f"{"hóa":<10}"
                f"{"phân loại":<10}"
            )
            for do_dai in range(len(luu_mssv)):
                trung_binh_cong=(luu_toan[do_dai]+luu_hoa[do_dai]+luu_ly[do_dai])/3
                if trung_binh_cong>=8:
                    phan_loai="giỏi"
                elif 6<=trung_binh_cong<8:
                    phan_loai="khá"
                else:
                    phan_loai="trung bình"
                print(
                f"{luu_mssv[do_dai]:<13}"
                f"{luu_ten[do_dai]:<17}"
                f"{luu_tuoi[do_dai]:<10}"
                f"{luu_toan[do_dai]:<10}"
                f"{luu_ly[do_dai]:<10}"
                f"{luu_hoa[do_dai]:<10}"
                f"{phan_loai:<10}"
                )
    if nhap==3:
            xoa_sv=int(input("nhập mã số sinh viên:"))
            if xoa_sv==luu_mssv:
                    xoa_sv=luu_mssv.remove(luu_mssv)
                    print("xóa thành công!!!")
            else:
                print("mã sinh iên không hợp lệ!!!")
    if nhap==4:
        print(
                                    f"{"mssv":<13}"
                                    f"{"họ và tên":<17}"
                                    f"{"tuổi":<10}"
                                    f"{"toán":<10}"
                                    f"{"lý":<10}"
                                    f"{"hóa":<10}"
                                    f"{"phân loại":<10}"
                                )
        for do_dai in range(len(luu_mssv)):
            trung_binh_cong=(luu_toan[do_dai]+luu_hoa[do_dai]+luu_ly[do_dai])/3
            if trung_binh_cong>=8:
                                phan_loai="giỏi"
            elif 6<=trung_binh_cong<8:
                                phan_loai="khá"
            else:
                                phan_loai="trung bình"
            tong.sort(reverse=True)
            print(
                            f"{luu_mssv[do_dai]:<13}"
                            f"{luu_ten[do_dai]:<17}"
                            f"{luu_tuoi[do_dai]:<10}"
                            f"{luu_toan[do_dai]:<10}"
                            f"{luu_ly[do_dai]:<10}"
                            f"{luu_hoa[do_dai]:<10}"
                            f"{phan_loai:<10}"
                            )
    if nhap==0:
        break
            
                        
            
                    
                        
                
                
