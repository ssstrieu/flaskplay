from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/welcome/<oname>/')
def index(oname):
	return render_template('index.html',yourname=oname)

@app.route('/')
def index2():
	return 'cats'

@app.route('/count/')
def count():
	numbers= range(10)
	return render_template('count.html', numbers=numbers)

@app.route('/pintrest/<creator>/')
def pin(creator):
	user='Samantha'
	pins = [
    {
        'image': '/static/images/paws.jpg',
        'caption': 'Paws',
        'avatar': '/static/images/android_boy.jpg',
        'name': 'Dwayne Stewart',
        'category': 'Latte Art'
    },
    {
        'image': '/static/images/paris.jpg',
        'caption': 'Paws',
        'avatar': '/static/images/android_boy.jpg',
        'name': 'Dwayne Stewart',
        'category': 'Latte Art'
    },
    {
        'image': '/static/images/vegan_chai.jpg',
        'caption': 'Paws',
        'avatar': '/static/images/android_boy.jpg',
        'name': 'Dwayne Stewart',
        'category': 'Latte Art'
    },
    {
        'image': '/static/images/olaf.jpg',
        'caption': "Is this a swan? Whatever - it's pretty!",
        'avatar': '/static/images/woman_italy.jpg',
        'name': 'Nuria Cohen',
        'category': 'Love My Latte'
    }
    ,
    {
        'image': '/static/images/snowman.jpg',
        'caption': "Is this a swan? Whatever - it's pretty!",
        'avatar': '/static/images/woman_italy.jpg',
        'name': 'Nuria Cohen',
        'category': 'Love My Latte'
    },
    {
        'image': '/static/images/pretty.jpg',
        'caption': "Is this a swan? Whatever - it's pretty!",
        'avatar': '/static/images/woman_italy.jpg',
        'name': 'Nuria Cohen',
        'category': 'Love My Latte'
    },
    {
        'image': '/static/images/paris.jpg',
        'caption': 'Paws',
        'avatar': '/static/images/android_boy.jpg',
        'name': 'Dwayne Stewart',
        'category': 'Latte Art'
    },
    {
        'image': '/static/images/vegan_chai.jpg',
        'caption': 'Paws',
        'avatar': '/static/images/android_boy.jpg',
        'name': 'Dwayne Stewart',
        'category': 'Latte Art'
    },
    {
        'image': '/static/images/olaf.jpg',
        'caption': "Is this a swan? Whatever - it's pretty!",
        'avatar': '/static/images/woman_italy.jpg',
        'name': 'Nuria Cohen',
        'category': 'Love My Latte'
    }
    ,
    {
        'image': '/static/images/snowman.jpg',
        'caption': "Is this a swan? Whatever - it's pretty!",
        'avatar': '/static/images/woman_italy.jpg',
        'name': 'Nuria Cohen',
        'category': 'Love My Latte'
    },
    {
        'image': '/static/images/pretty.jpg',
        'caption': "Is this a swan? Whatever - it's pretty!",
        'avatar': '/static/images/woman_italy.jpg',
        'name': 'Nuria Cohen',
        'category': 'Love My Latte'
    },
    {
        'image': '/static/images/paris.jpg',
        'caption': 'Paws',
        'avatar': '/static/images/android_boy.jpg',
        'name': 'Dwayne Stewart',
        'category': 'Latte Art'
    },
    {
        'image': '/static/images/vegan_chai.jpg',
        'caption': 'Paws',
        'avatar': '/static/images/android_boy.jpg',
        'name': 'Dwayne Stewart',
        'category': 'Latte Art'
    },
    {
        'image': '/static/images/olaf.jpg',
        'caption': "Is this a swan? Whatever - it's pretty!",
        'avatar': '/static/images/woman_italy.jpg',
        'name': 'Nuria Cohen',
        'category': 'Love My Latte'
    }
    ,
    {
        'image': '/static/images/snowman.jpg',
        'caption': "Is this a swan? Whatever - it's pretty!",
        'avatar': '/static/images/woman_italy.jpg',
        'name': 'Nuria Cohen',
        'category': 'Love My Latte'
    },
    {
        'image': '/static/images/pretty.jpg',
        'caption': "Is this a swan? Whatever - it's pretty!",
        'avatar': '/static/images/woman_italy.jpg',
        'name': 'Nuria Cohen',
        'category': 'Love My Latte'
    },
    {
        'image': '/static/images/paris.jpg',
        'caption': 'Paws',
        'avatar': '/static/images/android_boy.jpg',
        'name': 'Dwayne Stewart',
        'category': 'Latte Art'
    },
    {
        'image': '/static/images/vegan_chai.jpg',
        'caption': 'Paws',
        'avatar': '/static/images/android_boy.jpg',
        'name': 'Dwayne Stewart',
        'category': 'Latte Art'
    },
    {
        'image': '/static/images/olaf.jpg',
        'caption': "Is this a swan? Whatever - it's pretty!",
        'avatar': '/static/images/woman_italy.jpg',
        'name': 'Nuria Cohen',
        'category': 'Love My Latte'
    }
    ,
    {
        'image': '/static/images/snowman.jpg',
        'caption': "Is this a swan? Whatever - it's pretty!",
        'avatar': '/static/images/woman_italy.jpg',
        'name': 'Nuria Cohen',
        'category': 'Love My Latte'
    },
    {
        'image': '/static/images/pretty.jpg',
        'caption': "Is this a swan? Whatever - it's pretty!",
        'avatar': '/static/images/woman_italy.jpg',
        'name': 'Nuria Cohen',
        'category': 'Love My Latte'
    }
	]
	creators=[]

	for x in pins:
		if (x['name']==creator):
			author= x['name']
			print author
			creators.append(x)

	print 'outside', author
	return render_template('index2.html', user=user, pins=pins)




if __name__=='__main__':
    app.run(debug=True)