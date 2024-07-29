'''一个拆分文件工具'''
import os
import shutil
from tkinter import messagebox

def split_files(input_folder:str, output_folder:str,max_files_num:int=20,mode:str='move')->None:
    '''将一个文件夹中的文件分割为多个文件夹，默认每个文件夹最多20个文件,拆分模式为移动''' 
    def delete_contents(directory):
        '''确保目录存在'''
        if os.path.exists(directory):
            # 遍历目录中的所有文件和文件夹
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                # 如果是文件，则直接删除
                if os.path.isfile(item_path):
                    os.remove(item_path)
                # 如果是文件夹，则递归调用删除其内容
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
        else:
            messagebox.showinfo("info",f"Directory '{directory}' does not exist.")
            print(f"Directory '{directory}' does not exist.")

    delete_contents(output_folder)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # 获取输入文件夹中的所有文件
    files = os.listdir(input_folder)
    # 计数器
    count = 0
    folder_count = 1
    # 遍历文件
    if files is None or len(files) == 0:
        messagebox.showinfo("info","碗里没有余粮了")
    else:
        for file in files:
            # 输入文件路径
            file_path = os.path.join(input_folder, file)
            # 输出文件夹路径
            output_subfolder = os.path.join(output_folder, f'拆分文件夹_{folder_count}')
            # 如果输出文件夹不存在则创建
            if not os.path.exists(output_subfolder):
                os.makedirs(output_subfolder)
            if mode == 'copy':
                #复制文件到输出文件夹
                shutil.copy(file_path, output_subfolder)
            elif mode == "move":
                # 移动文件到输出文件夹
                shutil.move(file_path, output_subfolder)
            count += 1
            # 如果达到20个文件，重置计数器，并创建新的输出文件夹
            if count == max_files_num:
                count = 0
                folder_count += 1
        print(f'共将{len(files)}个文件分割为\n{folder_count}个文件夹')

# 用法示例

if "__main__" == __name__:
    split_files(
        r"D:\配置生成\主图配置单", 
        r"D:\配置生成\导出",
        max_files_num=20,
        mode='move'
    )
