FROM python:3.7
COPY . /app

# copy . == This copies all the files o`current directory and paste it into the desired folder. Here /app is the desired folder

WORKDIR /app
# This sets the working directory to the desired directory.Here our working directory is app.
RUN pip install -r requirements.txt
# RUN flask
# RUN gunicorn
EXPOSE $PORT 
# Port number will be sent by the environment variable. $ sign sort of gives the assent to use that port number to run our project.
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
# This command will be used to run our application. It is equivalent to the python app.py
# Because of gunicorn we are able to use ubuntu system.
# in the above command, "worker" divides the incoming requests among themselves. For example, if we have 1000 incoming requests, then 4 workers will
# divide them into 250 each.
# Gunicorn: Gunicorn ‘Green Unicorn’ is a Python WSGI (Web Server Gateway Interface)
# HTTP Server for UNIX. It’s a pre-fork worker model ported from Ruby’s Unicorn project.
# The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resource usage, and fairly speedy.
# By using gunicorn, we'll be able to serve your Flask application on more than one thread
# app:app == module_name : flask_object. If file name is app.py, then module_name will be app. Also, the namo of flask_object is app.(go to 
# app.py page : app = Flask(__name__))


# In this, basically what we have done is we have taken a base image which is based on ubuntu system then we had copied the entire files
# inside the app folder and the app folder is available inside the python:3.7. After that we have set our working directory to app