# California-Housing-Price-Prediction

The project is about building an end-to-end Machine learning project in which I crated a simple web app where a user can enter some information and model will predict the house price. I have used GitHub actions and Docker for Deployment creating CI/CD pipelines and then deployed it in Heroku Cloud. Please click on below click to see it in action

[https://california-housing-docker.herokuapp.com/](https://california-housing-docker.herokuapp.com/)

Software and tools required for this project
1. [Github](https://github.com)
2. [VS Code](https://code.visualstudio.com)
3. [Heroku Account](https://heroku.com)
4. [Git CLI](https://git-scm.com/downloads)

First step is to create a new environment - this will be a good habit since this will ensure one project libraries will not interact with other.
To create a new environment using conda
````
Conda create -p venv python==3.7 -y
````

<b>requirements.txt file</b>  - Mention names of all the libraries required for this project and then can just use below pip command to install all libraries in your newly created environment in one go.
````
pip install -r requirements.txt
````

<b>app.py file </b> - Used Flask library to made this file, it will take inputs and use pickle file to predict output in a web app whose front-end is designed using HTML. Basically, Flask library is used to create lightweight web applications.

Can run this app.py file using 
````
python app.py
````

Next step is to deploy this into a cloud - Heroku cloud is used in this project.
To deploy into Heroku you need
<b> Procfile</b> - It specifies on starting this application in cloud what command need to run first. we use gunicorn for this here.

Note: gunicorn need to be added in requirements.txt file as well.

To deploy this with the help of docker and github actions ie using CI/CD pipelines that means as soon as i push anything into my github it will automatically getdeployed on cloud.

For this you need to create
<b>Dockerfile</b> - Used a base image it will create a new Docker image 

To configure github actions
create .github folder inside workflows 
write main.yaml file in this

<b> Reference for this project </b>
[https://www.youtube.com/watch?v=MJ1vWb1rGwM&ab_channel=KrishNaik](https://www.youtube.com/watch?v=MJ1vWb1rGwM&ab_channel=KrishNaik)





