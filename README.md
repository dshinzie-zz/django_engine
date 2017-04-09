# README

### Description
This project is a rewrite of [Rails Engine](https://github.com/dshinzie/rails-engine) in Python and Django from Ruby on Rails. Django Engine builds a JSON API with the SalesEngine data schema using Django Rest Framework.

### Instructions
To set up the application, run the following commands in the order listed:
  * ```python manage.py makemigrations```
  * ```python manage.py migrate```
  * ```python -m api.scripts.load_data```  

* How to run the test suite
  * ```./manage.py test``` from the root directory

### Database Schema
![database schema](https://cloud.githubusercontent.com/assets/12074778/20814767/466658fa-b7d8-11e6-8faf-800d8e4e4aca.png)
