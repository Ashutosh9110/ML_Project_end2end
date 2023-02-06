# ML_project_end2end



conda create -p venv python==3.7 -y

conda activate venv/

pip install -r requirements.txt

# git status

# git add . == Uploads all the files or to add specific file == git add file_name

# git remove == Can be used to remove a file from the repository

# git log == it tells you about the information about the repository, who has made it and the date of the repository, also it tells you about 
# all the versions maintained by git.

# git ignore == when you don't want to include any file in the repository, include that file name in this file.

# git commit -m "message" == To create a version or commit all changes by git.

# git remote -v == To check the remote url

# git branch == To know the name of the branch

# git push origin main == To send changes to the git repository.


# git add . >> git commit -m "message" >>  git push origin main == That is how you commit new changes in the repository.

# Build Docker imagex

# docker build -t <image_name>: <tagname>

docker build -t ml-project:latest .

# Note: Image name for docker must be in lowercase

# To list docker images == docker images

# How to run docker image == run docker image

docker run -p 5000:5000 -e PORT=5000 09605b8ac3ff
docker run -p 5000:5000 -e PORT=5000 3c33ed04633c
# -e PORT == Environment varible port. We are choosing it as 5000
# 09605b8ac3ff == is the image id

```
To check running container : docker ps

To stop docker container == docker stop (container_id)
# Container id can be found in the docker ps (only the first four characters are enough to stop the container)

python setup.py install

pip install -e .