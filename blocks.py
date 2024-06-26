import hashlib
import json
import os

def get_hash(filename):
    blockchain_dir = os.curdir + '/blocks/'
    file = open(blockchain_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()

def check_integrity():
    blockchain_dir = os.curdir + '/blocks/'
    files = sorted([int(i) for i in os.listdir(blockchain_dir)])
    for file in files[1:]:
        ha = json.load(open(blockchain_dir + str(file)))['hash']
        prev_file = str(file -1)
        actual_hash = get_hash(prev_file)
        
        if ha == actual_hash:
            res = 'OK'
        else:
            res = 'Corrupted'
        
        print('Block {} is: {}'.format(prev_file, res))
    
    pass

def writeblock(who, amount, to_whom, prev_hash=''):
    blockchain_dir = os.curdir + '/blocks/'
    last_file = sorted([int(i) for i in os.listdir(blockchain_dir)])[-1]
    prev_hash = get_hash(str(last_file))
    file_name = str(last_file + 1)
    data = {'who': who,
            'amount': amount,
            'to_whom': to_whom,
            'hash': prev_hash}
    with open(blockchain_dir + file_name, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    writeblock(who='fedor', amount=5, to_whom='kseniya', prev_hash='')

if __name__ == '__main__':
    #main()
    check_integrity()
