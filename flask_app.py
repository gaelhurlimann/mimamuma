import os
import csv
import random


from flask import Flask
from flask import render_template
from flask import request

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
@app.route('/')

def index(bandname="Photek"):
    return render_template('matitle.html', name=bandname)
@app.route('/<string:bandname>', methods=['GET', 'POST'])
def hello_world(bandname):
	if request.method == 'POST':
		bandname = request.form['groupe']
		title = createtitle(bandname)
		return render_template('mamaker.html', name=bandname, title=title)
	else:
		return render_template('matitle.html', name=bandname)

def createtitle(bandname):
	groupesSyn = []
	VerbesSyn = []

#read groupes
	document_path = my_file = os.path.join(THIS_FOLDER, 'dictionnaries/groupe.txt')
	with open(document_path, 'r') as f:
		reader = csv.reader(f, delimiter='\t')
		groupesSyn = (list(reader))[0]
	groupe = groupesSyn[random.randint(0, len(groupesSyn)-1)]

#read Verbes
	document_path = 'dictionnaries/verbe.txt'
	with open(document_path, 'r') as f:
		reader = csv.reader(f, delimiter='\t')
		VerbesSyn = (list(reader))[0]
	verbe = VerbesSyn[random.randint(0, len(VerbesSyn)-1)]

#read des mots pour dire "musique"
	document_path = 'dictionnaries/musique.txt'
	with open(document_path, 'r') as f:
		reader = csv.reader(f, delimiter='\t')
		musiqueSyn = (list(reader))
	musique = musiqueSyn[random.randint(0, len(musiqueSyn)-1)]
	det = singplur_to_det(musique[1])

#read des adjectifs pour qualifier la musique
	document_path = 'dictionnaries/adj.txt'
	with open(document_path, 'r') as f:
		reader = csv.reader(f, delimiter='\t')
		adjSyn = (list(reader))
	adj = adjSyn[random.randint(0, len(adjSyn)-1)]

	if isfeminin(musique[1]):
		adj = adj[1]
	else:
		adj = adj[0]

	if un_s_ou_pas(musique[1]):
		adj = adj+"s"
	#un 2e adjectif	
	adj2 = adjSyn[random.randint(0, len(adjSyn)-1)]
	if isfeminin(musique[1]):
		adj2 = adj2[1]
	else:
		adj2 = adj2[0]
	if un_s_ou_pas(musique[1]):
		adj2 = adj2+"s"


	return str(groupe) +" "+bandname+" "+str(verbe) +" "+str(det)+" "+str(musique[0])+" "+str(adj)+" et "+str(adj2)
	# nom groupe + "nom" + verbe + noms musique + adj1 + adj 2 

def singplur_to_det(argument): 
    switcher = { 
        "m": "un", 
        "f": "une", 
        "mpl": "des",
        "fpl": "des"
    }
    return switcher.get(argument, " ")

def un_s_ou_pas(argument): 
    switcher = { 
        "m": "", 
        "f": "", 
        "mpl": "s",
        "fpl": "s"
    }
    return switcher.get(argument, "") 

def isfeminin(argument): 
    switcher = { 
        "m": 0, 
        "f": 1, 
        "mpl": 0,
        "fpl": 1
    }
    return switcher.get(argument, 0) 
