1.create a use to manage db for this project rather than directly using root(not safe)
	mysql> mysql -u root -p
	mysql> create user 'cielo'@'localhost' identified by '19970108';
	mysql> grant all privileges on final.x to 'cielo'@'localhost';

2.do later: make some input char to uppercase rather than limit input

3.python manage.py inspectdb

 