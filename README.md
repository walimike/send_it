# send_it; Challenge 3
## Project Overview
SendIT is a courier service that helps users deliver parcels to different destinations.<br>
SendIT provides courier quotes based on weight categories.
## Badges <br>
[![Build Status](https://travis-ci.org/walimike/send_it.svg?branch=add-badges)](https://travis-ci.org/walimike/send_it)            [![Coverage Status](https://coveralls.io/repos/github/walimike/send_it/badge.svg?branch=develop-v2)](https://coveralls.io/github/walimike/send_it?branch=develop-v2)                 [![Maintainability](https://api.codeclimate.com/v1/badges/a2aa72f959462adcbbde/maintainability)](https://codeclimate.com/github/walimike/send_it/maintainability)         [![Codacy Badge](https://api.codacy.com/project/badge/Grade/9da0f37eeb8840c680821eaf13dd36c1)](https://www.codacy.com/app/walimike/send_it?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=walimike/send_it&amp;utm_campaign=Badge_Grade)

### Main features
1. Users can create an account and log in.
2. Users can create a parcel delivery order.
3. Users can change the destination of a parcel delivery order.
4. Users can cancel a parcel delivery order.
5. Users can see the details of a delivery order.
6. Admin can change the status and present location of a parcel delivery order.
### Quick Setup
```
1. Open your terminal.
2. Type in the command git clone and paste in this link https://github.com/walimike/send_it.git. 
3. You can now checkout to the develop-v2 branch for version 2 of our API.
4. Create a virtualenv using python3, call the virtualenv venv.
5. Within your virtualenv, pip install -r requirements.txt
6. Now open a different terminal and open up postgres database on your local machine usind sudo su postgres
7. At this point you shall be prompted to enter your password(local host/computer password)
8. Now psql into postgres or anyother databse name available on your machine.
9. We now create a database called sendit_db and another called test_db using CREATE DATABASE sendit_db; and CREATE DATABASE test_db;
10. Now type \q in terminal to quit from postgres and then type psql sendit_db to enter our db
11. At this point, you'll see this: sendit_db=# in your terminal.
12. We shall now alter the password using \password to change the postgres password to 12345
14. Follow instructions 10 to 12 for the test_db
15. Now go back where we downloaded this project and type . venv/bin/activate to activate our virtualenv.
16. You can now run the app using python3 run.py
```
### API Features:

|URL Endpoint	|HTTP Method	|Description|
|-------------|-------------|-----------|
|`/parcels`	|`GET`|	Fetch all parcel delivery orders|
|`/parcels/<parcelId>`|`GET`|	Fetch a specific parcel delivery order|
|`/users/<userId>/parcels`|	`GET`|Fetch all parcel delivery orders by a specific user|
|`/parcels<parcelId>/cancel`|`PUT`|Cancel the specific parcel delivery order|
|`/parcels`|	`POST`|	Create a parcel delivery order|
|`/users`|	`GET`|	Fetch all current users|
|`/auth/signup`|`POST`|Register a user|
|`/auth/login`|`POST `|Login a user|
|`/parcels/<parcelId>/destination`|`PUT `|Change the location of a specific parcel delivery order(CURRENT USER)|
|`/parcels/<parcelId>/status`|`PUT `|Change the status of a specific parcel delivery order(ADMIN)|
|`/parcels/<parcelId>/presentLocation`|`PUT `|Change the present location of a specific parcel delivery order|


# Authors
Michael Robert Wali
