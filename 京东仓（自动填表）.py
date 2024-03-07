import xlwings as xw

wb= xw.books.active

def main():
    total = int(wb.sheets["交接清单"].range("P31").value)

    list1=  []
    for i in  range(total):
        list1.extend([wb.sheets["交接清单"].range(11+i,3).value] * int(wb.sheets["交接清单"].range(11+i,17).value) )  
        list1.append("货物名称")
    wb.sheets["商品清单"].range("B2").options(transpose= True).value = list1        


    list2 = []
    for i in  range(total):
        list2.extend( ("货物名称" , wb.sheets["交接清单"].range(11+i,3).value) * int(wb.sheets["交接清单"].range(11+i,20).value))  

    wb.sheets["箱子贴单明细新版"].range("C1").options(transpose= True).value = list2

if __name__ =="__main__":
    main()