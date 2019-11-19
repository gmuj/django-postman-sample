# django-postman-sample

To setup the project you just need to create a new virtual environment and install requirements.txt using pip

#setup: 
	#make venv 
	virtualenv venv3 --python=python3
	#start venv
	. ./venv3/bin/activate.fish	
	#install requirments
	pip3 install -r requirements.txt   
	# setup db, create backend
	python manage.py migrate
	#run the website example, see output for where to browse to
	python manage.py runserver

	
