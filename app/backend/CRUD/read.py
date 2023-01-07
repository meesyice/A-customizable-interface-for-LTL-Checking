from typing import Union
from flask import request

rule_names = ["LTL_Rule_A_ev_B", "LTL_Rule_A_ev_B_ev_C", "LTL_Rule_A_ev_B_ev_C_ev_D",
               "LTL_Rule_Attr_Val_Diff_Persons", "LTL_Rule_Four_Eyes_Principle", "LTL_Rule_A_nex_B_nex_C"]

"""
When we use more than one LTL rule, we use this function to get the LTL rules 
and the corresponding events
""" 
def readLTLRulesAndActivities() -> Union[str, dict]:
    activities = list()
    number = int(request.form['NumberOfRules'])
    for i in range(1, number + 1):
        rule = 'activitiesOfThe' + str(i) + 'Rule'
        activities.append(request.form.getlist(rule))
    expr = changeExpr(request.form['LTL_Rules'])
    dict_data = {removeAllOperator(expr)[i] : activities[i] for i in range(len(activities))}
    return ' '.join(expr).replace('LTL_And', '-').replace('LTL_Or', '+').replace('LTL_RB',')').replace('LTL_LB','('), dict_data

"""
remove operators from our expression
"""
def removeAllOperator(expr):
    return [value for value in expr if value != 'LTL_And' and value != 'LTL_Or' and value != 'LTL_LB' and value != 'LTL_RB']

"""
Add numbers to each ltl rule
"""
def changeExpr(expr):
    expr = expr.split()
    for name in rule_names:
        counter = 0
        while name in expr:
            expr[expr.index(name)] = name + '_' + str(counter)
            counter += 1
    return expr