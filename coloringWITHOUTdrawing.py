maxcolornumber = 50
class Node:
    def __init__(self):
        self.color = [True] * maxcolornumber
        self.incidentEdges = [None] * maxcolornumber
        self.variableList = []
    def assigncolor(self):
        for i in range(0,maxcolornumber):
            if self.color[i]:
                self.color[i] = False
                return(i)
    def exchangecolor(self, x,y):
        temp = self.color[x]
        self.color[x] = self.color[y]
        self.color[y] = temp
    def __del__(self):
        del self.color
        del self.incidentEdges
        del self.variableList

class Edge:
    def __init__(self,leftnode=0,rightnode=0,leftcolor=0,rightcolor=0):
        self.leftnode = leftnode
        self.rightnode = rightnode
        self.leftcolor = leftcolor
        self.rightcolor = rightcolor
        self.id = -1
        self.count = 0
        self.freeze = False
    def __str__(self):
        return str([self.leftnode,self.rightnode,self.leftcolor,self.rightcolor,self.id,self.freeze])
    def __repr__(self):
        return str([self.leftnode,self.rightnode,self.leftcolor,self.rightcolor,self.id,self.freeze])

class ExThread:
    def __init__(self,node):
        self.node = node
    def move(self):
        colorpairs=set()
        judge=False
        variableList=nodes[self.node].variableList[:]
        for edge1 in variableList:
            if edge1.leftcolor==edge1.rightcolor or edge1.freeze:
                continue
            if(self.node < n):
                    edge2=nodes[self.node].incidentEdges[edge1.rightcolor]
                    if edge2 is None:
                        nodes[self.node].exchangecolor(edge1.leftcolor,edge1.rightcolor)
                        nodes[self.node].incidentEdges[edge1.rightcolor]=edge1
                        nodes[self.node].incidentEdges[edge1.leftcolor]=None
                        edge1.leftcolor=edge1.rightcolor
                        nodes[self.node].variableList.remove(edge1)
                        nodes[edge1.rightnode].variableList.remove(edge1)
                        edge1.id=-1
                        edge1.freeze=True
                        judge=True
                        continue
                    elif edge1.leftcolor*maxcolornumber+edge2.leftcolor not in colorpairs and edge2.rightcolor==edge1.leftcolor:
                        nodes[self.node].incidentEdges[edge2.leftcolor]=edge1
                        nodes[self.node].incidentEdges[edge1.leftcolor]=edge2
                        temp=edge1.leftcolor
                        edge1.leftcolor=edge2.leftcolor
                        edge2.leftcolor=temp
                        edge1.id=-1
                        edge2.id=-1
                        edge1.freeze=True
                        edge2.freeze=True
                        nodes[self.node].variableList.remove(edge1)
                        nodes[self.node].variableList.remove(edge2)
                        nodes[edge1.rightnode].variableList.remove(edge1)
                        nodes[edge2.rightnode].variableList.remove(edge2)
                        colorpairs.add(edge2.leftcolor*maxcolornumber+edge1.leftcolor)
                        judge=True
                        continue
                    elif edge1.leftcolor*maxcolornumber+edge2.leftcolor not in colorpairs and edge2.rightcolor!=edge1.rightcolor:
                        nodes[self.node].incidentEdges[edge2.leftcolor]=edge1
                        nodes[self.node].incidentEdges[edge1.leftcolor]=edge2
                        temp=edge1.leftcolor
                        edge1.leftcolor=edge2.leftcolor
                        edge2.leftcolor=temp
                        edge1.id=-1
                        edge2.id=-1
                        edge1.count=0
                        edge2.count=0
                        edge1.freeze=True
                        edge2.freeze=False
                        nodes[self.node].variableList.remove(edge1)
                        nodes[edge1.rightnode].variableList.remove(edge1)
                        colorpairs.add(edge2.leftcolor*maxcolornumber+edge1.leftcolor)
                        judge=True
                        continue
                    elif edge1.leftcolor*maxcolornumber+edge2.leftcolor not in colorpairs and edge2.rightcolor==edge1.rightcolor:
                        if edge1.id==edge2.leftnode and edge1.id==edge1.leftnode:
                            edge1.count+=1
                            if edge1.count>=2:
                                continue
                        elif edge1.id<edge2.leftnode:
                            edge1.id=edge2.leftnode
                        nodes[self.node].incidentEdges[edge2.leftcolor]=edge1
                        nodes[self.node].incidentEdges[edge1.leftcolor]=edge2
                        temp=edge1.leftcolor
                        edge1.leftcolor=edge2.leftcolor
                        edge2.leftcolor=temp
                        edge2.id=edge1.id
                        edge1.id=-1
                        edge1.freeze=True
                        edge2.freeze=False
                        nodes[self.node].variableList.remove(edge1)
                        nodes[self.node].variableList.append(edge2)
                        nodes[edge1.rightnode].variableList.remove(edge1)
                        nodes[edge2.rightnode].variableList.append(edge2)
                        colorpairs.add(edge2.leftcolor*maxcolornumber+edge1.leftcolor)
                        judge=True
                        continue
            else:
                    edge2=nodes[self.node].incidentEdges[edge1.leftcolor]
                    if edge2 is None:
                        nodes[self.node].exchangecolor(edge1.leftcolor,edge1.rightcolor)
                        nodes[self.node].incidentEdges[edge1.leftcolor]=edge1
                        nodes[self.node].incidentEdges[edge1.rightcolor]=None
                        edge1.rightcolor=edge1.leftcolor
                        nodes[self.node].variableList.remove(edge1)
                        nodes[edge1.leftnode].variableList.remove(edge1)
                        edge1.id=-1
                        edge1.freeze=True
                        judge=True
                        continue
                    elif edge1.rightcolor*maxcolornumber+edge2.rightcolor not in colorpairs and edge2.leftcolor==edge1.rightcolor:
                        nodes[self.node].incidentEdges[edge2.rightcolor]=edge1
                        nodes[self.node].incidentEdges[edge1.rightcolor]=edge2
                        temp=edge1.rightcolor
                        edge1.rightcolor=edge2.rightcolor
                        edge2.rightcolor=temp
                        edge1.id=-1
                        edge2.id=-1
                        edge1.freeze=True
                        edge2.freeze=True
                        nodes[self.node].variableList.remove(edge1)
                        nodes[self.node].variableList.remove(edge2)
                        nodes[edge1.leftnode].variableList.remove(edge1)
                        nodes[edge2.leftnode].variableList.remove(edge2)
                        colorpairs.add(edge2.rightcolor*maxcolornumber+edge1.rightcolor)
                        judge=True
                        continue
                    elif edge1.rightcolor*maxcolornumber+edge2.rightcolor not in colorpairs and edge2.leftcolor!=edge1.leftcolor:
                        nodes[self.node].incidentEdges[edge2.rightcolor]=edge1
                        nodes[self.node].incidentEdges[edge1.rightcolor]=edge2
                        temp=edge1.rightcolor
                        edge1.rightcolor=edge2.rightcolor
                        edge2.rightcolor=temp
                        edge1.id=-1
                        edge2.id=-1
                        edge1.freeze=True
                        edge2.freeze=False
                        edge1.count=0
                        edge2.count=0
                        nodes[self.node].variableList.remove(edge1)
                        nodes[edge1.leftnode].variableList.remove(edge1)
                        colorpairs.add(edge2.rightcolor*maxcolornumber+edge1.rightcolor)
                        judge=True
                        continue
                    elif edge1.rightcolor*maxcolornumber+edge2.rightcolor not in colorpairs and edge2.leftcolor==edge1.leftcolor:
                        #if edge1.id==edge2.leftnode and edge1.id==edge1.leftnode:
                        #    continue
                        #elif edge1.id<edge2.leftnode:
                        #    edge1.id=edge2.leftnode
                        nodes[self.node].incidentEdges[edge2.rightcolor]=edge1
                        nodes[self.node].incidentEdges[edge1.rightcolor]=edge2
                        temp=edge1.rightcolor
                        edge1.rightcolor=edge2.rightcolor
                        edge2.rightcolor=temp
                        edge2.id=edge1.id
                        edge1.id=-1
                        edge1.freeze=True
                        edge2.freeze=False
                        nodes[self.node].variableList.remove(edge1)
                        nodes[self.node].variableList.append(edge2)
                        nodes[edge1.leftnode].variableList.remove(edge1)
                        nodes[edge2.leftnode].variableList.append(edge2)
                        colorpairs.add(edge2.rightcolor*maxcolornumber+edge1.rightcolor)
                        judge=True
                        continue
        return judge

