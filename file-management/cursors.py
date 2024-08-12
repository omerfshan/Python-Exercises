f=open("file-management\msg.txt")

print(f.read())
print(f.read())

f.seek(0)
print(f.readable())

# Dosyanın başına git
f.seek(0)

# Dosyanın tamamını oku
print(f.read())

# Dosyanın tamamını tekrar oku
print(f.read())

# Dosyanın 5. baytına git ve oradan itibaren oku
f.seek(5)
print(f.read())

# Dosyanın başına geri dön
f.seek(0)

# Satır satır oku
print(f.readline())  # Birinci satır
print(f.readline())  # İkinci satır
print(f.closed)
f.close()
print(f.closed)
