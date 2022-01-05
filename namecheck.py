from web3 import Web3
from ens import ENS
import string

infuraProjectId = 'PUT_INFURA_PROJECT_ID_HERE'
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/' + infuraProjectId))
ns = ENS.fromWeb3(w3)

freeList = []

for firstLetter in string.ascii_lowercase:
    for secondLetter in string.ascii_lowercase:
        for thirdLetter in string.ascii_lowercase:
            ensAddress = firstLetter + secondLetter + thirdLetter + '.eth'
            owner = ns.owner(ensAddress)
            if owner == '0x0000000000000000000000000000000000000000':
                freeList.append(ensAddress)
                print(ensAddress + " has owner " + owner)

with open('freeList.txt', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(freeList))