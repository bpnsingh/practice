# save following snippet as robot file(blog.robot)
*** Settings ***
Library    SeleniumLibrary
Library    blog.py

*** Test Case ***
Go To Blog Using Driver From Python File
  Open Browser    http://www.google.com    chrome
  # a keyword added in python which navigates to blog using driver initiated in robot-framework
  Go To Blog
