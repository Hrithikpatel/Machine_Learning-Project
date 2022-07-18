# Machine_Learning-Project

## Software and account Requirement.
1. [Github Account](https://github.com)
2. [Heroku Account](https://signup.heroku.com/)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)

Creating conda Enviornmentconda

```
conda create -p <venv> <python==version> -y
```
Activating Conda

```
conda activate <venv>/
```

Installing requirements.txt file

```
pip install -r requirements.txt
```

To Add files to git

```
git add .

OR

git add <file_name>
```
Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status

```
git status
```

To check all version maintained by git

```
git log
```
To create version/commit all changes by git

```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```
To check remote url

```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information
```
HEROKU_EMAIL = hrithikpatel200@gmail.com
HEROKU_API_KEY = <493db163-7151-4a5a-9766-5f9110572684>
HEROKU_APP_NAME = ml-regressionn
```
BUILD DOCKER IMAGE

```
docker build -t <image_name>:<tagname> .
Note: Image name for docker must be lowercase
```
To list docker image

```
docker images
```
Run docker image

```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```
To check running container in docker

```
docker ps
```
Tos stop docker conatiner

```
docker stop <container_id>
```

```
python setup.py install

```

Install ipykernel

pip install ipykernel

Data Drift: When your datset stats gets change we call it as data drift