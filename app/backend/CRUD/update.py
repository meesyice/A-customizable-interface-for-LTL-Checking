from flask import request
from pm4py import write_xes, read_xes

from app.backend.ltlcalls import apply_filter, choose_filter, AND, OR
from app.backend.CRUD.read import readFiltersAndEvents

"""
Apply LTL rules to process the file and overwrite the original file with the processed file
"""    
def writeFile(file_path):
    # get LTL Rules and then we need parse them
    rules = request.form['LTL_Rules']
    num = int(request.form['NumberOfRules'])
    activities = readActivities(num)
    print(rules, activities)
    # match composition:
    #     case 'none':
    #         filterd_log = apply_filter(read_xes(file_path), 
    #             choose_filter(request.form['LTL_rule_1']), request.form.getlist('activitiesOfThefirstRule'))
    #     case 'and':
    #         filters, events = readFiltersAndEvents()
    #         filterd_log = AND(read_xes(file_path), filters, events)
    #     case 'or':
    #         filters, events = readFiltersAndEvents()
    #         filterd_log = OR(read_xes(file_path), filters, events)
    # write_xes(filterd_log, file_path)
    
def readActivities(number):
    activities = list()
    for i in range(1, number + 1):
        rule = 'activitiesOfThe' + str(i) + 'Rule'
        activities.append(request.form.getlist(rule))
    return activities