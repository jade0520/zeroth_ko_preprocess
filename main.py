import os
import argparse

from tools.transcipts import create_transcipt_file
from tools.zeroth_token import create_token_file
from tools.folder_list import get_folder_paths
from tools.flac2wav import flac2wav

def _get_parser():
    ''' Get arguments parser '''
    parser = argparse.ArgumentParser(description='Zeroth Korean')
    parser.add_argument('-wav', action='store_true')
    parser.add_argument('--dataset_path', type=str,
                        default="../zeroth",
                        help='path of original dataset')
    parser.add_argument('--file_type', type=str, 
                        default="csv",
                        help='file type for transcripts ')
    parser.add_argument('--save_path', type=str,
                        default="./",
                        help='path to save')


    return parser


def create_wav_folders(dataset_path):
    folder_paths = get_folder_paths(dataset_path)
    wav_dir = os.path.join(dataset_path, "wav")

    for dir_ in  folder_paths:
        # 하위 폴더 구조 그대로 생성
        new_dir = os.path.join(wav_dir,dir_ )
        os.makedirs(new_dir, exist_ok=True)


def main():
    parser = _get_parser()
    args = parser.parse_args()

    audio_type = 'wav' if args.wav else 'flac'

    trans_path_list = create_transcipt_file(args.dataset_path, args.file_type, args.save_path, audio_type)
    print("transcripts and pathes are saved at ", trans_path_list)
    label_path = create_token_file(trans_path_list, args.save_path )
    print("token list file is saved at ", label_path)
    if args.wav: 
        create_wav_folders(args.dataset_path) # 폴더 생성 
        flac2wav(args.dataset_path) # wav 생성
         

if __name__ == '__main__':
    main()
