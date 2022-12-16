import re, json
from pm4py import write_xes, read_xes

from app.backend.CRUD.read import readLTLRulesAndActivities

"""
Apply LTL rules to process the file and overwrite the original file with the processed file
"""    
def writeFile(file_path):
    # get LTL Rules and then we need parse them
    rules, activities = readLTLRulesAndActivities()
    json_file = saveAsJSON(activities)
    print(json_file)
    
"""
transfer activities to a json file
"""
def saveAsJSON(activities:list):
    # rules = re.split('LTL_And|LTL_Or', rules.replace('(','').replace(')','').replace(' ',''))
    res = dict()
    for index in range(len(activities)):
        # res[rules[index]] = activities[index]
        res[str(index)] = activities[index]
    return json.dumps(res)