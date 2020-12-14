import sys
import json
import networkx as nx
import psycopg2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# define initial graph
graph = nx.Graph()

# get data from postgres

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


    # add all people
    for row in people:
        graph.add_node(row[0], name=row[1], age=row[2], infected=row[3])

    # connect all people who have made contact
    for row in contact:
        graph.add_edge(row[0],row[1])


    draw()

# draw graph
def draw():
    nx.draw_networkx(graph,font_color='black')
    plt.savefig('./static/img/graph.png') # save graph image
    plt.close()


graph.draw = draw