# STL Properties Extraction
A small web app where you can upload you stl file and the app finds properties of the stl file.\
\
It can extract properties of shape such as:
* Volume
* Sufrace Area
* Length
* Width and Height - in non cirular shape
* Diameter - in cirular shape

## Setup the env
Install required modules stated in requirements.txt file

You better create a Virtual Environment to not interfer with your other projects

## Run 
After installing modules, locate to project root folder and run:
```
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver
```
If server runs, it will give you a link to open the app. 


## Endpoints
The app has only two pages.\
**Home page** - to upload the stl file, after submitting file it will redirect you to stl/<id_of_stl_obj> page to display details\
**stl/<id_of_stl_obj>**  - Display details of a prevoisly stored propeties of stls identified by id. 
