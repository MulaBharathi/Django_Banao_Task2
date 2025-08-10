# Django Blog System for Doctors and Patients

This is a simple Django blog application integrated with a user system where **Doctors** can create and manage blog posts, and **Patients** can view published posts categorized by health topics.


## Setup Instructions

## **Clone the repository**

```
git clone https://github.com/MulaBharathi/Django_Banao_Task2
cd Django_Banao_Task2
```

## Install dependencies

```
pip install -r requirements.txt
```

## Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

## Create a superuser (admin user)

```
python manage.py createsuperuser
```

## Run the development server

```
python manage.py runserver
```

## admin panel
```
http://127.0.0.1:8000/admin/
```

## For Doctors
## Create a new blog post:

```
http://127.0.0.1:8000/doctor/blog/create/
```
(Shows the form for doctors to add new blog posts)

## View all blog posts created by the logged-in doctor:

```
http://127.0.0.1:8000/doctor/blog/posts/
```
(Lists all posts by that doctor, including drafts)

## For Patients
## View all published (non-draft) blog posts:

```
http://127.0.0.1:8000/blogs/
```


## Lists all blog posts visible to patients
```
http://127.0.0.1:8000/blogs/category/1/
```
(Shows posts only from category with ID1)
