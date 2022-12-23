from numpy import append
import pandas as pd
import re
import pm4py.algo.filtering.log.ltl as ltl
from enum import Enum
from pm4py import convert_to_dataframe , read_xes , filter_variants_top_k 
from ltlcalls import OR , AND , LTL_Rule

"""
This function returns the deviated log file
"""
def diff(df1,df2):
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




df1=read_xes('/Users/fares/github/A-customizable-interface-for-LTL-Checking/tests/data/roadtraffic.xes')
#df1=read_xes('/Users/fares/github/A-customizable-interface-for-LTL-Checking/tests/data/receipt.xes')

#df1= read_xes('tests/data/running-example.xes')
# print('the whole log :')
# print(convert_to_dataframe(df1))
#df2=OR(df1,[LTL_Rule.A_ev_B,LTL_Rule.four_eye], [["Confirmation of receipt","T04 Determine confirmation of receipt"],
 #                                                       ["T02 Check confirmation of receipt","T04 Determine confirmation of receipt"] ]  ) 
df2=OR(df1,[LTL_Rule.A_ev_B,LTL_Rule.four_eye], [["Create Fine","Send Fine"],
                                                        ["Payment","TInsert Fine Notification"] ]  ) 
#df2=OR(df1,[LTL_Rule.A_ev_B,LTL_Rule.four_eye], [["decide","examine thoroughly"],["reject request",None] ]  )

print('These are the most common variants : ')
print(convert_to_dataframe(variants(df1)))
print('These are the first 3 deviating cases ')
file=first_3_Deviating_Cases(df1,df2)
print(file)
#print(first_Deviating_Case(df1))
#write_xes((variants(df1)),'exported3.xes')
# print('THis is for k=1')
# print(convert_to_dataframe(filter_variants_top_k(df1,1)))
# print('This is for k=2')
# print(convert_to_dataframe(filter_variants_top_k(df1,2)))
# print('This is for k=3')
# print(convert_to_dataframe(filter_variants_top_k(df1,3)))