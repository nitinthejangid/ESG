# ESG
1. install python 
	- https://www.python.org/downloads/
	- set path C:\Users\Nitin\AppData\Local\Programs\Python\Python311\Scripts in System env variable path windows
2. install pipenv
	- cmd -> pip install pipenv
3. install 'VS Code'
	- https://code.visualstudio.com/download
4. install python in vscode 
  - in extention tab -> look for python and install
5.  create directry and then execute command in cmd (for ex- SG_Hackthon_22)
		- SG_Hackthon_22> pipenv install django
			- while installing we can note Virtualenv location: for ex -> C:\Users\Nitin\.virtualenvs\SG_Hackthon_22-4Y8VUCYZ
6. we need to activate virtual env inside the project for that we will use python interpeter
	- SG_Hackthon_22> pipenv shell 
	  - it will become from D:\WORK\SG_Hackthon_22> to (SG_Hackthon_22-4Y8VUCYZ) D:\WORK\SG_Hackthon_22> in cmd logs
7. to create new project in django
	- D:\WORK\SG_Hackthon_22> django-admin startproject esgProject .
8. to start the server
	- D:\WORK\SG_Hackthon_22> py manage.py runserver  or django-admin runserver
	- we can run http://localhost:8000/ 
9. to create app in django 
	- py manage.py startapp esgApp
	- resister esgApp in INSTALLED_APPS in settings.py 
10. click on 'run and debug' in vscode then click on 'create a launch.json file' then select django. next when we go in 'run and debug' we can see start app mark.

GET Rest call
  - http://localhost:8000/esgApp/getAnalyzedData/
