import os

def get_sub_folders_paths(dataset_path):
    subpath_lists = {'train':[], 'test':[]}

    # train 
    sub_folder_path = os.path.join(dataset_path, 'train_data_01/003')
    sub_folder_list = os.listdir(sub_folder_path)
    for sub_folder_name in sub_folder_list:
        subpath_lists['train'].append( os.path.join(sub_folder_path, sub_folder_name))

    # test
    sub_folder_path = os.path.join(dataset_path, 'test_data_01/003' )
    sub_folder_list = os.listdir(sub_folder_path)
    for sub_folder_name in sub_folder_list:
        subpath_lists['test'].append( os.path.join(sub_folder_path, sub_folder_name))

    return subpath_lists    


def get_trans_paths(dataset_path):
    subpath_lists = {'train':[], 'test':[]}

    # train 
    sub_folder_path = os.path.join(dataset_path, 'train_data_01/003')
    sub_folder_list = os.listdir(sub_folder_path)
    for sub_folder_name in sub_folder_list:
        trans_file_name = sub_folder_name + '_003.trans.txt'
        subpath_lists['train'].append(os.path.join(sub_folder_path, sub_folder_name, trans_file_name ))

    # test
    sub_folder_path = os.path.join(dataset_path, 'test_data_01/003' )
    sub_folder_list = os.listdir(sub_folder_path)
    for sub_folder_name in sub_folder_list:
        trans_file_name = sub_folder_name + '_003.trans.txt'
        subpath_lists['test'].append(os.path.join(sub_folder_path, sub_folder_name, trans_file_name ))

    return subpath_lists    

