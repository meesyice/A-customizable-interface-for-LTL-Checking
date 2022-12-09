from flask import request
from app.backend.ltlcalls import LTL_Rule, choose_filter


"""
When we use more than one LTL rule, we use this function to get the LTL rules 
and the corresponding events
""" 
def readFiltersAndEvents() -> tuple[list[LTL_Rule], list[list[str]]]:
    filters = []
    filters.append(choose_filter(request.form['LTL_rule_1']))
    filters.append(choose_filter(request.form['LTL_rule_2']))
    events = []
    events.append(request.form.getlist('activitiesOfThefirstRule'))
    events.append(request.form.getlist('activitiesOfThesecondRule'))
    return filters, events