import hashlib
from datetime import datetime, date

class Block(object):

    def __init__(self, data, previousHash=''):

        """ Data Important """

        self.data = data
        self.timestamp = datetime.now()
        self.previousHash = previousHash.encode('utf-8')
        self.hash = self.addHash()

    def addHash(self):
        block_hash = hashlib.sha256()
        data = '-'.join(map(str, self.data))
        if type(self.previousHash)==type(''):
            upda = data + '-dataEnd-' + self.timestamp.isoformat() + self.previousHash
            block_hash.update(upda.encode('utf-8'))
        else:
            upda = data + '-dataEnd-' + self.timestamp.isoformat() + str(self.previousHash, 'utf-8')
            block_hash.update(upda.encode('utf-8'))
        return block_hash.hexdigest()

class BlockChain(object):
    def __init__(self):
        self.chain = [self.genesisBlock()]
    def genesisBlock(self):
        return Block([], '000')
    def lastChain(self):
        return self.chain[-1]
    def addBlock(self,newblock):
        newblock.previousHash = self.lastChain().hash
        newblock.hash = newblock.addHash()
        self.chain.append(newblock)
    def chainValid(self):
        for index in range(1, len(self.chain)):
            block = self.chain[index]
            previous_block = self.chain[index-1]

            if block.hash != block.addHash():
                return False
            elif block.previousHash != previous_block.hash:
                return False
        return True
