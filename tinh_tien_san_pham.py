while True:
 tong=0
 don_hang=""
 so_luong_hang=0
 ten=input("tên khách hàng:")
 so_luong=int(input("số lượng sản phẩm:"))
 for san_pham in range(1,so_luong+1):
        ten_san_pham=input("tên sản phẩm:")
        don_gia=int(input("đơn giá:"))
        so_luong_mua=int(input("số lượng mua:"))
        so_luong_hang+=so_luong_mua
        thanh_tien=don_gia*so_luong_mua
        tong+=thanh_tien
        don_hang+=f"{ten_san_pham} | {don_gia} x {so_luong_mua}={thanh_tien}\n"
        if tong>=500_000:
            tien_giam=0.1
        elif 300_000<=tong<=500_000:
            tien_giam=0.05
        else:
            tien_giam=0
        tien_thanh_toan=tong-tien_giam*tong
 print("=======HÓA ĐƠN========")
 print("khách hàng:",ten)
 print(don_hang,end="")
 print("tổng tiền:",tong)
 print("giảm giá:",tien_giam*100,"%")
 print("thanh toán:",tien_thanh_toan)
 if tien_thanh_toan>=300_000 and so_luong_hang>=3:
        print("có quà tặng")
 else:
        print("không có quà tặng")
        mua_tiep=""
 while True:
        mua_tiep=input("bạn có muốn mua nữa không?(y/n):")
        if mua_tiep=="y":
                 break
        elif mua_tiep=="n":
                 break
        else:
                 print("lỗi")
 if mua_tiep=="n":
            break
        
            

         
            
        
            
    
    