import random,time,os
def RequestGenerator(n):
    a = []
    random.seed()
    for i in range(0,n):
        a.append(random.randint(0,n)-1)
    return a


#main function
n = 6
initialEdgesFile='initialEdges'
slots = 3
step=0
nodes=[]
AdjacencyList = []
initialEdges = []
data = {}

while True:
    step+=1
    print('Begin '+str(step)+' try')
    del nodes
    nodes = [Node() for each in range(n*2)]
    del AdjacencyList
    del initialEdges
    AdjacencyList = []
    initialEdges = []
    if os.path.isfile(initialEdgesFile):
        break
    else:
        for slot in range(slots):
            request = RequestGenerator(n)
            for i in range(0,len(request)):
                if request[i]!=-1:
                    edge=Edge(i,request[i]+n,nodes[i].assigncolor(),nodes[request[i]+n].assigncolor())
                    AdjacencyList.append(edge)
                    initialEdges.append(str(edge))
                    nodes[i].incidentEdges[edge.leftcolor]=edge
                    nodes[request[i]+n].incidentEdges[edge.rightcolor]=edge
                    if(edge.leftcolor!=edge.rightcolor):
                        nodes[i].variableList.append(edge)
                        nodes[request[i]+n].variableList.append(edge)
    
    ExchangeThreads1=[]
    for i in range(n):
        ExchangeThreads1.append(ExThread(i))
    ExchangeThreads2=[]
    for i in range(n):
        ExchangeThreads2.append(ExThread(i+n))
            
    judge=True
    count=0
    i=0
    while(judge):
        count+=1
        i+=1
        judge=False
        for thread in ExchangeThreads2:
            #print thread.node
            if(thread.move()):
                judge=True
        for thread in ExchangeThreads1:
            #print thread.node
            if(thread.move()):
                judge=True
        if i>=n or not judge:
            colorUsable=[True]*maxcolornumber
            for edge in AdjacencyList:
                if edge.leftcolor!=edge.rightcolor:
                    judge=True
                    if colorUsable[edge.leftcolor] and colorUsable[edge.rightcolor]:
                        edge.freeze=False
                        colorUsable[edge.leftcolor]=False
                        colorUsable[edge.rightcolor]=False
                    else:
                        edge.freeze=True
            i=0
        if count>(2*n)**2*2:
            #Storage the initial Condition for regenerate the deadlock
            f=open(initialEdgesFile,'w')
            for edge in initialEdges:
                f.write(str(edge)+'\n')
            f.close()
            print "Deadlock FOUND!!!"
            break
    if len(AdjacencyList) in data:
        if count*2 in data[len(AdjacencyList)]:
            data[len(AdjacencyList)][count*2]+=1
        else:
            data[len(AdjacencyList)][count*2]=1
    else:
        data[len(AdjacencyList)]={}
        if count*2 in data[len(AdjacencyList)]:
            data[len(AdjacencyList)][count*2]+=1
        else:
            data[len(AdjacencyList)][count*2]=1
    if step>=10000000:
        import json
        datafile=open("data",'w')
        print>>datafile, json.dumps(data,sort_keys=True,indent=4)
        datafile.close()
        break

raw_input()
