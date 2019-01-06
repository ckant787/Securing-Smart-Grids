# Securing Smart Grid System Using Homomorphic Encryption
In the digital world we are living in; the conventional power system has to meet the demands of a digital society. Thus, upgradation was required. This included smart meters. In this project, we emphasized on the security of data forwarded by smart meters. Data over a network has a high risk of being hacked and modified by attackers. Pure Paillier Homomorphic Encryption is used to encrypt data at each node. In this way, our approach supports efficient data aggregation while fully protecting user privacy. It is helpful for smart grids with repetitive routine data aggregation tasks.

### Main.py
##### !/usr/bin/env python2.7.11
> A spanning tree rooting at the collector device.Each node collects data from its children, aggregates from its own data and sends the intermediate result to the parent node.         

```python
import sys
import spin
import feed
import encrypt
import csv

# Creating the network by the help og graph
gi = feed.GraphInput()

condition = True
while(condition):
    print('\n\n==============List of Operations=================')
    print('To see tree                   "t   "')
    print('To start                      "s   "')
    print('To print destinations         "des "')
    print('To encrypt                    "e   "')
    print('To see encrypted list enter   "el  "')
    print('To see encrypted result enter "er  "')
    print('To see collector data enter   "cd  "')
    print('To decrypt result enter       "d   "')
    print('To quit press                 "q   "')
    
    print('==================Operations Completed===================)

```
Main.py implements following predefined modules such like “sys”, “csv” and user defined modules such as “spin”, “feed”, “encrypt”. Further modules like “mygraph” and “paillier” are used within defined function to create a minimum spanning tree and provide encryption at node data.

#### List of Functions
1. ```gi.tree()```: It provides visual tree representation of input data in the form of minimum rooted spanning tree where root is the collector node and all the other nodes are either substations or smart meters.

1. ```gi.destinations()```: It provides list of all the nodes set as destination in the GraphInput().
1. ```gi.implement()```: It provides the input to MyGraph and create a minimum spanning tree on the basis of input provided in csv file.
1. ```gi.path()```: Dijkstra’s path is calculated providing the shortest path between the source and the destination.
1. ```gi.encrypt()```: Encrypt function is called to perform encryption on received data by each node and run simultaneously.
1. ```encrypt.getList()```: Encrypted data at each node is stored in a list 
1. ```encrypt.encRes()```: Cummulutative result is encrypted under this function using Paillier Encryption.
1. ```gi.srcData()```: It provides fetching of data at collector node.
1. ```encrypt.dec()```: It decrypt the encrypted data using public and private key.

### Demo
![Commands](/MD/cmd.png)
![Tree](/MD/tree.png)
![Destination](/MD/des.png)
![Encrypt](/MD/encrypt.png)
![Encrypted List](/MD/enList.png)
![Encrypted Result](/MD/enRes.png)
![Decrypt](/MD/decrypt.png)

### Conclusion
Under this project, Aggregation is performed in a distributed manner accordance to the aggregation tree – each node collects data from its children, aggregates them with its own data, and sends the intermediate result to the parent node. Homomorphic Encryption is applied to protect the privacy of data. Aggregated data is made secure on the aggregation path and ensured that results are not revealed to smart meters while being traversed on a network. This module does not cover user maliciously forging their own data to manipulate aggregation result. Thus ensuring privacy control from foreign attacks only. Surely better techniques are coming to check for forged data and recovering the loses. 

### [Report](/REPORT/Homomorphic Encryption.docx)
