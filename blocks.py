import hashlib
import json
import os

def writeblock(who, amount, to_whom, prev_hash=''):
    blockchain_dir = os.curdir + '/SimplyBlockchain/SimplyBlockchain/blocks/'
    file = str(sorted([int(i) for i in os.listdir(blockchain_dir)])[-1]+1)
    data = {'who': who,
            'amount': amount,
            'to_whom': to_whom,
            'hash': prev_hash}
    with open(blockchain_dir + file, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    writeblock(who='ivan', amount=10, to_whom='fedor', prev_hash='123')

if __name__ == '__main__':
    main()
