from flask import Flask, request, render_template
from textblob import TextBlob

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def load_index():
    return render_template("index.html")

@app.route("/sentiment",methods=['GET','POST'])
def get_score():
    text=request.form.get("text")
    model=TextBlob(text)
    score=model.sentiment.polarity
    result=""
    if(score==0.0):
        result+="Neutral"
    elif(score>0.0):
        result+="Positive"
    else:
        result+="Negative"
    return render_template("result.html",value=str(score),text=text,
        result=result)

if(__name__ == "__main__"):
    app.run(host="0.0.0.0",port=8000,debug=True)
