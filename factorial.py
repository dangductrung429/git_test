# Tính tổng s = 1! + 2! + 3! + ... + 10! (dùng for)

# tính giai thưa cua a
def tinhgiaithua(a):
    a_zt = 1
    for i in range (1,a+1):
        a_zt = a_zt * i
        i = i + 1
    #print(a_zt)
    return a_zt

# tính tổng
s = 0
for a in range(1,11):
    s = s + tinhgiaithua(a)
print(f"tông dãy số là: {s}")