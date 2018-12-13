# coding:utf8
from flask import render_template, redirect, url_for

from . import home


@home.route("/")
def index():
    """主页"""
    return render_template("home/index.html")


@home.route("/login/")
def login():
    """登录页面"""
    return render_template("home/login.html")


@home.route("/logout/")
def logout():
    """登出自动跳转到登录的页面"""
    return redirect(url_for("home.login"))


@home.route("/regist/")
def regist():
    """登录页面"""
    return render_template("home/regist.html")


@home.route("/user/")
def user():
    """会员界面"""
    return render_template("home/user.html")


@home.route("/pwd/")
def pwd():
    """会员界面"""
    return render_template("home/pwd.html")

@home.route("/comments/")
def comments():
    """会员界面"""
    return render_template("home/comments.html")


@home.route("/loginlog/")
def loginlog():
    """会员界面"""
    return render_template("home/loginlog.html")



@home.route("/moviecol/")
def moviecol():
    """会员界面"""
    return render_template("home/moviecol.html")

