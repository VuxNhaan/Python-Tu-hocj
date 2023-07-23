import math
import os
os.system('cls')
"""Bài 1: Viết chương trình Python 
tính tổng các phần tử của danh sách"""
def Bai1(a):
    sum = 0
    for i in range(0, len(a)):
        sum += a[i]
    return sum

"""Bài 2: Viết chương trình Python đếm số lượng các 
số hạng dương và tổng của các số hạng dương."""
def Bai2(a):
    Sum = 0
    Count = 0
    for i in range(0, len(a)):
        if a[i] > 0:
            Count += 1
            Sum += a[i]
    return Count, Sum

"""Bài 3: Viết chương trình Python tính trung bình 
cộng của cả danh sách, trung bình cộng các phần tử dương trong danh sách."""
def Bai3(a):
    return round(Bai2(a)[1]/Bai2(a)[0])

"""Bai 4: Tìm vị trí phần tử âm đầu tiên trong danh sách"""
def Bai4(a):
    i = 0
    while a[i] >= 0:
        i += 1
        if i == len(a):
            return len(a)
    return i+1

"""Bài 5. Tìm vị trí phần tử dương cuối cùng trong danh sách"""
def Bai5(a):
    for i in range(len(a)-1, -1, -1):
        if a[i] >= 0:
            return i
    return len(a)

"""Bài 6. Tìm phần tử lớn nhất và vị trí của phần tử lớn nhất cuối cùng"""
def Bai6(a):
    Max = a[0]
    for i in range(1, len(a)-1):
       if a[i] > Max:
           vt = i
           Max = a[i]
    return Max, vt

"""Bai 7: Viết chương trình Python tìm phần tử lớn thứ nhì của danh sách
 và các vị trí của các phần tử đạt giá trị lớn nhì."""
def Bai7(a):
    B=a.copy()
    m=max(B)
    i=0
    while i<len(B):
        if B[i]==m:
            B.remove(B[i])
            i-=1
        i+=1
    if len(B)==0:
        print("Khong co so lon nhi")
    else:
        m=max(B)
        print("So lon nhi la",m,"tai vi tri",end=" ")
        for i in range(len(a)):
            if a[i]==m:
                print(i+1,end=", ")
    
#Bài 8. Số lượng các số dương liên tiếp nhiều nhất
def Bai8(a):
    n = len(a)
    maxN = 0
    max = 0
    for i in range(0, n -1):
        if a[i] >= 0:
            max += 1
            if max > maxN:
                maxN = max
        else:
            max = 0
    return maxN
        
#Bài 9. Tổng dương lớn nhất
def Bai9(a):
    n = len(a)
    Sum = 0
    SumMax = 0
    for i in range(0, n -1):
        if a[i] >= 0:
            Sum += a[i]
            if Sum > SumMax:
                SumMax = Sum
        else:
            Sum = 0
    return SumMax

# Bài 10. Số lượng phần tử đan dấu dài nhất
def Bai10(a):
    n = len(a)
    M = 0
    count = 0
    Max = 0
    for i in range(0, n-1):
        if a[i]*a[i+1] < 0:
            count += 1
            Max = max(count, M)
        else:
            count = 0
    if Max == 0:
        return 0
    return Max+1

# Bài 11. Tính số lượng các phần tử không tăng nhiều nhất.
def Bai11(a):
    n = len(a)
    M = 0
    count = 0
    Max = 0
    for i in range(0, n-1):
        if a[i] >= a[i+1]:
            count += 1
            Max = max(count, M)
        else:
            count = 0
    if Max == 0:
        return 0
    return Max+1

# Bài 12. Tìm vị trí bắt đầu đoạn con dương liên tiếp có nhiều phần tử nhất.
def Bai12(a):
    n = len(a)
    maxN = 0
    max = 0
    star = -1
    for i in range(0, n -1):
        if a[i] >= 0:
            max += 1
            if max > maxN:
                maxN = max
                star = i - max + 1
        else:
            max = 0
    return star
def main():
    a = [-2, -4, 1, 9, 3, 6, 2, 3, -6, 8]
    print(a)
    print(f"Tong cac phan tu trong mang: {Bai1(a)}")
    print("So phan tu duong va tong cac so hang do: ", Bai2(a)[0])
    print("Trung binh cong cac so duong:", Bai3(a))
    print("Vi tri phan tu am dau tien trong mang: ", Bai4(a))
    if Bai5(a) == len(a):
        print("Khong co phan tu duong")
    else:
        print(f"Vi tri phan tu duong cuoi cung la: {Bai5(a)}")
    print("Phan tu lon nhat trong mang va vi tri: ", Bai6(a))
    Bai7(a)
    print("Số lượng các số dương liên tiếp nhiều nhất: ", Bai8(a))
    print("Tong các số dương liên tiếp co tong lon nhất: ", Bai9(a))
    print("Số lượng phần tử đan dấu dài nhất: ", Bai10(a))
    print("số lượng các phần tử không tăng nhiều nhất: ", Bai11(a))
    print("Vị trí bắt đầu đoạn con dương liên tiếp có nhiều phần tử nhất: ", Bai12(a))



if __name__ == "__main__":
    main()