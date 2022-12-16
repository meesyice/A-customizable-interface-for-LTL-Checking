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
    Four_eyes_principle = 5
    Attr_val_diff_persons = 6
    
class LTL_Combiner(Enum):
    And = 1
    Or = 2


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
        case  LTL_Rule.Four_eyes_principle:
            filtered_log = ltl.ltl_checker.four_eyes_principle(
                file, events[0], events[1])
        # 6th rule : value different persons
        case  LTL_Rule.Attr_val_diff_persons:
            filtered_log = ltl.ltl_checker.attr_value_different_persons(
                file, events[0])
        case _:
            filtered_log = None

    return filtered_log


def choose_filter(filter_name):
    match filter_name:
        case 'LTL_A_ev_B':
            return LTL_Rule.A_ev_B
        case 'LTL_A_ev_B_ev_C':
            return LTL_Rule.A_ev_B_ev_C
        case 'LTL_A_ev_B_ev_C_ev_D':
            return LTL_Rule.A_ev_B_ev_C_ev_D
        case 'LTL_A_nex_B_nex_C':
            return LTL_Rule.A_nex_B_nex_C
        case 'LTL_Four_Eyes_Principle':
            return LTL_Rule.Four_eyes_principle
        case 'LTL_Attr_Val_Diff_Persons':
            return LTL_Rule.Attr_val_diff_persons
        case _:
            return None

def choose_combiner(combiner_name):
    match combiner_name:
        case 'LTL_And':
            return LTL_Combiner.And
        case 'LTL_Or':
            return LTL_Combiner.Or
        case _:
            return None
            

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


def parse_mod_ltl(mod_LTL_Rule: str):
    filters = []
    combiners = []
    for subrule in mod_LTL_Rule.split(" "):
        print(subrule)
        if subrule in ["LTL_And", "LTL_Or"]:
            combiners.append(choose_combiner(subrule))
        else:
            filters.append(choose_filter(subrule))
    return filters, combiners

print(parse_mod_ltl("LTL_A_ev_B LTL_Or LTL_A_ev_B_ev_C LTL_And LTL_A_ev_B_ev_C_ev_D"))