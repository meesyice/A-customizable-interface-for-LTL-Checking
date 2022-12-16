import pandas as pd
import pm4py.algo.filtering.log.ltl as ltl
from enum import Enum
from pm4py import convert_to_dataframe , read_xes
from ltlcalls import OR , AND , LTL_Rule

def diff(df1,df2):
    return  pd.merge(convert_to_dataframe(df1),convert_to_dataframe(df2),indicator = True, how='left').loc[lambda x : x['_merge']!='both']

def dev_log(file):
    file = convert_to_dataframe(file).drop_duplicates(subset=["case:concept:name"], keep="first")
    if len(file)>3 :
        return file.iloc[:3]
    else :
        return file

def dev_log_all(file):
   return convert_to_dataframe(file).drop_duplicates(subset=["case:concept:name"], keep="first")
    
def dev_event(file):
    return convert_to_dataframe(file).loc[:,['concept:name']]

df1= read_xes("/Users/fares/github/A-customizable-interface-for-LTL-Checking/tests/data/running-example.xes")
df2= OR(df1,[LTL_Rule.A_ev_B,LTL_Rule.four_eye], [["decide","examine thoroughly"],["reject request",None] ]  )

print(convert_to_dataframe(df1))
print("---------------------------------")
print(convert_to_dataframe(df2))
print("---------------------------------")
print(diff(df1,df2))
print("---------------------------------")
print(dev_log_all(diff(df1,df2)))
print("---------------------------------")
print(dev_log(diff(df1,df2)).loc[:,['concept:name']])
