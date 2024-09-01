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
    * **TO register** - http://127.0.0.1:8000/register/
    * **api curl for search user** - curl --location 'http://127.0.0.1:8000/search_users?user_name=premasj007@gmail.com&page=1'
2.python_code : this app contain all practiced python codes and oops concept.
3.accuknox : this app contain api urls to create a Person with name and age and upload the file.
 * **TO LOgin**  - http://127.0.0.1:8000/login/
 * **To Upload** - http://127.0.0.1:8000/upload/
 * **TO Create Person** - http://127.0.0.1:8000/create/ 
