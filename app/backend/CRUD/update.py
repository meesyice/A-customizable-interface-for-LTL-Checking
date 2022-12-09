from flask import request
from pm4py import write_xes, read_xes

from app.backend.ltlcalls import apply_filter, choose_filter, AND, OR

"""
Apply LTL rules to process the file and overwrite the original file with the processed file
"""    
def writeFile(file_path):
    ltl_rule_1 = request.form['LTL_rule_1']
    events_1 = request.form.getlist('activitiesOfThefirstRule')
    composition = request.form['andOr']
    # if composition != 'none':
    #     ltl_rule_2 = request.form['LTL_rule_2']
    #     events_2 = request.form.getlist('activitiesOfThesecondRule')
    match composition:
        case 'none':
            filterd_log = apply_filter(read_xes(file_path), choose_filter(ltl_rule_1), events_1)
        case 'and':
            filters = []
            filters.append(request.form['LTL_rule_1'])
            filters.append(request.form['LTL_rule_2'])
            events = []
            events.append(request.form.getlist('activitiesOfThefirstRule'))
            events.append(request.form.getlist('activitiesOfThesecondRule'))
            print(file_path, filters, events)
            filterd_log_log = AND(read_xes(file_path), filters, events)
        case 'or':
            filters = []
            filters.append(request.form['LTL_rule_1'])
            filters.append(request.form['LTL_rule_2'])
            events = []
            events.append(request.form.getlist('activitiesOfThefirstRule'))
            events.append(request.form.getlist('activitiesOfThesecondRule'))
            filterd_log = OR(read_xes(file_path), filters, events)
    write_xes(filterd_log, file_path)