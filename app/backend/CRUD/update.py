from flask import request
from pm4py import write_xes, read_xes

from app.backend.ltlcalls import apply_filter, choose_filter

"""
Apply LTL rules to process the file and overwrite the original file with the processed file
"""    
def writeFile(file_path):
    ltl_rule_1 = request.form['LTL_rule_1']
    events_1 = request.form.getlist('activitiesOfThefirstRule')
    value = request.form['andOr']
    if value != 'none':
        ltl_rule_2 = request.form['LTL_rule_2']
        events_2 = request.form.getlist('activitiesOfThesecondRule')
    filterd_log = apply_filter(read_xes(file_path), choose_filter(ltl_rule_1), events_1)
    write_xes(filterd_log, file_path)