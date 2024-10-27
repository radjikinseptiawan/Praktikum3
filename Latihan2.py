N = int(input("Masukkan jumlah bilangan: "))

max_val = 0

for i in range(1, N + 1):
    bilangan = int(input(f"Masukkan bilangan ke-{i}: "))
    
    if bilangan > max_val:
        max_val = bilangan

print(f"Bilangan terbesar adalah: {max_val}")