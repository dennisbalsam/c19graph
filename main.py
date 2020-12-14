import json
import random
import os
import subprocess
from graph_operations import graph, initialGraph, tracePath
from flask import Flask, request, render_template, redirect, url_for, make_response
app = Flask(__name__)


def updateAndDraw():
    graph.filehash = random.randint(1000,4000)
    graph.draw(f'static/img/graph{graph.filehash}.png')

@app.route("/")
def index():
    initialGraph()
    resp = make_response(render_template('index.html',
        filepath = f'static/img/graph{graph.filehash}.png',
        nodes = graph.nodes()))
    resp.cache_control.max_age = 0
    return resp

@app.route("/addedge")
def addedge():
    graph.add_edge(int(request.args.get('label1')),int(request.args.get('label2')),color='k')
    updateAndDraw()
    return redirect(url_for('index'))

@app.route("/toggleinfection")
def toggleinfection():

    node = int(request.args.get('label'))
    graph.nodes[node]['infected'] = not graph.nodes[node]['infected']

    if graph.nodes[node]['infected'] == True :
        graph.nodes[node]['color'] = 'r'
        tracePath(node,2)
    else:
        graph.nodes[node]['color'] = 'teal'

    print(graph.nodes[node]['infected'])
    updateAndDraw()
    return render_template('index.html',
        filepath = f'static/img/graph{graph.filehash}.png',
        nodes = graph.nodes()) 
    # return redirect(url_for('index'))


if __name__ == '__main__':
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
  app.run()