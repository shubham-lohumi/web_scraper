import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():

    url="https://www.geeksforgeeks.org/machine-learning/ml-linear-regression/"
    response=requests.get(url)

    if response.status_code==200:
        print("web fetched sucessfully")
    else:

        print("falied")

    soup=BeautifulSoup(response.text,'html.parser')

    para=soup.find_all("div",class_="content")
    if para:
        article=[p.text for p in para.find_all("p")]
    else:
        article=[]

    return render_template("index.html",data=article)

if __name__=="__main__":
    app.run(debug=True)