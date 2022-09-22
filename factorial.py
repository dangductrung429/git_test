# Tính tổng s = 1! + 2! + 3! + ... + 10! (dùng for)

# tính giai thưa cua x
def tinhgiaithua(x):
    x_zt = 1
    for i in range (1,x+1):
        x_zt = x_zt * i
        i = i + 1
    #print(x_zt)
    return x_zt

# tính tổng
s = 0
for x in range(1,11):
    s = s + tinhgiaithua(x)
print(f"tông dãy số là: {s}")