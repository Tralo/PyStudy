#coding:utf-8

import pickle

class Bird(object):
    canFlying = True
    sonName = "egg"

bird = Bird()
#fr = open('a.txt','wb')
#pickStr = pickle.dump(bird,fr)
#fr.close()

fr = open('a.txt','rb')
pickleStr = pickle.load(fr)
print(pickleStr)
fr.close()



