maxcolornumber = 20
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

class Edge:
    def __init__(self,leftnode=0,rightnode=0,leftcolor=0,rightcolor=0):
        self.leftnode = leftnode
        self.rightnode = rightnode
        self.leftcolor = leftcolor
        self.rightcolor = rightcolor
        self.id = -1
        self.count = 0
        
    def __str__(self):
        return str([self.leftnode,self.rightnode,self.leftcolor,self.rightcolor,self.id])
    def __repr__(self):
        return str([self.leftnode,self.rightnode,self.leftcolor,self.rightcolor,self.id])

class ExThread:
    def __init__(self,node):
        self.node = node
    def move(self):
        edges=set()
        judge=False
        #print self.node
        #print nodes[self.node].variableList
        for edge1 in nodes[self.node].variableList:
            if(self.node < n):
                if(edge1 not in edges):
                    edge2=nodes[self.node].incidentEdges[edge1.rightcolor]
                    if edge2 is None:
                        nodes[self.node].exchangecolor(edge1.leftcolor,edge1.rightcolor)
                        nodes[self.node].incidentEdges[edge1.rightcolor]=edge1
                        nodes[self.node].incidentEdges[edge1.leftcolor]=None
                        edge1.leftcolor=edge1.rightcolor
                        nodes[self.node].variableList.remove(edge1)
                        nodes[edge1.rightnode].variableList.remove(edge1)
                        edge1.id=-1
                        edges.add(edge1)
                        judge=True
                        continue
                    elif edge2 not in edges and edge2.rightcolor==edge1.leftcolor:
                        nodes[self.node].incidentEdges[edge2.leftcolor]=edge1
                        nodes[self.node].incidentEdges[edge1.leftcolor]=edge2
                        temp=edge1.leftcolor
                        edge1.leftcolor=edge2.leftcolor
                        edge2.leftcolor=temp
                        edge1.id=-1
                        edge2.id=-1
                        nodes[self.node].variableList.remove(edge1)
                        nodes[self.node].variableList.remove(edge2)
                        nodes[edge1.rightnode].variableList.remove(edge1)
                        nodes[edge2.rightnode].variableList.remove(edge2)
                        edges.add(edge1)
                        edges.add(edge2)
                        judge=True
                        continue
                    elif edge2 not in edges and edge2.rightcolor==edge1.rightcolor:
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
                        nodes[self.node].variableList.remove(edge1)
                        nodes[self.node].variableList.append(edge2)
                        nodes[edge1.rightnode].variableList.remove(edge1)
                        nodes[edge2.rightnode].variableList.append(edge2)
                        edges.add(edge1)
                        edges.add(edge2)
                        judge=True
                        continue
                    elif edge2 not in edges:
                        nodes[self.node].incidentEdges[edge2.leftcolor]=edge1
                        nodes[self.node].incidentEdges[edge1.leftcolor]=edge2
                        temp=edge1.leftcolor
                        edge1.leftcolor=edge2.leftcolor
                        edge2.leftcolor=temp
                        edge1.id=-1
                        edge2.id=-1
                        edge2.count=0
                        nodes[self.node].variableList.remove(edge1)
                        nodes[edge1.rightnode].variableList.remove(edge1)
                        edges.add(edge1)
                        edges.add(edge2)
                        judge=True
                        continue
            else:
                if(edge1 not in edges):
                    edge2=nodes[self.node].incidentEdges[edge1.leftcolor]
                    if edge2 is None:
                        nodes[self.node].exchangecolor(edge1.leftcolor,edge1.rightcolor)
                        nodes[self.node].incidentEdges[edge1.leftcolor]=edge1
                        nodes[self.node].incidentEdges[edge1.rightcolor]=None
                        edge1.rightcolor=edge1.leftcolor
                        nodes[self.node].variableList.remove(edge1)
                        nodes[edge1.leftnode].variableList.remove(edge1)
                        edge1.id=-1
                        edges.add(edge1)
                        judge=True
                        continue
                    elif edge2 not in edges and edge2.leftcolor==edge1.rightcolor:
                        nodes[self.node].incidentEdges[edge2.rightcolor]=edge1
                        nodes[self.node].incidentEdges[edge1.rightcolor]=edge2
                        temp=edge1.rightcolor
                        edge1.rightcolor=edge2.rightcolor
                        edge2.rightcolor=temp
                        edge1.id=-1
                        edge2.id=-1
                        nodes[self.node].variableList.remove(edge1)
                        nodes[self.node].variableList.remove(edge2)
                        nodes[edge1.leftnode].variableList.remove(edge1)
                        nodes[edge2.leftnode].variableList.remove(edge2)
                        edges.add(edge1)
                        edges.add(edge2)
                        judge=True
                        continue
                    elif edge2 not in edges and edge2.leftcolor==edge1.leftcolor:
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
                        nodes[self.node].variableList.remove(edge1)
                        nodes[self.node].variableList.append(edge2)
                        nodes[edge1.leftnode].variableList.remove(edge1)
                        nodes[edge2.leftnode].variableList.append(edge2)
                        edges.add(edge1)
                        edges.add(edge2)
                        judge=True
                        continue
                    elif edge2 not in edges:
                        nodes[self.node].incidentEdges[edge2.rightcolor]=edge1
                        nodes[self.node].incidentEdges[edge1.rightcolor]=edge2
                        temp=edge1.rightcolor
                        edge1.rightcolor=edge2.rightcolor
                        edge2.rightcolor=temp
                        edge1.id=-1
                        edge2.id=-1
                        edge2.count=0
                        nodes[self.node].variableList.remove(edge1)
                        nodes[edge1.leftnode].variableList.remove(edge1)
                        edges.add(edge1)
                        edges.add(edge2)
                        judge=True
                        continue
        return judge

