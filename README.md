# Recycling Prototype
This repo contains the code used in the waste application in our thesis project Utilizing Machine Learning to Help People Sort Recyclable Items. 

## Clone Repo
Go to the directory where you want to clone the repo, for example:
```
cd C:\Users\username\OneDrive\Documents\Project
```
Clone the repo in the directory
```
git clone https://code.pot.cybercom.com/scm/tw/claudiaselina_thesis2022.git
cd claudiaselina_thesis2022
```

## Dependencies
* Visual Studio Code (recommended)
* Python (make sure it's a version that TensorFlow supports)
* Flask
* TensorFlow
* Numpy
* Pillow

## Launch on Mac
Run the application by entering the following in the terminal: 
FLASK_APP=index.py flask run 

The application will then run at "localhost:5000".

## Launch on Windows
Enter the following in the terminal of the prototype directory: 
```
set FLASK_APP=index.py
$env:FLASK_APP="index.py"
```
And then run the application in the same terminal using: 
```
python -m flask run 
```

#### Could not import PIL-image error message
If you are getting an internal server error when submitting the image in the front end application try this: 
```
pip install --upgrade tensorflow keras numpy pandas sklearn pillow
```
Afterwards re-open the project and do the steps again provided in the guide for Windows
