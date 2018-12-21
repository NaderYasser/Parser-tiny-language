from in_out import *
import pygraphviz as pgv
Graph=pgv.AGraph()


index = 0
tokens = ['read','x','read', 'y']
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
        exp()
        match(')')
    else:
        temp = token
        match(token)
        Graph.add_node(count,label = temp)
        count += 1
    return Graph.get_node(count-1)


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
        #name = name + '1'
        Graph.add_node(count,label = token)
        parentnode = Graph.get_node(count)
        count += 1
        match(token)
        leftchild = temp
        rightchild =term()
        Graph.add_edge(parentnode,leftchild)
        Graph.add_edge(parentnode,rightchild)  #rightchild
        temp = parentnode
    if (token == '<' or token == '>'):
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
        Graph.add_node(count,label = 'read')
        Graph.add_node(token)
        Graph.add_edge(count,token)
        temp = Graph.get_node(count)
        count +=1
    return temp


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
        Graph.add_edge(parentnode,leftchild)
        Graph.add_edge(parentnode,rightchild)  #rightchild
        temp = parentnode

    return temp    




def stmt():
    temp = Read()
    Graph.add_subgraph(temp, rank = 'same')
    return temp



    
def stmtSeq():
    temp = stmt()
    global count
    while (token == ';'):
        # parentnode = Graph.add_node(count , label='StmtSeq')
        match(token)
        leftchild = temp
        rightchild =  stmt()
        Graph.add_edge('StmtSeq',leftchild)
        Graph.add_edge('StmtSeq',rightchild)
        count+=1
        
    return temp 




stmtSeq()




Graph.draw('file1.png',prog='dot') 




