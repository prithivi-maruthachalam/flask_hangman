#a Prithvi Maruthachalam production

from flask import Flask,render_template,request,redirect,url_for
import random
file = open('words.txt','r')
words = file.readlines()



word = ""
position = list()
tick = 0
attempts = 0
word = ""
app = Flask(__name__)
@app.route('/')
def index():
	global word
	global position
	global tick
	global attempts
	position = list()
	tick = 0
	attempts = 0
	x = random.randint(1,len(words))
	word = words[x].strip('\n')
	word = word.lower()
	return render_template('index.html')

	
@app.route('/mainGame/<positions>')
def mainGame(positions):
	global position
	global word 
	global tick
	global attempts
	positions = position
	print("[HELP]:      ----------------------",word)
	print("tick",tick)
	if(tick == 0):
		position = list([""]*len(word))
	print(list(word),positions)
	if(list(word) == positions):
		return render_template('gameOver.html',text="You Win!",identity="win")
	elif(attempts >= 7):
		return render_template('gameOver.html',text="You Lost",identity="lose")
		
	return render_template('mainGame.html',wordToGuess = word,pos = list(positions),length = len(word),tries = (7-attempts))

@app.route('/mainGame/checkLetter',methods=['POST'])
def checkLetter():
	choice = request.form['userLetter'];
	choice = choice.lower()
	global position
	global word
	global tick
	global attempts
	tick += 1
	flag = 0
	for i,letter in enumerate(word):
		if letter == choice:
			position[i] = letter
			flag = 1
	if flag == 0:
		attempts += 1
	return redirect(url_for('mainGame',positions = position))
	
	
	
if __name__ == '__main__':
	app.debug = True
	app.run()
	app.run(debug=True)
