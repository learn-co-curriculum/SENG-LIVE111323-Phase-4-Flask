# OBJECTIVES
## Deployment -- Deploying a Flask App with Render


Explain what it means to deploy an application
Observe how to configure an application for deployment
Observe how to deploy an application to render

## Checklist 
* Sign up for Render https://dashboard.render.com/register
* Connect your GitHub account. 
* Install PostgreSQL (You can skip this step if postgres is installed)
* PostgreSQL Window
    `sudo apt update`
    `sudo apt install postgresql postgresql-contrib libpq-dev`
    `psql --version`
    `sudo service postgresql start`
    Create a database user, check what your operating system user name is
    `whoami`
    `sudo -u postgres -i`
    `createuser -sr your_user_name_here`
* PostgreSQL Mac
    `psql --version`
    `brew install postgresql`
    `brew services start postgresql`

* Create a Database on Render (skip this portion if you already have a Postgres instance on Render)
    * On the dashboard click `New +` and select `PostgresSQL`
    * Name the database something generic like `postgres_instance` or `my_database`
    * Set the PostgreSQL version to 15
    * Scroll to the bottom and click `Create Database`
* Create a flask app
    * Useful libraries: 
        -python-dotenv (to save environment variables if it want it to be secure)
        -gunicorn 
        -psycopg2-binary 
        

    * In app add `import os` and `from dotenv import load_dotenv` set app.config['SQLALCHEMY_DATABASE_URI'] os.environ.get('DATABASE_URI') 
    * Create a .evn file
    Note: https://github.com/motdotla/dotenv Dot env will allow you to set environment variables. 
* Create a file requirements file that will be used by Render with `$pipenv requirements > requirements.txt`
* At this point, create at least one model and one route to test your Flask Web API. 

* Start to build out the React Client with at least one component that a request to the test route you built for your backend. 
    Note: Your React app and server should be in the same directory. The root directory structure should look like this.
    |- client 
    |- server
    |- .env
    |- .gitignore
    |- Pipfile
    |- Pipfile.lock
    |_ requirements.tx

* Configure your client by creating a static react app.
* In your client’s package.json add a proxy server `"proxy": "http://localhost:5555",`
* Remove `http://localhost:5555/` from any of your fetch requests but keep the endpoint. For example: A GET all to productions should only be passed the end point ‘/productions as the url. 

* In the root directory of your app run ` npm install --prefix client`
* Run `npm run build --prefix client`
* Note: You’ll notice there’s a new build folder in the client folder. This is your static app

* Configure your Client routes. Our web API will interfere with our routes from react-router, so we must handle them on our server. 
* In app.py add:

```python
app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build'
)
@app.route('/')
@app.route('/<int:id>')
def index(id=0):
    return render_template("index.html")
```
Create a local environment variable that connects to your render db. 
On your Dabases page on Render, click the ‘Connect’ select the External Connections tab, and copy the “External Database URL” 
In the .env file, create an environment variable ‘DATABSAE_URI’ and set it to the external database URL. IMPORTANT: replace postgres with postgresql 
Migrate your database 
Migrate your database 
flask db init
flask db revision --autogenerate -m ‘Create tables’
flask db upgrade
Test your app locally to make sure it works by running `gunicorn --chdir server app:app`
Push to GitHub
Create a repo on git hub
Connect your local project to get hub.
`git remote add origin git@github.com:<your-github-name>/your-repo-name.git`
`git add .`
`git commit -m ‘my first commit’
`git push origin main`
Create the Web Service on Render
On the Render dashboard click `New +` and select Web Service.
Connect your repo by selecting it from ‘connect a repository’ or passing render the repository’s URL
Name your application
Change the “Build Command” to 
`pip install -r requirements.txt && npm install --prefix client && npm run build --prefix client`

Change the “Start Command” to
`gunicorn --chdir server app:app`
Scroll down and click Advance 
Add Environment Variable `PYTHON_VERSION` as 3.8.13
Add Environment Variable `DATABASE_URI``
In a new tab open your Postgres instance on Render. Click “Connect” and copy the Internal Database Url
Past that url as the value for `DATABASE_URL` IMPORTANT: In the url replace postgres with postgresql 
Create your webserver and get a snack!!!