import random,time
import matplotlib.pyplot as plt
def RequestGenerator(n):
    a = []
    random.seed()
    for i in range(0,n):
        a.append(random.randint(0,n)-1)
    return a
    
def drawnodes(s,i):
    global ax
    if(i==1):
        color='r'
        posx=-1*scale
    else:
        color='b'
        posx=1*scale
    posy=0
    for n in s:
        plt.gca().add_patch( plt.Circle((posx,posy),radius=0.1*scale,fc=color))
        if posx>0:
            ax.annotate(n,xy=(posx+0.2*scale,posy))
        else:
            ax.annotate(n,xy=(posx-0.2*scale,posy))
        posy+=1*scale

def color(x):
    return {
        0: 'r',
        1: 'b',
        2: 'g',
        3: 'y',
        4: 'k',
        5: 'c',
        6: 'm',
        7: '#00FFFF',
        8: '#8A2BE2',
        9: '#FFE4C4',
        10: '#6495ED',
        11: '#D2691E',
        12: '#00008B',
        13: '#FF8C00',
        14: '#A52A2A',
        15: '#8B008B',
        16: '#FF1493',
        17: '#FFFF00',
        18: '#00FF7F',
        19: '#CD853F',
        20: '#800080',
    }[x]

def draw():
    global ax,lines
    Multiplicity = [[0]*(n*2) for each in range(n*2)]

    lines.append(ax.lines)
    ax.lines=[]
    
    connections=[]
    for edge in AdjacencyList:
        offset=(-1)**(Multiplicity[edge.leftnode][edge.rightnode]+1) * ((Multiplicity[edge.leftnode][edge.rightnode]+1)/2) * 0.08 * scale
        Multiplicity[edge.leftnode][edge.rightnode]+=1
        if(edge.leftcolor==edge.rightcolor):
            connections+=[((-1*scale,0),(edge.leftnode*scale+offset,(edge.rightnode-n+edge.leftnode)/float(2)*scale+offset),color(edge.leftcolor),1)]
            connections+=[((1*scale,0),((edge.rightnode-n)*scale+offset,(edge.rightnode-n+edge.leftnode)/float(2)*scale+offset),color(edge.rightcolor),1)]
        else:
            connections+=[((-1*scale,0),(edge.leftnode*scale+offset,(edge.rightnode-n+edge.leftnode)/float(2)*scale+offset),color(edge.leftcolor),1.5)]
            connections+=[((1*scale,0),((edge.rightnode-n)*scale+offset,(edge.rightnode-n+edge.leftnode)/float(2)*scale+offset),color(edge.rightcolor),1.5)]
    for c in connections:
        plt.plot(c[0],c[1],c[2],linewidth=scale*c[3])
    plt.draw()

def press(event):
    global lines,k,ax
    #print len(lines)
    if event.key=='right':
        k+=1
        if k>len(lines)-2:
            k=len(lines)-2
        #print k
        ax.lines=lines[k]
        plt.draw()
    elif event.key=='left':
        k-=1
        if k<0:
            k=0
        #print k
        ax.lines=lines[k]
        plt.draw()



#main function
n = 6
scale = 3
nodes = [Node() for each in range(n*2)]
initialEdgesFile='initialEdges'
lines=[]
fig=plt.figure(figsize=(12,9))
ax=fig.add_subplot(111)
fig.canvas.mpl_connect('key_press_event',press)
set1=[]
set2=[]
for i in range(n):
    set1.append(str(i))
    set2.append(str(i+n))
plt.axis([-2*scale,2*scale,-1*scale,(max(len(set1),len(set2))+1)*scale])
frame=plt.gca()
frame.axes.get_xaxis().set_ticks([])
frame.axes.get_yaxis().set_ticks([])
drawnodes(set1,1)
drawnodes(set2,2)

slots = 3
AdjacencyList = []
initialEdges = []
import os
if os.path.isfile(initialEdgesFile):
    f=open(initialEdgesFile)
    initialEdgesFromFile=f.readlines()
    for edgeFromFile in initialEdgesFromFile:
        temp=edgeFromFile[1:-2].split(',')
        edge=Edge(int(temp[0]),int(temp[1]),int(temp[2]),int(temp[3]))
        nodes[int(temp[0])].color[int(temp[2])]=False
        nodes[int(temp[1])].color[int(temp[3])]=False
        AdjacencyList.append(edge)
        initialEdges.append(str(edge))
        nodes[int(temp[0])].incidentEdges[int(temp[2])]=edge
        nodes[int(temp[1])].incidentEdges[int(temp[3])]=edge
        if(int(temp[2])!=int(temp[3])):
            nodes[int(temp[0])].variableList.append(edge)
            nodes[int(temp[1])].variableList.append(edge)
    draw()
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
        draw()

ExchangeThreads1=[]
for i in range(n):
    ExchangeThreads1.append(ExThread(i))
ExchangeThreads2=[]
for i in range(n):
    ExchangeThreads2.append(ExThread(i+n))
            
judge=True
count=0
while(judge):
    count+=1
    judge=False
    for thread in ExchangeThreads2:
        #print thread.node
        if(thread.move()):
            judge=True
    draw()
    for thread in ExchangeThreads1:
        #print thread.node
        if(thread.move()):
            judge=True
    draw()
    if count>n*5:
        #Storage the initial Condition for regenerate the deadlock
        f=open(initialEdgesFile,'w')
        for edge in initialEdges:
            f.write(str(edge)+'\n')
        f.close()
        break

k=0
ax.lines=lines[k]
plt.show()
