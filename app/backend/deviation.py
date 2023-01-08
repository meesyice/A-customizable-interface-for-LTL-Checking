from numpy import append
import pandas as pd
import re
import pm4py.algo.filtering.log.ltl as ltl
from enum import Enum
from pm4py import convert_to_dataframe , read_xes , filter_variants_top_k 
from app.backend.ltlcalls import apply_rule , Conversion

"""
This function returns the deviated log file
"""
def diff(df1,df2):
    if convert_to_dataframe(df2).empty:
        return df1
    else :
        return  pd.merge(convert_to_dataframe(df1),convert_to_dataframe(df2),indicator = True, how='left').loc[lambda x : x['_merge']!='both']


"""
This function takes a deviated log file as an input and gives us only the first 3 deviating cases back
"""
def first_3_Deviating_Cases(df1,df2):
    count=0 
    li=convert_to_dataframe(diff(df1,df2))['case:concept:name'].values.tolist()
    j = 0
    for i in range(0,len(li)):
        if count < 3:
            j = i
        if i < len(li)-1 and li[i] != li[i+1]:
             count += 1
    return convert_to_dataframe(diff(df1,df2)).iloc[:j+1]

"""
This function takes a deviated log file as an input and gives us only the first deviated case back
"""
def first_Deviating_Case(file):
    count=0 
    xs=convert_to_dataframe(file)['case:concept:name'].values.tolist()
    j = 0
    for i in range(0,len(xs)):
        if count < 1:
            j = i
        if i < len(xs)-1 and xs[i] != xs[i+1]:
             count += 1
    return convert_to_dataframe(file).iloc[:j+1]

"""
This function takes a log file as an input and gives us its most commun variants back
"""
def variants(file):
    k=3
    j=1
    frames = []
    string = 'This is variant number 1'
    df = pd.DataFrame([string], columns=['concept:name'])
    frames.append(df)
    frames.append(first_Deviating_Case(convert_to_dataframe(filter_variants_top_k(file,1))))
    for x in range(1,k):
        j+=1
        string = 'This is variant number '+str(j)+' :'
        df = pd.DataFrame([string], columns=['concept:name'])
        frames.append(df)
        frames.append(first_Deviating_Case( convert_to_dataframe(diff(filter_variants_top_k(file,x+1),filter_variants_top_k(file,x)))))
    result = pd.concat(frames).loc[:,['concept:name']]
    return result


expr = 'LTL_Rule_A_ev_B_0 + LTL_Rule_A_ev_B_ev_C_0 - ( LTL_Rule_Attr_Val_Diff_Persons_0 + LTL_Rule_Four_Eyes_Principle_0 ) - LTL_Rule_A_nex_B_nex_C_0'
expr = Conversion(len(expr)).infixToPostfix(expr).replace('-',' LTL_And ').replace('+', ' LTL_Or ')
activities = {'LTL_Rule_A_ev_B_0': ['decide', 'check ticket'], 'LTL_Rule_A_ev_B_ev_C_0': ['check ticket', 'check ticket', 'check ticket'], 'LTL_Rule_Attr_Val_Diff_Persons_0': ['examine casually'], 'LTL_Rule_Four_Eyes_Principle_0': ['check ticket', 'check ticket'], 'LTL_Rule_A_nex_B_nex_C_0': ['pay compensation', 'examine casually', 'register request']}
input_log = read_xes('tests/data/running-example.xes')    
print(convert_to_dataframe(input_log))
filtered_log = convert_to_dataframe( apply_rule(input_log, expr.split(), activities) )
print(filtered_log)
print(convert_to_dataframe(first_3_Deviating_Cases(input_log, filtered_log)) )
