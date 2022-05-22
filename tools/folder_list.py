import os

def get_folder_paths(dataset_path):
    # dataset_path 제외한 폴더 경로 
    folder_paths = []
    # train 
    sub_folder_path = os.path.join(dataset_path, 'train_data_01/003')
    sub_folder_list = os.listdir(sub_folder_path)
    for sub_folder_name in sub_folder_list:
        wav_folderPATH = os.path.join('train_data_01/003', sub_folder_name)   
        folder_paths.append(wav_folderPATH)

    # test
    sub_folder_path = os.path.join(dataset_path, 'test_data_01/003' )
    sub_folder_list = os.listdir(sub_folder_path)
    for sub_folder_name in sub_folder_list:
        wav_folderPATH = os.path.join('test_data_01/003', sub_folder_name)   
        folder_paths.append(wav_folderPATH)

    return folder_paths    

def get_flacs_paths(dataset_path):
    subpath_lists = {'train':[], 'test':[]}

    # train 
    sub_folder_path = os.path.join(dataset_path, 'train_data_01/003')
    sub_folder_list = os.listdir(sub_folder_path)
    for sub_folder_name in sub_folder_list:
        wav_folderPATH = os.path.join(sub_folder_path, sub_folder_name)
        wav_name_list = os.listdir(wav_folderPATH)     

        for wav_file_name in  wav_name_list:
            if wav_file_name.endswith(".txt"): continue
            subpath_lists['train'].append(os.path.join(wav_folderPATH, wav_file_name))

    # test
    sub_folder_path = os.path.join(dataset_path, 'test_data_01/003' )
    sub_folder_list = os.listdir(sub_folder_path)
    for sub_folder_name in sub_folder_list:
        wav_folderPATH = os.path.join(sub_folder_path, sub_folder_name)
        wav_name_list = os.listdir(wav_folderPATH)     

        for wav_file_name in  wav_name_list:
            if wav_file_name.endswith(".txt"): continue
            subpath_lists['test'].append(os.path.join(wav_folderPATH, wav_file_name))
            
    return subpath_lists    


def get_trans_paths(dataset_path):
    subpath_lists = {'train':[], 'test':[]}

    # train 
    sub_folder_path = os.path.join(dataset_path, 'train_data_01/003')
    sub_folder_list = os.listdir(sub_folder_path)
    for sub_folder_name in sub_folder_list:
        trans_file_name = sub_folder_name + '_003.trans.txt'
        subpath_lists['train'].append(os.path.join(sub_folder_path, sub_folder_name,trans_file_name ))

    # test
    sub_folder_path = os.path.join(dataset_path, 'test_data_01/003' )
    sub_folder_list = os.listdir(sub_folder_path)
    for sub_folder_name in sub_folder_list:
        trans_file_name = sub_folder_name + '_003.trans.txt'
        subpath_lists['test'].append(os.path.join(sub_folder_path, sub_folder_name,trans_file_name ))

    return subpath_lists    

