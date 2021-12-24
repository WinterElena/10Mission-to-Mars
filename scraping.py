#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping


# In[ ]:


app = Flask(__name__)


# In[ ]:


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

