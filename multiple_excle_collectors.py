"""
#主文件夹
    #sheet1name
        #name1.xlsx
        #name2.xlsx
        #name3.xlsx
    #sheet2name
        #name1.xlsx
        #name2.xlsx
        #name3.xlsx
#workbook
    sheet1name
    sheet2name
这个工具的作用就是  将和sheetname名字相同的1个文件夹中的所有的excel文件合并成一个pandas件，并将数据写入到对应的sheet中。
"""
import os
import xlwings as xw
import pandas as pd
path  = f"{os.path.split(os.path.realpath(__file__))[0]}/"



def  readsheet_to_sheet(workbook, sheetname):
    '''读取sheetname对应的文件夹中的所有excel文件，并将数据合并到一个pandas数据框中'''
    folder_path = path + sheetname
    all_df = pd.DataFrame()
    for filename in os.listdir(folder_path):
        if filename.endswith('.xlsx'):
            file_path = os.path.join(folder_path, filename)
            print(f"Reading sheets from {file_path}:")
            
            with xw.Book(file_path) as wb:
                for sheet in wb.sheets:
                    # 读取工作表数据并跳过第一行
                    df = sheet.used_range.options(pd.DataFrame, index=False, header=1).value
                    
                    # 打印工作表名称和数据
                    print(f"\nSheet: {sheet.name}")
                    print(df)
                   
                    all_df = pd.concat([all_df,df],ignore_index=True)

    workbook.sheets[sheetname].range("A2").options(header = False , index = False).value  = all_df


def main(book_name):
    ''' 打开excel文件'''
    wb1 = xw.books(book_name)

        ##########          #这里做了切片, 因为我前面2个工作表是不需要收集的
    shop_list = [x for x in wb1.sheet_names][3:]

    for i in shop_list:
        readsheet_to_sheet(workbook=wb1,sheetname=i)
    

if __name__ == "__main__":
    main("JD优惠券百补各店铺承担比例信息截止2024年7月.xlsx")