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

docker build -t ml-project:latest

# Note: Image name for docker must be in lowercase

