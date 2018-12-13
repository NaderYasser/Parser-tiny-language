from in_out import *
import pygraphviz as pgv
Graph=pgv.AGraph()
Graph1=pgv.AGraph()
Graph2=pgv.AGraph()
#tokens=get_tokens("x := x + 3 ; ")

index = 0
tokens = ['x',':=','3','*','6','+','y','*','7','-','z']
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
        #exp
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
    while (token == '+' or token == '-') :
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

    return temp
def assign():
    temp = exp()        
    global token
    global count
    while (token == ':=') :
        #name = name + '1'
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

# factor()
# term()
assign()


Graph.draw('file1.png',prog='dot') 



