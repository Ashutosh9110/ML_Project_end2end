FROM python:3.7
COPY . /app

# copy . == This copies all the files o`current directory and paste it into the desired folder. Here /app is the desired folder

WORKDIR /app
# This sets the working directory to the desired directory.Here our working directory is app.
RUN pip install -r requirements.txt
# RUN flask
# RUN gunicorn
EXPOSE $PORT
# Port number will be sent by the environment variable.
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
# This command will be used to run our application