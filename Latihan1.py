max = 0

bilangan = int(input("Masukkan bilangan :"))
while bilangan != 0 :
    if bilangan > max : 
        max = bilangan
    bilangan = int(input("masukkan bilangan :"))
print(f"bilanga terbersar = {max}")