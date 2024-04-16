import os
import zipfile
import json
import torch
import glob
import csv
import pandas as pd
def extract_category_from_metadata(metadata_file):
    # 打开metadata文件并读取内容
    with open(metadata_file, 'r') as f:
        metadata = f.readlines()

    # 遍历每一行，查找包含Category字段的行
    for line in metadata:
        if line.startswith("Category"):
            # 如果找到Category字段，提取其值并返回
            category_value = line.split("=")[1].strip()  # 获取等号后面的值，并去除两边的空格
            return category_value

def load_labels(root_dir,language,type,suffix='AV_Aligned'):
    """Loads labels from the directory."""
    labels = {}
    files=[]
    # number of folder dont have a LandMarks
    for folder_name in os.listdir(root_dir):
        #
        if not f'_{language}_' in folder_name:
            continue
        folder_path = os.path.join(root_dir, folder_name)

        if os.path.isdir(folder_path):
            
            csv_file_list = glob.glob(folder_path + f'/*{language}*{type}_{suffix}.csv')
            # print(f'{csv_file_list=}')
            files.extend(csv_file_list)
            

        # print(f'loading {folder_name=}')
    print(f'{len(files)=}')
    
    for csv_file in files:
        file_name_ = os.path.basename(csv_file)
        # filename example: SSL_C2_S055_P109_VC1_004803_005542_Arousal_AV_Aligned
        file_name =file_name_.split('.')[0]
        key="_".join(file_name.split('_')[:-3])
        print(f'processing {file_name}')
        # key example : 'SSL_C2_S055_P109_VC1_004803_005542'
        # print(f'{key=}')
     
        label = []
      
        with open(csv_file, newline='') as csvfile:
            
            df = pd.read_csv(csv_file)
            label = df[type.lower()].values.reshape(-1, 1)
            labels[key]=label

    return labels

def test():
    # Example Usage
    root_dir = "/home/ubuntu/gxy/535proj/dataset/SEWAv02"

    labels=load_labels(root_dir,language='C2',type='Arousal',suffix='AV_Aligned')

    print(f'{len(labels)=}')
    ele=labels["SAH_C2_S047_P093_VC1_000538_001078"]
    print(f'{len(ele)=}')
    print(f'{type(ele)=}')
    print(f'{ele=}')

        
        
