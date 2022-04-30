from flask import Flask, render_template, jsonify, make_response,redirect
from dotenv import load_dotenv


app = Flask(__name__,static_url_path='',static_folder='static', template_folder='templates')

# if __name__ == '__main__':
#     app.run(debug=True)
    
@app.route("/",methods=['GET'])
def index_get():
    return render_template("index.html")

app.run(debug=True)
