import sys
import time
#from ete2 import Tree
import myGraph
import spin
import encrypt
import csv
import math


# Set up input and output variables for the script
test1 = open("\\mnt\\S:\\Projects\\Homomorphic/Encryption\\HE_1.0\\vertex.csv", "r")
test2= open("\\mnt\\S:\\Projects\\Homomorphic/Encryption\\HE_1.0\\edge.csv", "r")

# Set up CSV reader and process the header
csvReader1 = csv.reader(test1)
csvReader2 = csv.reader(test2)
header1 = csvReader1.next()
header2 = csvReader2.next()
nodeIndex = header1.index("Node")
dat  = header1.index("Data")
xIndex = header1.index("X")
yIndex = header1.index("Y")
 
# Make an empty list
data = []
xList = []
yList = []
nodeList = []
meters = []
#Graph Initialization~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
g = myGraph.Graph()

class GraphInput:
    def input_data(self):
        for row in csvReader1:
            node = row[nodeIndex]
            datum  = row[dat]
            x    = row[xIndex]
            y    = row[yIndex]
            nodeList.append(node)
            data.append(int(datum))
            xList.append(int(x))
            yList.append(int(y))
            g.add_vertex(node,int(datum))

    def calc_data(self):
        main = dict( zip(nodeList,zip( xList, yList)))
        for row in csvReader2:
            Src,Des,Rest = row[:3] + [None]*(3 - len(row))
            result_list1 = list(main[Src])
            result_list2 = list(main[Des])
            ed = math.sqrt(((int(result_list1[0])-int(result_list2[0]))**2)+((int(result_list1[1])-int(result_list2[1]))**2))
            g.add_edge(Src,Des,int(ed))   

    def destinations(self):
        num = raw_input("Enter Number of destination : ")
        for i in range(int(num)):
            dest = raw_input("Enter destination : ")
            meters.append(str(dest))
        
        print '\n\n-------------------------------------------'
        print 'Meters are : %s' %(meters[::])
        print '-------------------------------------------\n\n'

    '''
	def tree(self):
        sys.stdout.write('\nTree data: Fetching ')
        spin.Spinner(' <--> Fetched!')
        t =  Tree("((a,(e,b,(d,c,(f)))));")
        print(" _______________________________________")
        print("|                                       |")
        print t
        print("|_______________________________________|")
        time.sleep(3)
	'''

    def implement(self):
        sys.stdout.write('\nGraph data: Fetching ')
        spin.Spinner(' <--> Fetched!')
        print(" _________________________________________")
        print('|                                         |')
        for v in g:
                for w in v.get_connections():
                        vid = v.get_id()
                        #print (type(vid))
                        wid = w.get_id()
                        #print (type(wid))
                        dat1 = v.get_data()
                        #print (type(dat1))
                        dat2 = w.get_data()
                        #print (type(dat2))
                        a = v.get_weight(w)
                        #print(type(a))
                        print ('| Src %s = %3d | Dest %s = %3d |'
                               ' Cost = %3d | '
                               % ( vid, dat1, wid, dat2,
                                   v.get_weight(w)))

        print("|_________________________________________|\n")
        time.sleep(3)
    def path(self):
        myGraph.dijkstra(g, g.get_vertex('a'))

    def encrypt(self):
        for t in meters:
            target  =       g.get_vertex(t)
            path    =       [t]
            myGraph.shortest(target, path)
            sys.stdout.write('Fetching shortest path for Meter %s ' % (t))
            spin.Spinner('... Done!')
            print 'The shortest path for %s : %s\n' %(t, path[::])
            encrypt.enc(path)
            print('\nDestination %s completed-------------------------\n'
                  %path[0])
        encrypt.setData()

    def srcData(self):
        sys.stdout.write('Fetching source data ')
        spin.Spinner('... Done!')
        target = g.get_vertex('a')
        print(target.get_data())
        
    def getData(self):
        target = g.get_vertex('a')
        target.set_data(cz)


if __name__ == '__main__':

    gi = GraphInput()
