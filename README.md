# UOCIS322 - Project 2 #

This project we used Docker and Flask to host a webpage client server relationship.
  
## Completeing the Project 2

* In this project we update the Dockerfile to my data

* Make my Credentials.ini for the skeliton provided

* edit the app.py and build the simple flask app image using Docker

## Tasks

The goal of this project was to implement a "file checking" logic, while also adding configuration reading to your Python script.

* If a file exists in `web/pages/` then our sciprt in app.py has a error handling for the fallowing:
    * `web/pages/404.html` will display "File not found!"
    * `web/pages/403.html` will display "File is forbidden!"
    * `200/OK`

    ⚠️ NOTE: a request contains illegal characters (`..` or `~`)

* Add a configuration parsing logic `app.py` so that it looks for `credentials.ini`, and if not found `default.ini`, and reads the port number and debug mode from the file found.

* Update your name and email in `Dockerfile`. Update `README` with your name, info, and a brief description of the project 

* After that Project is Completed

##Project 2 Function

The function of P2 was to introduce flask and docker fundimentals to a person with little to no background and make them comfortable.

*To Create a server that handles get requests forma client on a network.
 
An unforseen was geting people familiar with WSL since the deparment servers decided to be singy. 



## Authors

Daniel Willard
