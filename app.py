from flask import Flask,render_template,jsonify

from flask import request as req 

import pickle

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')




@app.route('/detect',methods=['GET','POST'])
def detection():
    return render_template('detection.html')
    
@app.route('/detect/predict',methods=['GET','POST'])
def predict():
    
    userid=""
    title=""
    if req.method=='POST':
        userid=req.form['userid']
        title=req.form['tweets']
        # pipeline=pickle.load(open('model.pkl','rb'))
        print(userid)
    res=0
    msg=""
    if(res):msg="Fake"
    else:msg="Real"
    # res=pipeline.predict([title]) 
    
      
    return render_template('detection.html',result=res,msg=msg)
    
    
    
    
if __name__=='__main__':
    debug=False
    print("app is running")
    app.run()