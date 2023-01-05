import re, json
from pm4py import write_xes, read_xes

from app.backend.CRUD.read import readLTLRulesAndActivities

"""
Apply LTL rules to process the file and overwrite the original file with the processed file
"""    
def writeFile(file_path):
    # get LTL Rules and then we need parse them
    rules, activities = readLTLRulesAndActivities()
    print(rules, '\n', activities)