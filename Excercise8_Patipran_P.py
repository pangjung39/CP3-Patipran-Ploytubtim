username = input("Username : ")
password = input("Password : ")
if username == "Patipan" and password == "Ploytubtim":
    print("Log In success")
    print("""ยินดีต้อนรับสู่ร้านของชำ
     กรุณาเลือกสินค้า
      1. แป๊ปซี่  10 บาท
      2. โค้ก   10 บาท
      3. เลย์ โนริ สาหร่าย  20 บาท
      4. เลย์ ซาวครีม   20 บาท 
      """)
    product = int(input(" กรุณาใส่หมายเลขสินค้า : "))
    if product == 1:
        print("แป๊ปซี่ 10 บาท")
        amount = int(input("กรุณาใส่จำนวนที่ต้องการ : "))
        price = amount*10
        print("ราคารวม ",price ,"บาท")
    elif product == 2:
        print("\033[31m","โค้ก   10 บาท","\033[0m")
        amount = int(input("กรุณาใส่จำนวนที่ต้องการ : "))
        price = amount*10
        print("ราคารวม ",price ,"บาท")
    elif product == 3:
        print("เลย์ โนริ สาหร่าย   20 บาท ")
        amount = int(input("กรุณาใส่จำนวนที่ต้องการ : "))
        price = amount*20
        print("ราคารวม ",price ,"บาท")
    elif product == 4:
        print("เลย์ ซาวครีม")
        amount = int(input("กรุณาใส่จำนวนที่ต้องการ : "))
        price = amount*20
        print("ราคารวม ",price ,"บาท")
    else:
        print("ระบบไม่สามารถเลือกรายการให้ได้ ระบบยกเลิกอัตโนมัติ")
else:
    print("Can not Access")

