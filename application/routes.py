from application import app
from flask import render_template, redirect, url_for, request, flash
import string, random


@app.route("/")
@app.route("/home")
def home():
    username = ''
    strings = ''.join(random.choices(string.ascii_lowercase[0:3], k=5))
    numbers = ''.join(random.choices(string.digits, k=3))
    prize =''
    for i in range(len(strings)):
        if i+1 > len(numbers):
            username += strings[i]
        else:
            username += strings[i] + numbers[i]

    if username[0]=='a':
        if random.randrange(1,100,1)<=25:
            prize= "Youve won £100!"
        elif random.randrange(1,100,1)<=75:
            prize='Youve won £50!'
        else:
            prize="You didn't win this time"
    else:
        prize='Youve lost'
    
    return render_template('home.html', title='Home', username=username, prize=prize)


