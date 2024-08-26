###REQUIREMENTS
install Python 3.7
# Make virtual environment    
    # Activate virtual environment
    source env/bin/activate
    
    # Install requirements
    pip install -r requirements.txt
        
    # Start the development server
    python manage.py runserver

#### migrate DB changes
    python manage.py migrate
##here we have three apps
1.register: here we have code user register, login, and logout using django 
2.python_code : this app contain all practiced python codes.
3.accuknox : this app contain api urls to create a user and upload the file.
