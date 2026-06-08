'''
Library Management System
Problem

Design a library system.

Requirements

Each book should contain:

book id
title
author
availability status

Functionalities
Issue book
Return book
Display availability
Count total books using class variable

Book : 
  property [id,title,author,status =True]
  behaviour: [issue(), submit(), is_available()]
'''


class Book:
    def __init__(self,id,title,author):
        self.__id=id
        self.__title=title
        self.__author=author
        self.__status=True

    def issue(self):
        if self.status