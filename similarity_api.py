from flask import Flask,jsonify,request,render_template
import string
from custom_logger.logger import logger
from flask_cors import CORS
from processor.matcher import distance

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
@app.route("/string_matching", methods=['GET','POST'])
def string_matching():
    if request.method == 'POST':
        string_1=request.form["string_1"]
        string_2 = request.form["string_2"]
        file=distance(string_1,string_2)
        return render_template('similarity.html',file=file,string_1=string_1,string_2=string_2)
    else:
        return render_template('new_similarity.html')

if __name__ == '__main__':
    app.run(debug=True)