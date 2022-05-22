import os

from tools.folder_list import get_trans_paths
from tqdm import tqdm
import csv

def create_transcipt_file(dataset_path, path_list_file_type, save_path):

    # wav와 script가 있는 경로 목록
    transPATH_dict = get_trans_paths(dataset_path)

    # csv
    if path_list_file_type == "csv": 
        train_file_path = creat_csv(transPATH_dict, save_path, 'train')
        test_file_path = creat_csv(transPATH_dict, save_path, 'test')

        return train_file_path, test_file_path

    elif path_list_file_type == "txt": 
        train_file_path = creat_txt(transPATH_dict, save_path, 'train')
        test_file_path = creat_txt(transPATH_dict, save_path, 'test')  
        return train_file_path, test_file_path

    else :
        print("Invalid file type for transcipts")

        return None

def creat_txt(transPATH_dict, save_path, dataset = 'train' ):
    file_path = os.path.join(save_path, dataset+'_transcripts.txt')
    with open(file_path, 'w') as f:
        # 경로 및 transcript pair 저장 파일 쓰기 준비
        f.write('file_name,text\n')
        for subpath in tqdm(transPATH_dict[dataset], desc='Integrating...'):
            # sub folder 마다의 transcipt 파일 불러와서 저장
            tran_list = get_txt_lines(subpath)
            for line in tran_list:
                f.write(f'{os.path.join(os.path.split(subpath)[0], line[:12])},{line[13:-1]}\n') # 스크립트에서 '\n' 빼기 위해 -1
    return file_path

def creat_csv(transPATH_dict, save_path,  dataset = 'train' ):
    file_path = os.path.join(save_path, dataset+'_transcripts.csv')
    with open(file_path, 'w', newline = '') as f:
        # 경로 및 transcript pair 저장 파일 쓰기 준비
        wr = csv.writer(f)
        wr.writerow(['file_name','text'])

        for subpath in tqdm(transPATH_dict[dataset], desc='Integrating...'):
            # sub folder 마다의 transcipt 파일 불러와서 저장
            tran_list = get_txt_lines(subpath)
            for line in tran_list:
                wr.writerow([f'{os.path.join(os.path.split(subpath)[0], line[:12])}',f'{line[13:-1]}']) # 스크립트에서 '\n' 빼기 위해 -1

    return file_path

def get_txt_lines(path):
    with open(path, 'r') as f:
        tran_list = f.readlines()
    return tran_list