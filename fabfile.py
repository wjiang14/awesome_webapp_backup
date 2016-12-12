#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Deployment toolkit.
'''

import os, re

from datetime import datetime
from fabric.api import *

env.user = 'michael'
env.sudo_user = 'root'
env.hosts = ['192.168.0.3']

db_user = 'root'
db_password = 'root'