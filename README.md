# Smart Strategy website

### Setup

#### For Windows  
Create a virtual environment <code>python -m venv venv</code>  
Activate virtual enviroment <code>source venv/Scripts/activate</code>

#### For Mac  
Create a virtual environment <code>python3 -m venv venv</code>  
Activate virtual enviroment <code>source venv/bin/activate</code>

Run <code>pip install -r requirements.txt</code> (pip3 for Mac)  
Run <code>cd frontend; npm install</code>  

Make migrations: <code> cd ../backend; python manage.py migrate </code>
Navigate back to the root directory <code> cd .. </code> 

### Development
Run <code>source dev.sh</code>  

### Production
Run <code>source build.sh</code>  
Run <code>source prod.sh</code>