from flask import request
from pm4py import write_xes, read_xes

from app.backend.ltlcalls import apply_filter, choose_filter, AND, OR
from app.backend.CRUD.read import readFiltersAndEvents

"""
Apply LTL rules to process the file and overwrite the original file with the processed file
"""    
def writeFile(file_path):
    ltl_rule_1 = request.form['LTL_rule_1']
    events_1 = request.form.getlist('activitiesOfThefirstRule')
    composition = request.form['andOr']

    match composition:
        case 'none':
            filterd_log = apply_filter(read_xes(file_path), choose_filter(ltl_rule_1), events_1)
        case 'and':
            filters, events = readFiltersAndEvents()
            filterd_log = AND(read_xes(file_path), filters, events)
        case 'or':
            filters, events = readFiltersAndEvents()
            filterd_log = OR(read_xes(file_path), filters, events)
    write_xes(filterd_log, file_path)