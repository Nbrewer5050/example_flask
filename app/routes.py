#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Our flask routes"""

from flask import (flash, g, redirect, render_template, request, session,
                   url_for)

from app import app
from app.forms.name import NameForm
from app.database import get_db, get_all_users, create_user


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route("/dump/users")
def show_all_users():
    users = get_all_users()
    return render_template("all_users.html", users=users)


@app.route('/users', methods=["GET", "POST"])
def get_users():
    # Creating an output dictionary
    out = {"ok": True, "body": ""}
    body_list = []
    if "GET" in request.method:
        # get_all_users() returns all records from the user table
        form = NameForm()
        raw_data = get_all_users()
        for item in raw_data:
            temp_dict = {
                "first_name": item[0],
                "last_name": item[1],
                "hobbies": item[2]
            }
            body_list.append(temp_dict)
        if not body_list:
            body_list.append({})            # This is done so that when we reference the 0th index on lines 47-50 the code doesn't break
        out["body"] = body_list
        return render_template(
            "about_me.html",
            first_name=out["body"][0].get("first_name"),    # This is just for the sake of being an example, you should never do this in a real app.
            last_name=out["body"][0].get("last_name"),      # Ideally in a real app you would not hardcode the index like we've done here.
            hobbies=out["body"][0].get("hobbies"),
            form=form)
    if "POST" in request.method:
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        hobbies = request.form.get("hobbies")
        create_user((first_name, last_name, hobbies))
        flash("Created new user!")
        return redirect(url_for("get_users"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

# # ====================== EXAMPLE CODE ==============================

# app.add_url_rule("/rafael", "index", index)

# We now know what routes are, so let's talk about views
# @app.route('/sample1')
# def sample1():                          # Functions like sample1() that handle application urls are called "view functions".
#     return "<h1>Hello, World!</h1>"     # This is returning a super simple HTML view.


# @app.route('/user/<name>')              # We can specify dynamic components in routes
# def user(name):
#     return "<h1>Hello, %s!</h1>" % name # This allows us to format the string with a variable (name)


# @app.route('/square/<int:number>')      # We can specify a data type for dynamic components.
# def square(number):
#     return ("<h1>%s squared is %s</h1>"
#             % (number, number**2))      # This is a python shortcut for squaring a number.


# @app.route('/countdown/<int:number>')      # We can specify a data type for dynamic components.
# def countdown(number):
#     return "</br>".join([ str(i) for i in range(number, 0, -1) ])

# from flask import request

# @app.route('/agent')
# def agent():
#     user_agent = request.headers.get("User-Agent")
#     return "<p>Your user agent is %s</p>" % user_agent


# from flask import Flask, render_template

# @app.route('/myroute')
# def my_view_function():
#     return render_template("index.html")


# @app.route("/user/<name>")
# def user(name):
#     return render_template("user.html", name=name)

# @app.route('/register', methods=["GET", "POST"])
# def registration_form():
#     form = NameForm()
#     if form.validate_on_submit():
#         first_name = form.first_name.data
#         last_name = form.last_name.data
#         hobbies = form.hobbies.data
#         return ("<h1>Hello, %s %s. Your hobbies are: %s</h1>"
#                 % (first_name, last_name, hobbies))
#     return render_template("form_example.html", form=form)