import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():

    url="https://quotes.toscrape.com"
    response=requests.get(url)

    if response.status_code==200:
        print("web fetched sucessfully")
    else:

        print("falied")

    soup=BeautifulSoup(response.text,'html.parser')

    quotes=soup.find_all("span",class_="text")

    return render_template("index.html",data=quotes)

if __name__=="__main__":
    app.run(debug=True)