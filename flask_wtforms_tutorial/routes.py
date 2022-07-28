from re import template
from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash
from .forms import *
import numpy
import random
from flask_wtforms_tutorial.total_sales import TotalSales

@app.route("/", methods=['GET', 'POST'])
def user_options():
    
    form = UserOptionForm()
    #check if the request method is POST. POST method means that form data was submitted
    #So, if method is POST we can get the form data 
    if request.method == 'POST' and form.validate_on_submit():
        option = request.form['option']

        if option == "1":
            #if form option is "1" go to the admin page
            return redirect('/admin')
        else:
            #if form option is "2" go to the reservations page
            return redirect("/reservations")
    
    return render_template("options.html", form=form, template="form-template")

@app.route("/admin", methods=['GET', 'POST'])
def admin():

    error = None
    admin_logged_in = False
    total_sales = ""
    Row_list2  = [
            ["O", "O", "O", "O"], 
            ["O", "O", "O", "O"], 
            ["O", "O", "O", "O"], 
            ["O", "O", "O", "O"], 
            ["O", "O", "O", "O"], 
            ["O", "O", "O", "O"], 
            ["O", "O", "O", "O"], 
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"]]

    #read reservations.txt file into list
    with open("reservations.txt") as file:
        lines = file.readlines()
        file_read = []
        row_seat_list = []
        for line in lines:
            list = line.split(", ")
            file_read.append(list)
            row_seat_list.append(list[1:3])

    for z in row_seat_list:
            Row_list2[int(z[0])][int(z[1])] = "X"

    form = AdminLoginForm()

    if request.method == "POST" and form.validate_on_submit():
        username = request.form["username"]
        password = request.form["password"]

        with open("passcodes.txt") as file:
            lines = file.readlines()
            admins = []
            pwds = []

        for line in lines:
            list = line.split(", ")
            admins.append(list[0])
            pwds.append(list[1].replace("\n", ""))

        if username == admins[0] and password == pwds[0]:
            admin_logged_in = True
        elif username == admins[1] and password == pwds[1]:
            admin_logged_in = True
        elif username == admins[2] and password == pwds[2]:
            admin_logged_in = True
        else:
            error = "Wrong username or password, try again"

        if request.method == "GET" and admin_logged_in:
            return redirect(url_for('admin'))
        sales = TotalSales('reservations.txt')
        total_sales = "Total Sales:" + str(sales.get_total_prices())
            
    return render_template("admin.html", form=form, template="form-template", error=error, Row_list2=Row_list2, admin_logged_in=admin_logged_in, total_sales = total_sales)

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():

    submitting_data = False
    Row_list1  = [
            ["O", "O", "O", "O"], 
            ["O", "O", "O", "O"], 
            ["O", "O", "O", "O"], 
            ["O", "O", "O", "O"], 
            ["O", "O", "O", "O"], 
            ["O", "O", "O", "O"], 
            ["O", "O", "O", "O"], 
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"]]

    #read reservations.txt file into list
    with open("reservations.txt") as file:
        lines = file.readlines()
        file_read = []
        row_seat_list = []
        for line in lines:
            list = line.split(", ")
            file_read.append(list)
            row_seat_list.append(list[1:3])

    for z in row_seat_list:
            Row_list1[int(z[0])][int(z[1])] = "X"
 
    form = ReservationForm()
    # getting data from the form once submit
    if request.method == "POST" and form.validate_on_submit():
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        row_choice = int(request.form["row"])
        seat_choice = int(request.form["seat"])
        submitting_data = True

        #check if the seat is already reserved
        if Row_list1[row_choice-1][seat_choice-1] == "X":
            error = f"Error: Row: {row_choice} Seat: {seat_choice} already reserved"
            submitting_data = False
            return render_template("reservations.html", form=form, template="form-template", error=error,
            submitting_data=submitting_data, Row_list1=Row_list1, row_choice=row_choice, seat_choice=seat_choice, 
            first_name=first_name, last_name=last_name)
            
        else:
            #if the seat is not reserved, add the reservation to the file
            combo = first_name + "INFOC"
            mix = []
            for letter in combo:
                mix.append(letter)
            random.shuffle(mix)
            TicketNumber = "".join(mix) + "1040"
            with open("reservations.txt", "a") as file:
                file.write(f"\n{first_name}, {row_choice-1}, {seat_choice-1}, {TicketNumber}")
            Row_list1[row_choice-1][seat_choice-1] = "X"
            
            return render_template("reservations.html", form=form, template="form-template", Row_list1=Row_list1,
            submitting_data=submitting_data, row=row_choice, seat=seat_choice, 
            fname=first_name, lname=last_name, TicketNumber=TicketNumber)

    return render_template("reservations.html", form=form, template="form-template",Row_list1=Row_list1)


