import os
import soundfile as sf
from tqdm import tqdm
from tools.folder_list import get_flacs_paths


def flac2wav(dataset_path):
    flac_paths_dict = get_flacs_paths(dataset_path)

    for flac_path in tqdm(flac_paths_dict['train'], desc='train flac to wav ...'):
        flac_path_list = flac_path.split('/')
        flac_path_list.insert(2, "wav")
        wav_path = os.path.join(*flac_path_list)[:-4] + "wav"
        a = sf.read(flac_path)
        sf.write(wav_path,a[0],a[1],format="WAV", endian = "LITTLE", subtype="PCM_16")

    for flac_path in tqdm(flac_paths_dict['test'], desc='test flac to wav ...'):
        flac_path_list = flac_path.split('/')
        flac_path_list.insert(2, "wav")
        wav_path = os.path.join(*flac_path_list)[:-4] + "wav"
        a = sf.read(flac_path)
        sf.write(wav_path,a[0],a[1],format="WAV", endian = "LITTLE", subtype="PCM_16")
