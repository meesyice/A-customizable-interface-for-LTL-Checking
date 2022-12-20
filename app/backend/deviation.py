import pandas as pd
import pm4py.algo.filtering.log.ltl as ltl
from enum import Enum
from pm4py import convert_to_dataframe , read_xes
from ltlcalls import OR , AND , LTL_Rule

class Deviation(Enum):
    deviatied_log= 1
    first_3 = 2
    deviated_events = 3
# def deviated(df1,df2,Dev:Deviation):
#     match Deviation:
#         case Deviation.deviatied_log:
#             return pd.merge(convert_to_dataframe(df1),convert_to_dataframe(df2),indicator = True, how='left').loc[lambda x : x['_merge']!='both']
#         case Deviation.first_3:
#             count=0 
#             xs=convert_to_dataframe(diff(df1,df2))['case:concept:name'].values.tolist()
#             li = list(map(int,xs))
#             for i in range(0,len(li)):
#                 if count == 3:
#                     count = i
#                     break
#                 if li[i] != li[i+1]:
#                     count += 1
#             return convert_to_dataframe(file).iloc[:count]
#         case Deviation.deviated_events:
#                 return convert_to_dataframe(file).loc[:,['concept:name']]

"""
This function returns the deviated log file
"""
def diff(df1,df2):
    return  pd.merge(convert_to_dataframe(df1),convert_to_dataframe(df2),indicator = True, how='left').loc[lambda x : x['_merge']!='both']

"""
This function takes a deviated log file as an input and gives us only the first 3 deviations back
"""
def first_3_Deviating_logs(file):
    count=0 
    xs=convert_to_dataframe(diff(df1,df2))['case:concept:name'].values.tolist()
    li = list(map(int,xs))
    for i in range(0,len(li)):
        if count == 3:
            count = i
            break
        if li[i] != li[i+1]:
            count += 1
        
    return convert_to_dataframe(file).iloc[:count]
"""
This function returns the deviated events back
"""
def dev_event(file):
    return convert_to_dataframe(file).loc[:,['concept:name']]

df1= read_xes("/Users/fares/github/A-customizable-interface-for-LTL-Checking/tests/data/running-example.xes")
df2= OR(df1,[LTL_Rule.A_ev_B,LTL_Rule.four_eye], [["decide","examine thoroughly"],["reject request",None] ]  )

#print(convert_to_dataframe(df1))
#print("filtered log : ---------------------------------")
#print(convert_to_dataframe(df2))
print(" deviation log : ---------------------------------")
print(diff(df1,df2))
print("first 3 ---------------------------------")
print(first_3_Deviating_logs(diff(df1,df2)))
#print(" ---------------------------------")
