import os
blockchain_dir = os.curdir + '/SimplyBlockchain/blocks/'
print(blockchain_dir)
#print('C:\Users\AEDeryazhentsev/MyDocuments/MyPython/SimplyBlockchain/blocks/1.json')
with open(blockchain_dir + '1.json', 'r') as file:
    text = file.read()
print(text)