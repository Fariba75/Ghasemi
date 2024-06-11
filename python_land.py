def login():
    username = input("نام کاربری: ")
    password = input("رمزعبور: ")

    if username == "amirhossein" and password == "12345":
        print("ورود موفقیت آمیز")
    elif username == "hooshang" and password == "009922":
        print("ورود موفقیت آمیز")
    elif username == "manizhe" and password == "00000":
        print("ورود موفقیت آمیز")
    elif username == "mahsa" and password == "m11m3":
        print("ورود موفقیت آمیز")
    else:
        print("نام کاربری یا رمزعبور اشتباه است")

login()     
