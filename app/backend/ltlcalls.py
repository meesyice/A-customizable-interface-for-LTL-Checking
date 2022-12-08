import pandas as pd
import pm4py.algo.filtering.log.ltl as ltl
from enum import Enum
from pm4py import convert_to_dataframe

"""
Enum of all LTL rules provided by pm4py.
"""
class LTL_Rule(Enum):
    A_ev_B = 1
    A_ev_B_ev_C = 2
    A_ev_B_ev_C_ev_D = 3
    A_nex_B_nex_C = 4
    four_eye = 5
    val_diff_person = 6


""" 
apply_filter is a function that recieves a log file and an ltl rule and some activities and 
then based on what ltl rule has been chosen the log file will get filtered
"""
def apply_filter(file, filter_type: LTL_Rule, events):
    match filter_type:
       # 1st rule : A eventually B
        case LTL_Rule.A_ev_B:
            filtered_log = ltl.ltl_checker.A_eventually_B(
                file, events[0], events[1])
       # 2nd rule : A eventually B evenetually C
        case LTL_Rule.A_ev_B_ev_C:
            filtered_log = ltl.ltl_checker.A_eventually_B_eventually_C(
                file, events[0], events[1], events[2])
        # 3rd rule : A eveventually B eventually C eventually D
        case LTL_Rule.A_ev_B_ev_C_ev_D:
            filtered_log = ltl.ltl_checker.A_eventually_B_eventually_C_eventually_D(
                file, events[0], events[1], events[2], events[3])
        # 4th rule : A next to B next to C
        case  LTL_Rule.A_nex_B_nex_C:
            filtered_log = ltl.ltl_checker.A_next_B_next_C(
                file, events[0], events[1], events[2])
        # 5th rule : four eyes principle
        case  LTL_Rule.four_eye:
            filtered_log = ltl.ltl_checker.four_eyes_principle(
                file, events[0], events[1])
        # 6th rule : value different persons
        case  LTL_Rule.val_diff_person:
            filtered_log = ltl.ltl_checker.attr_value_different_persons(
                file, events[0])
        case _:
            filtered_log = None

    return filtered_log


def choose_filter(filter_name):
    match filter_name:
        case 'A eventually B':
            return LTL_Rule.A_ev_B
        case 'A eventually B eventually C':
            return LTL_Rule.A_ev_B_ev_C
        case 'A eventually B eventually C eventually D':
            return LTL_Rule.A_ev_B_ev_C_ev_D
        case 'A next to B next to C':
            return LTL_Rule.A_nex_B_nex_C
        case 'Four eyes principle':
            return LTL_Rule.four_eye
        case 'Value different persons':
            return LTL_Rule.val_diff_person

""" 
OR is a function that combine filtered logs by keeping the events that satisfy at least one filter. 
Events are represented as list of lists where list i correspond to filter i .
Converting our log file to data frames allows us to use some useful preimplemented panda functions like drop_duplicates().
We return the concatenation of the data frames after the filtering happened and we drop any duplicates.
"""
def OR(file, filters: LTL_Rule, events: list[list[str]]):
    dataframes = []
    i = 0 
    for filter in filters:
        dataframes.append(convert_to_dataframe(apply_filter(file, filter, events[i])))
        i+=1
    if len(dataframes[0]) == 0:
        return dataframes[1]
    elif len(dataframes[1]) == 0:
        return dataframes[0]
    else:
        return pd.concat(dataframes).drop_duplicates().reset_index(drop=True)

""" 
AND is a function that combine filtered logs by keeping the events that satisfy both filters. 
Events are represented as list of lists where list i correspond to filter i .
Converting our log file to data frames allows us to use some useful preimplemented panda functions like drop_duplicates().
We return the intersection of the data frames after the filtering happened and we drop any duplicates.
"""
def AND(file, filters: LTL_Rule, events: list[list[str]]):
    dataframes = []
    i = 0
    for filter in filters:
        dataframes.append(convert_to_dataframe(apply_filter(file, filter, events[i])))
        i+=1
    if len(dataframes[0]) == 0 or len(dataframes[1]) == 0:
        return pd.DataFrame()
    else:
        return pd.merge(dataframes[0],dataframes[1], how='inner').drop_duplicates()
