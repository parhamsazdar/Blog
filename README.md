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
* `pip install -r requirements.txt`
4. Set your database configuration in settings_local.py (get help from settings_local_sample.py)
3. Run initial command
* `python manage.py creategroups`
5. Create superuser
* `python manage.py createsuperuser`
6. Now create your table.
* `python manage.py migrate` 
7. Runserver
* `python manage.py runserver`
8. Now you can enjoy my website by add some post in django admin (Remember the post should be active and confirm for displaying in the website (this is a rule))
## Features
1. Like or dislike a post
2. Comment and edit comment
3. Simple search (live search with Ajax) & professional search
4. Post a post
5. Edit post
6. Using some tags for post
7. Nested category
8. Active and confirm a post
