from flask import Flask
from datetime import datetime
import re
from flask import render_template, request, redirect, url_for
import json


class scratchlessonplan:



    def scratcheasy():
        return render_template("scratcheasy.html")