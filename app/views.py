from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = { 'nickname' : 'Scott' } # fake user
	posts = [
		{
			'author': { 'nickname': 'benji'},
			'body': 'The avengers movie is awesome!'
		},
		{
			'author': { 'nickname': 'Rach'},
			'body': 'Nice day!'
		},
		{
			'author': { 'nickname': 'Rach'},
			'body': 'Nice day!'
		},
		{
			'author': { 'nickname': 'Rach'},
			'body': 'Nice day!'
		},
		{
			'author': { 'nickname': 'Rach'},
			'body': 'Nice day!'
		},
		{
			'author': { 'nickname': 'Rach'},
			'body': 'Nice day!'
		},
		{
			'author': { 'nickname': 'Rach'},
			'body': 'Nice day!'
		},
		{
			'author': { 'nickname': 'Rach'},
			'body': 'Nice day!'
		},
		{
			'author': { 'nickname': 'Rach'},
			'body': 'Nice day!'
		},
		{
			'author': { 'nickname': 'Rach'},
			'body': 'Nice day!'
		}
	]
	return render_template("index.html", 
		title = 'Home',
		user = user,
		posts = posts)