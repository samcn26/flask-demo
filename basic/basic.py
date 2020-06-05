from flask import Flask,request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello():
    return {"name": "sam-tech"}

class School(Resource):
    # in path
    def get(self, name):
        # in query
        args = request.args
        # request body json
        json_data = request.get_json()

        # request.form works only if you POST data with the right content types; 
        # form data is either POSTed with the application/x-www-form-urlencoded or multipart/form-data encodings.
        # e.g. curl <url> -d 'teacher=sam' -X GET

        return {"school-name": name,"teacher": args["teacher"], 'json':json_data}

api.add_resource(School, '/school/<string:name>')

if __name__ == '__main__':
      app.run('0.0.0.0','5000',debug=True)

# to test
# poython3 -m venv venv -> source venv/bin/activate -> python basic/basic.py
# curl http://127.0.0.1:5000/school/sam-tech?teacher=tom  -X GET -H "Content-Type: application/json" -d '{"company":"jc-tech","age":18}'