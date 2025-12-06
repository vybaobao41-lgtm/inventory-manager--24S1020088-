# inventory.py

# Khai báo biến danh sách toàn cục products
products = []
# Cập nhật hàm add_product() trong inventory.py
def add_product():
    global products # Khai báo sử dụng biến toàn cục products
    print("\n--- NHẬP HÀNG MỚI ---")
    try:
        name = input("Nhập tên sản phẩm: ")
        price = float(input("Nhập giá sản phẩm: "))
        quantity = int(input("Nhập số lượng tồn kho: "))
        
        # Tạo dictionary sản phẩm
        new_product = {
            'name': name,
            'price': price,
            'qty': quantity
        }
        
        # Thêm vào danh sách products toàn cục
        products.append(new_product)
        print(f"Đã nhập hàng thành công: {name} (SL: {quantity})")
        
    except ValueError:
        print("Lỗi: Giá và Số lượng phải là số hợp lệ.")



def view_inventory():
    pass 

def check_low_stock():
    pass 

def main():
    while True:
        print("\n--- QUẢN LÝ KHO HÀNG ---")
        print("1. Nhập hàng mới")
        print("2. Xem tồn kho")
        print("3. Cảnh báo hết hàng")
        print("4. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            check_low_stock()
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()