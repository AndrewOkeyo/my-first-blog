from django.shortcuts import render

from django.http import HttpResponse
import pymysql
import pymysql.cursors
from django.template import Template, Context
from django.template.loader import get_template


def index(request):
    conn = pymysql.connect('127.0.0.1', 'root', '', 'books', charset='utf8mb4', 
                           cursorclass=pymysql.cursors.DictCursor)
    
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM books_book")
        rows = cur.fetchall()
        t = get_template('books/index.html')
    
        return HttpResponse(t.render({'books': rows}))
    



