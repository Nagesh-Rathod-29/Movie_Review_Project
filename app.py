from flask import Flask,render_template,request,jsonify
import model,config
import traceback

_model = model.Model()


app = Flask(__name__)
@app.route('/')
def home():
    #return jsonify({"Result":"This is home page"})
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def output():
    try:
        if request.method=='GET':
            data = request.args.get
            text = data(('text'))
            prediction = _model.result(text)
            
            result = ""
            if prediction == 0:
                result = "NEGATIVE REVIEW"
            else:
                result = "POSITIVE REVIEW"

            return render_template('index.html',prediction=result)
        else:
            
            data = request.form.get
            text = data(('text'))
            prediction = _model.result(text)
            
            result = ""
            if prediction == 0:
                result = "NEGATIVE REVIEW"
            else:
                result = "POSITIVE REVIEW"

            return render_template('index.html',prediction=result)
    except:
        return jsonify({"Error":f"{traceback.print_exc()}"})
if __name__ == "__main__":
    app.run(host=config.HOST,port=config.PORT,debug=True)