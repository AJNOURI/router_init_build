__author__ = 'AJ NOURI'

import jinja2
import os

varDict = {}
varDict['login'] = 'admin'
varDict['password'] = 'cisco'
varDict['hostname'] = 'IOU1'
varDict['domain'] = 'cciethebeginning.wordpress.com'

lst = [varDict]

print lst[0]['login']

loader = jinja2.FileSystemLoader(os.getcwd())
jenv = jinja2.Environment(loader=loader, trim_blocks=True,lstrip_blocks=True)
template = jenv.get_template('main-config.jj2')

with open(varDict['hostname']+"_initial-config.cfg", "wb") as conf_file:
        conf_file.write(template.render(lst=lst))

#TODO: error
#http://stackoverflow.com/questions/4531941/typeerror-unhashable-type-dict-when-dict-used-as-a-key-for-another-dict
"""
login
password
hostname
domain

"""
