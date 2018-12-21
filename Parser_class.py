from in_out import *
from graphviz import Graph
Graph = Graph(format='png')


index = 0
tokens = ['x',':=','6',';','z',':=','y','+','7']
def get_token():
    global index
    if(index < len(tokens)):
        temp = index
        index = index +1
        return tokens[temp]

token = tokens[index]
index = index +1
count = 0

def match(expected_token):
    global token
    token = get_token()

def factor():
    global token
    global Graph
    global count

    if (token == '('):
        match('(')
        #exp()
        match(')')
    else:
        temp = token
        match(token)
        Graph.node(count,label = temp)
        count += 1
    return Graph.node(count-1)


def term():
    temp = factor()
    global token
    global count
    while (token == '*' or token == '/') :
        #name = name + '1'
        Graph.node(count,label = token)
        parentnode = Graph.node(count)
        count += 1
        match(token)
        leftchild = temp
        rightchild =factor()
        Graph.edge(parentnode,leftchild)
        Graph.edge(parentnode,rightchild)  #rightchild
        temp = parentnode

    return temp    
        

def exp():
    temp = term()        
    global token
    global count
    while (token == '+' or token == '-' ) :
        #name = name + '1'
        Graph.node(count,label = token)
        parentnode = Graph.node(count)
        count += 1
        match(token)
        leftchild = temp
        rightchild =term()
        Graph.edge(parentnode,leftchild)
        Graph.edge(parentnode,rightchild)  #rightchild
        temp = parentnode
    if (token == '<' or token == '>'):
        Graph.node(count,label = token)
        parentnode = Graph.node(count)
        count += 1
        match(token)
        leftchild = temp
        rightchild = exp()
        Graph.edge(parentnode,leftchild)
        Graph.edge(parentnode,rightchild)
        return parentnode
    
    else:
        return temp
def assign():
    temp = exp()        
    global token
    global count
    while (token == ':=') :
        Graph.node(count,label = token)
        parentnode = Graph.node(count)
        count += 1
        match(token)
        leftchild = temp
        rightchild =exp()
        Graph.edge(parentnode,leftchild)
        Graph.edge(parentnode,rightchild)  #rightchild
        temp = parentnode

    return temp    




def stmt():
    temp = assign()
    Graph.subgraph(temp)
    return temp



    
def stmtSeq():
    temp = stmt()
    while (token == ';'):
        match(token)
        temp1 =  stmt()
        Graph.edge(temp1,temp )
        temp = temp1
    return temp 




stmtSeq()




Graph.render() 




