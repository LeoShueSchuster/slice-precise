from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/processed', methods=['POST'])
def process():
	numSmTurkey =   max((170 - int(request.form['sTurkeyCount'])),0)
	numLgTurkey =   max((35 - int(request.form['lTurkeyCount'])),0)
	numSmChix =     max((45 - int(request.form['sMChixCount'])),0)
	numLgChix =     max((5 - int(request.form['lMChixCount'])),0)
	numSmRB =       max((8 - int(request.form['sRBCount'])),0)
	numLgRB =       max((8 - int(request.form['lRBCount'])),0)
	numSmPastrami = max((5 - int(request.form['sPastramiCount'])),0)
	numLgPastrami = max((6 - int(request.form['lPastramiCount'])),0)
	numCapi =       max((45 - int(request.form['capiCount'])),0)

	turkeyNeeded =   round((((((numSmTurkey*2.25)+(numLgTurkey*3.5))/16) + 3.5) - float(request.form['turkeyWeight'])),1)
	chixNeeded =     round((((((numSmChix*2.25)+(numLgChix*3.5))/16) + 2.5) - float(request.form['chixWeight'])),1)
	rbNeeded =       round((((((numSmRB*2.25)+(numLgRB*3.5))/16) + 2.5) - float(request.form['rbWeight'])),1)
	pastramiNeeded = round((((((numSmPastrami*3)+(numLgPastrami*4))/16) + 3) - float(request.form['pastramiWeight'])),1)
	capiNeeded =     round(((((numCapi*1.75)/16) + 2.5) - float(request.form['capiWeight'])),1)
	turkeyNeeded =   max(turkeyNeeded,0)
	chixNeeded =     max(chixNeeded,0)
	rbNeeded =       max(rbNeeded,0)
	pastramiNeeded = max(pastramiNeeded,0)
	capiNeeded =     max(capiNeeded,0)

	hamNeeded =       max((4 - float(request.form['ham'])),0)
	salamiNeeded =    max((3 - float(request.form['salami'])),0)
	bolognaNeeded =   max((25 - int(request.form['bologna'])),0)
	provoloneNeeded = max((6 - float(request.form['provolone'])),0)
	tomatoNeeded =    max(int(round((9 - float(request.form['tomato']))*9,0)),0)

	return render_template('processed.html', sTurkeyPortionsNeeded=numSmTurkey,
		lTurkeyPortionsNeeded=numLgTurkey, sMChixPortionsNeeded=numSmChix, lMChixPortionsNeeded=numLgChix,
		sRBPortionsNeeded=numSmRB, lRBPortionsNeeded=numLgRB, sPastramiPortionsNeeded=numSmPastrami,
		lPastramiPortionsNeeded=numLgPastrami, capiPortionsNeeded=numCapi, poundsTurkey=turkeyNeeded,
		poundsChix=chixNeeded, poundsRB=rbNeeded, poundsPastrami=pastramiNeeded, poundsCapi= capiNeeded, 
		tinsOfHam=hamNeeded, tinsOfSalami=salamiNeeded, slicesOfBologna=bolognaNeeded,
		tinsOfProvolone=provoloneNeeded, numTomato=tomatoNeeded)

if __name__ == '__main__':
	app.run()