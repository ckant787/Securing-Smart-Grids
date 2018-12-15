#!/usr/bin/env python2.7
'''
    A spanning tree rooting at the collector device.            /
    Each node collects
    data from its children, aggregates from  /
    its own data and sends the intermediate result to the parent/
    node.                                                       /
'''

import sys
import spin
import feed
import encrypt
import spin

gi = feed.GraphInput()
gi.input_data()
gi.calc_data()
sys.stdout.write('\nInitializing ')
spin.Spinner(' : Completed!')
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<" Demo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

condition = True
while(condition):

    print('\n\n==================================Commands==================================')
    print('To see tree                   "t   "')
    print('To start                      "s   "')
    print('To print destinations         "des "')
    print('To encrypt                    "e   "')
    print('To see encrypted list enter   "el  "')
    print('To see encrypted result enter "er  "')
    print('To see collector data enter   "cd  "')
    print('To decrypt result enter       "d   "')
    print('To quit press                 "q   "')
    print('==================================Commands==================================\n\n')

    x = raw_input("\nInsert value and press Enter : ")
    if(x == 'des'):
        gi.destinations()

    elif(x == 's'):
        gi.implement()
        gi.path()

    elif(x == 'e'):
        gi.encrypt()
        
    elif(x == 'el'):
        encrypt.getList()

    elif(x == 'er'):
        encrypt.encRes()

    elif(x == 'cd'):
        gi.srcData()

    elif(x == 'd'):
        encrypt.dec()

    elif(x == 'q'):
        condition = False
    
    else:
        print 'No valid input'

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<" Demo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
