import os
from pm4py import write_xes, read_xes
from app import app
from werkzeug.utils import secure_filename
from app.backend.CRUD.read import readLTLRulesAndActivities
from app.backend.ltlcalls import Conversion, apply_rule
from app.backend.deviation import first_3_Deviating_Cases, variants

"""
Apply LTL rules to process the file and overwrite the original file with the processed file
"""    
def writeFile(file_path):
    # get LTL Rules and then we need parse them
    expr, activities = readLTLRulesAndActivities()
    expr = Conversion(len(expr)).infixToPostfix(expr).replace('-',' LTL_And ').replace('+', ' LTL_Or ')
    result_path = os.path.join(app.config['UPLOAD_DIRECTORY'], secure_filename('result.xes'))
    input_log = read_xes(file_path)
    filtered_log = apply_rule(input_log, expr.split(), activities)
    write_xes(filtered_log, result_path)
    deviating_cases_path = os.path.join(app.config['UPLOAD_DIRECTORY'], secure_filename('deviating_cases.xes'))
    deviating_cases = first_3_Deviating_Cases(input_log, filtered_log)
    write_xes(deviating_cases, deviating_cases_path)
    var = variants(filtered_log).reset_index(drop=True)
    var_path = os.path.join(app.config['UPLOAD_DIRECTORY'], secure_filename('variants.xes'))
    with open(var_path, 'w') as f:
        f.write(var.to_json())
    return deviating_cases.drop(columns=['_merge']).to_html() , var.to_html()
    