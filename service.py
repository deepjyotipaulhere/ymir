from flask import Flask,jsonify,make_response,request
from flask_cors import CORS
import os
import pymongo

app=Flask(__name__)
CORS(app)

@app.route("/uploadimage", methods=['POST'])
def uploadimage():
    from werkzeug.utils import secure_filename
    try:
        import random
        x=request.files['test']
        filename = secure_filename(str(random.randint(1,10000))+str(hash(x.filename))+x.filename)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="genuine-axle-260012-f128668d1884.json"

        from google.cloud import storage
        storage_client=storage.Client()
        bucket = storage_client.get_bucket('ymirimages')
        blob = bucket.blob(filename)
        blob.upload_from_file(x,content_type=x.content_type)
        blob.make_public()

        return blob.public_url
    except Exception as ex:
        # print(ex)
        # con.close()
        return make_response(str(ex),500)


@app.route("/detect", methods=['POST'])
def detect():
    x=request.get_json()
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="genuine-axle-260012-f128668d1884.json"

    from google.cloud import vision

    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    print(str(x['filename']))
    image.source.image_uri = str(x['filename'])
    response = client.document_text_detection(image=image).text_annotations

    client = pymongo.MongoClient("mongodb+srv://deepjyotipaul:TmP8LdcF3mPHB3r@cluster0-frj9e.mongodb.net/test?retryWrites=true&w=majority")
    db = client.ymir
    coll=db.records
    coll.insert_one({
        'file': str(x['filename']),
        'text': response[0].description
    })
    client.close()

    return response[0].description

@app.route("/getrecords", methods=['GET'])
def getrecords():
    client = pymongo.MongoClient("mongodb+srv://deepjyotipaul:TmP8LdcF3mPHB3r@cluster0-frj9e.mongodb.net/test?retryWrites=true&w=majority")
    db = client.ymir
    coll=db.records
    rows=coll.find({}, {'_id': False})
    client.close()
    res=[row for row in rows]
    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
