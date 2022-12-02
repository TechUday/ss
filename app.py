### Integrate HTML With Flask
### HTTP verb GET And POST

##Jinja2 template engine
'''
{%...%} conditions,for loops
{{    }} expressions to print output
{#....#} this is for comments
'''

import csv
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')



### Result checker submit html page
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    str=''
    if request.method == 'POST':
        science = request.form['science']
        with open("covid-19-dataset-2.csv", "r") as scoreFile:
            scoreFileReader = csv.reader(scoreFile)
            gender = science
            for row in scoreFileReader:
                if row[0] == gender:
                    str = 'country: '+row[0]+'Last Update: '+row[1]+'Lat: '+row[2]+'Long: '+row[3]+'Confirmed: '+row[4]+ 'Deaths: '+row[5]+'Recovered'+row[6]+ 'Active'+row[7]+'eople_Tested: ' + row[9] +'People_Hospitalized: ' + row[10]+'Mortality_Rate'+row[11]
                    print(row)

    strr = ''.join(str)

    return render_template("index.html",result=strr)


if __name__ == '__main__':
    app.run(debug=True)