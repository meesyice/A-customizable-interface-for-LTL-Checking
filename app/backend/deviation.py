from numpy import append
import pandas as pd
import re
import pm4py.algo.filtering.log.ltl as ltl
from enum import Enum
from pm4py import convert_to_dataframe , read_xes , filter_variants_top_k 


"""
This function returns the deviated log file
"""
def diff(df1,df2):
    if convert_to_dataframe(df2).empty:
        return df1
    else :
        return convert_to_dataframe(df1).merge(convert_to_dataframe(df2), how='left',indicator = True).loc[lambda x : x['_merge']!='both']



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
    if convert_to_dataframe(file).empty:
        return convert_to_dataframe(file)
    else:
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
    string = 'This is variant number 1 :'
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

