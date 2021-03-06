# Zeroth 데이터 셋 전처리 
음성인식을 위해 zeorth 한국어 데이터 셋을 전처리해주는 코드 입니다. 사용은 아래를 참고해주세요.

## Reference
sooftware님의 [ksponspeech](https://github.com/sooftware/ksponspeech)를 참고하여 작성하였습니다.  
감사합니다.

## 데이터 셋 준비

1. openslr 에서 데이터 셋 가져오기 (https://www.openslr.org/40/)  
```
wget https://www.openslr.org/resources/40/zeroth_korean.tar.gz  
```
2. 압푹 풀기 
```
mkdir ./zeroth/ # 폴더 생성
tar -xvf ./zeroth_korean.tar.gz -C ./zeroth/
``` 
3. setting   
    3-1. 코드 준비  
    ```
    git clone
    cd ./zeroth_ko_preprocess
    ```
    3-2. 환경 준비 
    ```
    pip install pandas 
    pip install tqdm
    pip install soundfile
    ```
    or
    ```
    pip install -r requirements.txt
    ``` 

4. 데이터 전처리  
- run.sh에서 경로 설정 필요
```
bash run.sh
```

## 결과 
- (wav file 생성)
    ```
    zeroth
    ├── test_data_01
    ├── train_data_01
    └── wav
        ├── test_data_01
        └── train_data_01
    ```
- labels_for_chars.csv
    ```
    id,char,freq
    3, ,306930
    4,이,35483
    ```
- train_transcripts.csv (wav로 변환)
    ```
    file_name,text
    /wav/train_data_01/003/190/190_003_0002.wav,이 사고로 크게 다친 서씨가 인근 병원으로 옮겨졌으나 의식이 없는 상태다
    /wav/train_data_01/003/190/190_003_0023.wav,힐리스의 매력은 신발 밑창에 바퀴가 달려 있어 인라인스케이트처럼 미끄러지듯 달릴 수 있다는 점이다
    ```  

##  기존 Zeoroth 데이터 셋 구조 
zeroth의 훈련 및 시험 데이터는 아래와 같은 경로로 저장되어 있다.  
음원은 flac 확장자를 사용하며, 각 음원에 대한 스크립트는 폴더에 하나씩 있는 .trans.txt에 한번에 저장되어 있다.
```
zeroth
├── test_data_01
│   └──  003
|       ├── 104
│       ├── ...
│       └── 149
|           ├── 149_003_0057.flac
|           ├── ...
|           ├── 149_003_2839.flac
│           └── 149_003.trans.txt
├── train_data_01
│   └──  003
|       ├── 106
│       ├── ...
│       └── 218
|           ├── 218_003_0005.flac
|           ├── ...
|           ├── 218_003_2997.flac
│           └── 218_003.trans.txt
└── ...

```
### .trans.txt 구조
``` 
218_003_0005 앞으로 계속 북진하면서 정오 무렵엔 동해상으로 올라와 오후 두 시를 전후해선 부산 남동쪽 백 쉰 킬로미터 부근 해상까지 북상하겠습니다
218_003_0015 한술 더 떠 여당 의원들은 국회 예결특위에서 강신명 경찰청장을 압박 신변보호 조치를 하겠다는 답변까지 얻어냈습니다
```

## 코드 동작 원리
1. 폴더 별로 있는 스크립트 파일을 train/test로만 나누어 통합한다. (csv/txt)
2. 전처리가 된 깨끗한 스크립트이므로, 다른 전처리는 하지 않는다.
3. 빈도 순으로 토큰 생성한다. (csv/txt)
4. flac file을 wav file로 바꾼다.
