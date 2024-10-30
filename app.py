import os
import cv2
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
 return render_template('pagina.html')

@app.route('/image/<filename>')
def uploaded_file(filename):
    file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(file)

@app.route('/upload', methods=['POST'])
def upload_image():
 if 'image' not in request.files:
  return jsonify({'error': 'No image file uploaded'}), 400

    #to do
 
 # Return the image file, IP, and datetime in JSON response
  return jsonify({

    #to do2
    
 })
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)