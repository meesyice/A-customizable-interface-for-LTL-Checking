from flask import request

"""
When we use more than one LTL rule, we use this function to get the LTL rules 
and the corresponding events
""" 
def readLTLRulesAndActivities():
    activities = list()
    number = int(request.form['NumberOfRules'])
    for i in range(1, number + 1):
        rule = 'activitiesOfThe' + str(i) + 'Rule'
        activities.append(request.form.getlist(rule))
    rules = request.form['LTL_Rules']
    return rules, activities