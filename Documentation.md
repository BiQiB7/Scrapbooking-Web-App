# Set up
1. Install virtual environment and activate.  [reference](https://linuxhint.com/activate-virtualenv-windows/#:~:text=To%20activate%20virtualenv%20on%20Windows%2C%20first%2C%20install%20the%20pip.,%5CScripts%5Cactivate%E2%80%9D%20command.)
``` 
C:\Users\biqif>pip install virtualenv
C:\Users\biqif\SOProject>virtualenv venvironment 
C:\Users\biqif\SOProject>venvironment\Scripts\activate
```


2. Install below. [reference](https://realpython.com/lessons/setting-up-your-django-app/ )
- pip 22.3.1 `C:\>pip install --upgrade pip`
- Python 3.10.4
- django 2.0  `(venvironment) C:\Users\biqif\SOProject>python -m pip install django==2.0`

3. Start project.
```
(venvironment) C:\Users\biqif\SOProject>django-admin startproject scrappAR
(venvironment) C:\Users\biqif\SOProject>cd scrappAR
(venvironment) C:\Users\biqif\SOProject\scrappAR>python manage.py startapp users
```

4. Modify settings.py, which is found in `C:\Users\biqif\SOProject\scrappAR\scrappAR`. 
- Under INSTALLED_APPS, add 'users'.
- migrate the changes by `(venvironment) C:\Users\biqif\SOProject\scrappAR>python manage.py migrate`
- `(venvironment) C:\Users\biqif\SOProject\scrappAR>python manage.py runserver`

5. add new user by `(venvironment) C:\Users\biqif\SOProject\scrappAR>python manage.py createsuperuser`
