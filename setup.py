#use this file to create the exe file from the given python script

from distutils.core import setup
import glob
import py2exe
import serial
from time import time
import csv
from datetime import datetime

setup(console=["serialread.py"])
