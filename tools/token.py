import os

from tools.folder_list import get_trans_paths
from tqdm import tqdm
import pandas as pd


def get_txt_lines(path):
    with open(path, 'r') as f:
        trans_list = f.readlines()
    return trans_list

def create_token_file(transcripts_paths = [], save_path = './'):

    # 전체 스크립트 모으기
    trans_list = []
    for transcripts_path in transcripts_paths:
        trans_list.extend(get_txt_lines(transcripts_path)) 

    # 전체 char 카운트
    char_dict = {}
    for line in trans_list:
        line = line.split(',')[1][:-1] # 스크립트 부분만 가져오기 + '\n' 제외
        if line == 'text': continue

        for char in line:
            # 모든 라인의 글자별 탐색
            try:
                # 이미 저장된 문자면 횟수 추가
                char_dict[char] += 1  
            except:
                # 처음 본 문자면 새로 추가
                char_dict[char] = 1  
                             
    sorted_char_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True) # 빈도수 기준 내림차순정렬

    # 정렬된 라벨
    label = {'id':[], 'char': [], 'freq': []}

    for idx, (ch, freq) in enumerate(sorted_char_dict):
        label['id'].append(idx + 3)
        label['char'].append(ch)
        label['freq'].append(freq)

    # csv로 저장
    os.makedirs(save_path, exist_ok=True)
    label_df = pd.DataFrame(label)
    file_path  = os.path.join(save_path, 'labels_for_chars.csv')
    label_df.to_csv(file_path, encoding='utf-8', index=False)

    return file_path