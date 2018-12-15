import sys
from paillier import *
import spin
import feed

enc_list=[]
priv, pub = generate_keypair(512)
cz = encrypt(pub, 0)

def enc(path):
    for t in path[:-1]:
        global cz
        target  =       feed.g.get_vertex(t)                                 #Applying Encryption on shortest path on defined node
        dat=target.get_data()
        cx      =       encrypt(pub, dat)
        enc_list.append(cx)                                             #Creating Encrypted List
        sys.stdout.write('Encrypting node %s '%(t))
        spin.Spinner('<--> Encrypted!')
        cz      =       e_add(pub, cz, cx)
        #print(enc_list[::])                                            #Encrypted List Preview

def setData():
    target = feed.g.get_vertex('a')
    target.set_data(cz)

def encRes():
    sys.stdout.write('Fetching results ')
    spin.Spinner('... Done!')
    print('\n#   %s'%cz)

def dec():
    z = decrypt(priv,pub,cz)
    sys.stdout.write("\nDecrypting ")
    spin.Spinner('<--> Decrypted : # %s'%z)

def getList():
    print(enc_list[::])
