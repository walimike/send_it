# Send It
## Project Overview
__SendIT is a courier service that helps users deliver parcels to different destinations.<br> SendIT provides courier quotes based on weight categories.__

## Badges <br>
[![Build Status](https://travis-ci.org/walimike/send_it.svg?branch=api-v1)](https://travis-ci.org/walimike/send_it)

[![Coverage Status](https://coveralls.io/repos/github/walimike/send_it/badge.svg?branch=api-v1)](https://coveralls.io/github/walimike/send_it?branch=api-v1)

## Main features
1. Users can create an account and log in.
2. Users can create a parcel delivery order.
3. Users can change the destination of a parcel delivery order.
4. Users can cancel a parcel delivery order.
5. Users can see the details of a delivery order.
6. Admin can change the status and present location of a parcel delivery order.  

## Quick Setup
1. Open your terminal.
2. Type in the command git clone and paste in this link https://github.com/walimike/send_it.git.
3. You can now checkout to the develop branch.
4. Create a virtual environment and then `pip install -r requirements.txt`
5. Now run the app using `python run.py`

## UI Demo
The UI demo is hosted on gh-pages on this link:  https://walimike.github.io/send_it/

## The API works as follows:
The url_prefix is `/v1/api/`
1. `GET /parcels` Fetch all parcel delivery orders
2. `GET /parcels/<parcelId>` Fetch a specific parcel delivery order
3. `GET /users/<userId>/parcels` Fetch all parcel delivery orders by a specific user
4. `PUT /parcels/<parcelId>/cancel` Cancel the specific parcel delivery order
5. `POST /parcels` Create a parcel delivery order

#  Authors
Michael Robert Wali
