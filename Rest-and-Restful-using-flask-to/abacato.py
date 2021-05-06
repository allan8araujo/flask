from flask import Flask
import requests
app=Flask(__name__)

name=input(str())

@app.route("/")
def Tibia_nick_searcher():
    link=('https://api.tibiadata.com/v2/characters/'+name+'.json')
    response=requests.get(link).json()
    return print(response)

if __name__ == '__main__':
    app.run()