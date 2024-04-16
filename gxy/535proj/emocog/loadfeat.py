import csv
import glob
import os
import pandas as pd


def load_FeatfromCSV(folder_path,lang,featrue=None):
    dataset={}

    # 获取符合条件的csv文件名列表
    # csv_files = glob.glob(folder_path + f'/*_{lang}_*.csv')
    csv_files = glob.glob(folder_path + f'/*_{lang}_*.csv')
    print(f'{len(csv_files)=}')
    

    # 循环读取每个csv文件
    for csv_file in csv_files:
        file_name_ = os.path.basename(csv_file).split('.')[0]
        df = pd.read_csv(csv_file,header=0)
        
        data_array = df.values

        dataset[file_name_]=data_array
    
    return dataset






def split_train_val(dataset):
    """Splits the data into training and validation sets."""

    train_data = {}
    val_data = {}

    split_index = int(len(list((dataset.keys()))) * 0.8)
    # print(f'{split_index=}')

    # 训练集数据
    for idx, (folder_name, feats) in enumerate(dataset.items()):
        if idx < split_index:
            train_data[folder_name] = feats
        else:
            val_data[folder_name] = feats


    # print(f'{len(train_data)=}')
    # print(f'Length of the first element in train_data: {len(list(train_data.values())[0])}')


    return train_data, val_data



def split_train_val_cul(dataset,inils,cul):
    """Splits the data into training and validation sets."""
    culdata={}
    for it in inils:
        culdata[it]={}
       # 训练集数据
        for idx, (folder_name, landmarks_list) in enumerate(dataset[it].items()):
            if folder_name.split('_')[1]==cul:
                culdata[it][folder_name]=landmarks_list
        
        print(f'{len(culdata[it])=}')
        print(f'{list((culdata[it].keys()))[0]=}')
        
        
    train_data = {}
    val_data = {}
    for it in inils:
        
        
        split_index = int(len(list((culdata[it].keys()))) * 0.8)
        # print(f'{split_index=}')
    
        # 训练集数据
        for idx, (folder_name, landmarks_list) in enumerate(culdata[it].items()):
            if idx < split_index:
                train_data[folder_name] = landmarks_list
            else:
                val_data[folder_name] = landmarks_list
    
    
    print(f'{len(train_data)=}')
    print(f'Length of the first element in train_data: {len(list(train_data.values())[0])}')


    return train_data, val_data


def test():
    # 定义文件夹路径
    root='/home/ubuntu/gxy/535proj/FacialLMextraction/extractedLM/AUs'
    dataset=load_FeatfromCSV(root,'C1')
    print(f'{len(dataset)=}')
    keys=dataset.keys()
    print(f'{keys=}')
    print(f'{dataset[list(keys)[0]]=}')
    traind,vald=split_train_val(dataset)
    
    print(f'{len(traind)=}')
    print(f'{len(vald)=}')
    
    
    
    
# test()