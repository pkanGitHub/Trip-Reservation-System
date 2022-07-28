
# Trip Reservation System

This is a Python application that simulates a bus seating chart and ticket purchasing tool. The user will navigate web pages 
to input specified information, such as seat location and name, that is then checked against the current seating chart in to prevent double booking a seat. 
The seating chart and total sales will update with each user submission in the admin login section of the application.

---

## Instructions to run the project:

This project requires the installation of [Docker](https://docs.docker.com/get-docker/) to navigate the application.<br>
Once Docker is open, locate the project directory using `cd` command in terminal.<br> 
Type `docker-compose up` in terminal to run.

---

## The user will navigate as follows:

- **User Select** - Admin login or Reserve a seat<br>
     - **Admin login** - User will be prompted to enter correct Admin login information (username and password)
       - The admin user screen will print the current seating chart and current total ticket sales
       - Admin credentials located in `password.txt`
     - **Reservations** - User will be prompted to enter First and Last name, seat row, and seat number
       - The typical user seeking to reserve a seat will also be presented with an updated seating chart and
a form to enter reservation information.

**Application is a static web page and will remain active once initiated**