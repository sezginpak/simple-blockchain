# Simple-Blockchain

Simple-Blockchain is a Python library for dealing with word pluralization.

## Installation

Source code

```bash
git clone https://github.com/sezginpak/simple-blockchain.git
```

## Usage

```python
from simpleBlockchain import BlockChain, Block

chain = BlockChain()
chain.addBlock(Block([1,2,3]))
chain.addBlock(Block([4,5,6]))
chain.addBlock(Block([7,8,9]))
chain.addBlock(Block([10,11,12]))

print(chain.chainValid())

for i in range(len(chain.chain)):
    print(i.data)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
