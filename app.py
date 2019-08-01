from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/processed', methods=['POST'])
def process():
	numSmTurkey = (170 - int(request.form['sTurkeyCount']))
	numLgTurkey = (35 - int(request.form['lTurkeyCount']))
	numSmChix = (45 - int(request.form['sMChixCount']))
	numLgChix = (5 - int(request.form['lMChixCount']))
	numSmRB = (8 - int(request.form['sRBCount']))
	numLgRB = (8 - int(request.form['lRBCount']))
	numSmPastrami = (5 - int(request.form['sPastramiCount']))
	numLgPastrami = (6 - int(request.form['lPastramiCount']))
	numCapi = (45 - int(request.form['capiCount']))

	turkeyNeeded = round((38.5 - float(request.form['turkeyWeight']) - (((numSmTurkey*2.25)+(numLgTurkey*3.5))/16)),1)
	chixNeeded = round((12.5 - float(request.form['chixWeight']) - (((numSmChix*2.25)+(numLgChix*3.5))/16)),1)
	rbNeeded = round((8 - float(request.form['rbWeight']) - (((numSmRB*2.25)+(numLgRB*3.5))/16)),1)
	pastramiNeeded = round((8.5 - float(request.form['pastramiWeight']) - (((numSmPastrami*3)+(numLgPastrami*4))/16)),1)
	capiNeeded = round((10 - float(request.form['capiWeight']) - ((numCapi*1.75)/16)),1)

	hamNeeded = (4 - float(request.form['ham']))
	salamiNeeded = (3 - float(request.form['salami']))
	bolognaNeeded = (25 - int(request.form['bologna']))
	provoloneNeeded = (6 - float(request.form['provolone']))
	tomatoNeeded = int(round((9 - float(request.form['tomato']))*9,0))

	return render_template('processed.html', sTurkeyPortionsNeeded=numSmTurkey,
		lTurkeyPortionsNeeded=numLgTurkey, sMChixPortionsNeeded=numSmChix, lMChixPortionsNeeded=numLgChix,
		sRBPortionsNeeded=numSmRB, lRBPortionsNeeded=numLgRB, sPastramiPortionsNeeded=numSmPastrami,
		lPastramiPortionsNeeded=numLgPastrami, capiPortionsNeeded=numCapi, poundsTurkey=turkeyNeeded,
		poundsChix=chixNeeded, poundsRB=rbNeeded, poundsPastrami=pastramiNeeded, poundsCapi= capiNeeded, 
		tinsOfHam=hamNeeded, tinsOfSalami=salamiNeeded, slicesOfBologna=bolognaNeeded,
		tinsOfProvolone=provoloneNeeded, numTomato=tomatoNeeded)

if __name__ == '__main__':
	app.run()