1. Install django and dependencies using pip

```py 
pip install django
pip install django-cors-headers
pip install djangorestframework
```
2. Go to backend folder
3. To run the server:
```py 
python manage.py runserver 5001
```
5001 is the port number you want to initialze the server at

4. Go to frontend folder/pokemon_the_series
5. Install the necessary dependencies:
```py 
npm install
```
6. To run the frontend website:
```py 
npm start

```
7. Post the schema and the documents to Solr by running:
``` bash
bash startup.sh
```
or 
``` bash
bash startup_afonso.sh
```
If you have Solr installed in your system and not Docker;

