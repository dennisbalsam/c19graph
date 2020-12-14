import sys
import json
import networkx as nx
import psycopg2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# define initial graph
graph = nx.Graph()

# trace path of spread
def tracePath(node, depth):
    if depth == 0: return
    
    for i in graph.neighbors(node):
        graph.add_edge(node, i, color='r')
        tracePath(i, depth-1)

# get initial data from database
def initialGraph():
    try:
        connection = psycopg2.connect(user = 'postgres', host = '127.0.0.1', port = '5432', database = 'c19contact')
    except (Exception) as error :
        sys.stderr.write(str(error))
        sys.exit(1)

    cursor = connection.cursor()

    # all people rows
    cursor.execute('select * from People;')
    people = cursor.fetchall()

    # all contact rows 
    cursor.execute('select * from Contact;')
    contact = cursor.fetchall()

    # connect all people who have made contact
    for row in contact:
        graph.add_edge(row[0],row[1],color='k')

    # add all people
    for row in people:
        if row[3] == True: # infected node
            graph.add_node(row[0], name=row[1], age=row[2], infected=row[3], color='r')
            tracePath(row[0],2)
        else:
            graph.add_node(row[0], name=row[1], age=row[2], infected=row[3], color='teal')


    draw()



# draw graph
def draw():
    edge_colors = list(nx.get_edge_attributes(graph,'color').values())
    node_colors = list(nx.get_node_attributes(graph,'color').values())

    # nx.draw_networkx(graph,font_color='black')
    nx.draw_networkx(graph, node_color=node_colors,edge_color=edge_colors, font_color='white', pos=nx.circular_layout(graph), width=2)
    plt.savefig('./static/img/graph.png') # save graph image
    plt.close()


graph.draw = draw