import json
import random
import os
import subprocess
from graph_operations import graph, initialGraph
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)





def updateAndDraw():
    graph.draw()

@app.route("/")
def index():
    initialGraph()
    return render_template('index.html',filepath = f'static/img/graph.png') 

@app.route("/addnode")
def addnode():
    graph.add_node(int(request.args.get('label')))
    updateAndDraw()
    return redirect(url_for('index'))

@app.route("/addedge")
def addedge():
    graph.add_edge(int(request.args.get('label1')),int(request.args.get('label2')),color='k')
    updateAndDraw()
    return redirect(url_for('index'))


if __name__ == '__main__':
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
  app.run(host='0.0.0.0')