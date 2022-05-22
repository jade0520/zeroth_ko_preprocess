import os
import argparse

from tools.transcipts import create_transcipt_file
from tools.token import create_token_file

def _get_parser():
    ''' Get arguments parser '''
    parser = argparse.ArgumentParser(description='Zeroth Korean')
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


def main():
    parser = _get_parser()
    args = parser.parse_args()

    trans_path_list = create_transcipt_file(args.dataset_path, args.file_type, args.save_path)
    print("transcripts and pathes are saved at ", trans_path_list)
    label_path = create_token_file(trans_path_list, args.save_path )
    print("token list file is saved at ", label_path)

if __name__ == '__main__':
    main()
