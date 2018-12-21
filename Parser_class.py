from in_out import *
import pygraphviz as pgv
Graph=pgv.AGraph()


index = 0

tokens = read_lines('testCase.txt') 

def get_token():
    global index
    if(index < len(tokens)):
        temp = index
        index = index +1
        return tokens[temp]

token = tokens[index]
index = index +1
count = 0

def ConnectHorizontal(firstNode,secondNode):
    Graph.subgraph(nbunch=[firstNode,secondNode],rank= 'same')
    Graph.add_edge(firstNode,secondNode)
    

def match(expected_token):
    global token
    token = get_token()

def factor():
    global token
    global Graph
    global count

    if (token == '('):
        match('(')
        ret = exp()
        match(')')
    else:
        temp = token
        match(token)
        Graph.add_node(count,label = temp)
        ret = Graph.get_node(count)
        count += 1
    return ret


def term():
    temp = factor()
    global token
    global count
    while (token == '*' or token == '/') :
        #name = name + '1'
        Graph.add_node(count,label = token)
        parentnode = Graph.get_node(count)
        count += 1
        match(token)
        leftchild = temp
        rightchild =factor()
        Graph.add_edge(parentnode,leftchild)
        Graph.add_edge(parentnode,rightchild)  #rightchild
        temp = parentnode

    return temp    
        

def exp():
    temp = term()        
    global token
    global count
    while (token == '+' or token == '-' ) :
        Graph.add_node(count,label = token)
        parentnode = Graph.get_node(count)
        count += 1
        match(token)
        leftchild = temp
        rightchild =term()
        Graph.add_edge(parentnode,leftchild)
        Graph.add_edge(parentnode,rightchild)  #rightchild
        temp = parentnode
    if (token == '<' or token == '>'or token == '='):
        Graph.add_node(count,label = token)
        parentnode = Graph.get_node(count)
        count += 1
        match(token)
        leftchild = temp
        rightchild = exp()
        Graph.add_edge(parentnode,leftchild)
        Graph.add_edge(parentnode,rightchild)
        return parentnode
    
    else:
        return temp


def Read():
    global count
    match('read')
    if(isIdentfier(token)):
        Graph.add_node(count,label = 'read \n'+token,shape='rectangle')

        temp = Graph.get_node(count)
        count +=1
        match(token)
    return temp

def Write():
    global count
    match('write')
    temp1 = exp()
    Graph.add_node(count, label ='write',shape='rectangle')
    Graph.add_edge(count , temp1)
    temp = Graph.get_node(count)
    count+=1
    match(token)
    return temp

def ifStatement():
    global count
    global token
    match('if')
    Graph.add_node(count,label = 'if',shape='rectangle')
    parentnode= Graph.get_node(count)
    count +=1
    leftchild=exp()
    Graph.subgraph(nbunch=[leftchild],rank= 'same')

    match('then')
    rightchild=stmtSeq()
    Graph.subgraph(nbunch=[leftchild,rightchild],rank= 'same')

    Graph.add_edge(leftchild,rightchild,color='white')
    Graph.add_edge(parentnode,leftchild)
    Graph.add_edge(parentnode,rightchild)
    if (token=='else'):
        match('else')
        elsechild = stmtSeq()
        Graph.add_edge(parentnode,elsechild)
    match('end')
    return parentnode

def repeat():
    global count
    global token
    match('repeat')
    Graph.add_node(count,label = 'repeat',shape='rectangle')
    parentnode= Graph.get_node(count)
    count +=1
    leftchild = stmtSeq()
    match('until')
    rightchild = exp()
    Graph.subgraph(nbunch=[rightchild],rank = 'same')
    Graph.add_edge(parentnode,leftchild)
    Graph.add_edge(parentnode,rightchild)
    return parentnode

def assign():
    temp = exp()        
    global token
    global count
    while (token == ':=') :
        Graph.add_node(count,label = token)
        parentnode = Graph.get_node(count)
        count += 1
        match(token)
        leftchild = temp
        rightchild =exp()
        Graph.subgraph(nbunch=[leftchild,rightchild],rank = 'same')
        Graph.add_edge(leftchild,rightchild , color = 'white')
        Graph.add_edge(parentnode,leftchild)
        Graph.add_edge(parentnode,rightchild)  #rightchild
        temp = parentnode

    return temp    

def stmt():
    if token == 'read':
        temp = Read()
    elif token == 'write':
        temp = Write()   
    elif token == 'if':
        temp = ifStatement()
    elif token =='repeat':
        temp = repeat()    
    else:
        temp = assign()    
    return temp
   
def stmtSeq():
    temp = stmt()
    temp1 = temp
    global count
    while (token == ';'):
        match(token)
        temp2 = stmt()
        ConnectHorizontal(temp1,temp2)
        temp1 = temp2

    return temp

stmtSeq()
Graph.draw('SyntaxTree.png',prog='dot') 




