import main
from main import getPrediction
from flask import Flask, render_template, request, redirect, flash, url_for
import urllib.request
from werkzeug.utils import secure_filename
import os

# Trying out the function
# pred_label = getPrediction('plastic/plastic25.jpg')
# print(pred_label)

UPLOAD_FOLDER = 'static/'
# Full dir: /Users/selinaoberg/Documents/Universitetet/VT-22/Exjobb/Waste_Classificator/uploads/

app = Flask(__name__)                    
app.secret_key = '8662747133' # change value?
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Route to HTML
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/", methods = ['POST']) #/file
# Our function for pushing the image to the classifier model
def submit_image():
     if request.method == 'POST':
          if 'file' not in request.files:
               flash('No file part')
               return redirect(request.url)
          file = request.files['file']
        # Error message if no file submitted
          if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        # Return results predictive data
          if file:
            filename = secure_filename(file.filename)
            # kanske behöver byta till actual dir istället för UPLOAD_FOLDER
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) 
            # getPrediction(filename)
            prediction, filename, transform = getPrediction(filename)
            flash(prediction)
            flash(filename)
            flash(transform)
            # need to flash(filename) too?
            return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

