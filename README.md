# Blog ( Django & PostgreSql & BootStrap & Ajax)
### Blog-Post website 
![Capture](https://user-images.githubusercontent.com/71823327/109257732-098c5880-780e-11eb-85c1-a5affe60addf.PNG)
![3](https://user-images.githubusercontent.com/71823327/109257722-05f8d180-780e-11eb-9c29-1244c9f7aa25.PNG)
## Short description
This code is Django project website that people can post in it and enjoy reading or surffung the website.
We have three groups in this project.
There is no  seperated UI for the following groups to do their relevant jobs .
These groups utilize django admin for supplementing their task optimally.
1. Admin (superuser)
* Can control all the site
2. Editor
* Can confirm or reject the post also  posts somthing
3. Wirter
* Can post and active or deactive it
4. Simple user
* Can comment, like or dislike the post
## How to run this project
1. cd to root directory
2. Install requirements
* `pip install -r requirements`
3. Set your database configuration if your not using `sqlite` in `settings_local.py` (you have to create `settings_local.py` get help from settings_local_sample.py)
* `SECRET_KEY = 'SECRET_KEY'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DATABASENAME',
        'USER': 'USERNAME',
        'PASSWORD': 'PASSWORD',
        'HOST': 'HOST'
    }
}`

5. Run initial command
* `python manage.py creategroups`
6. Create superuser
* `python manage.py createsuperuser`
7. Now create your table.
* `python manage.py migrate` 
8. Runserver
* `python manage.py runserver`
9. Now create some category when you are admin in your panel
10. Also you have to specifiy your main content of site (what the site is generally about) and choose some high quality image with some describing sentence for it.
Then you have to set thise data when you are in admin postion in to your data base.(Its about model MainContent in my code.)
10. Now create some writers , simple users and editors.
11. Now you can enjoy the website by add some post in django admin (Remember the post should be active and confirm for displaying in the website (this is a rule))
## Features
1. Like or dislike a post
2. Comment and edit comment
3. Simple search (live search with Ajax) & professional search
4. Post a post
5. Edit post
6. enroll user
7. Using some tags for post
8. Nested category
9. Active and confirm a post
