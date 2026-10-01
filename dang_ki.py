import json
write_data=[{"users":"",
            "passwords":"",
            "fullname":"",
            "login_count":0}]
def empty():
    with open("users.json","r",encoding="utf-8") as f:
        if not json.load(f):
            with open("users.json","w",encoding="utf-8") as f:
                json.dump({"users": []},f,ensure_ascii=False)
                return {"users": []}
def load_users():
            try:
                with open("users.json","r",encoding="utf-8") as af:
                    check=json.load(af)
                    return check
            except FileNotFoundError:
                empty()
                error=print("Bạn chưa đăng kí tài khoản, xin hãy đăng kí!")
                return error 
def menu():
    print("""=====Hệ thống đăng kí tài khoản=====
1. Đăng ký
2. Đăng nhập
3. Thoát""")
def save_data(write_data):
    with open("users.json","w",encoding="utf-8") as f:
            json.dump(write_data,f,ensure_ascii=False,indent=4)
def register():
    while True:
            name=input("Username:").strip()
            mk=input("Password:").strip()
            tach=list(mk)
            if len(tach)<6:
                print("Lỗi: Mật khẩu phải có ít nhất 6 kí tự!")
                continue
            full_name=input("Họ tên:").strip()
            if not full_name or not name or not mk:
                    print("Không được bỏ trống")
                    continue
            for item in write_data:
                item["users"]=name
                item["passwords"]=mk
                item["fullname"]=full_name
                item["login_count"]=0
            print("Đăng kí thành công!")
            break
def login():
    count_limit=3
    count=0
    data=load_users()
    if not data:
        return
    while count<count_limit:
        while True:
            check_user=input("Username:").strip()
            if not check_user:
                print("Username không được bỏ trống!")
                continue
            while True:
                check_password=input("Password:").strip()
                for items in data:
                    if (check_user == items["users"]) and (check_password == items["passwords"]):
                        check=print(f"xin chào:{items['users']}(đăng nhập lần thứ {items["login_count"]+1})")
                        items["login_count"]+=1
                        save_data(data)
                        return check
                    else:
                        count+=1
                        if count_limit-count==0:
                            print(f"Tên tài khoản hoặc mật khẩu đã nhập sai!(bạn đã hết lần thử!)")
                            continue
                        else:
                            print(f"Tên tài khoản hoặc mật khẩu đã nhập sai!(bạn còn {count_limit-count} lần thử!)")
                break
            if count==3:
                    break
def main():   
    while True:      
        menu()
        try:
            nhap=int(input("Nhập:"))
        except:
            print("Yêu cầu nhập 1 trong 3 số!")
            continue
        if nhap==1:
            register()
            save_data(write_data)
        elif nhap==2:
            login()
        elif nhap==3:
            break
        else:
            print("xin hãy chọn từ 1-3!")
main()


    
        
        
    