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

class LTL_Bracket(Enum):
    Left = 1
    Right = 2


""" 
apply_filter is a function that recieves a log file and an ltl rule and some activities and 
then based on what ltl rule has been chosen the log file will get filtered
"""
def apply_filter(file, filter_type: LTL_Rule, events: list[str]):
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
            

def choose_Bracket(bracket_name):
    match bracket_name:
        case 'LTL_LB':
            return LTL_Bracket.Left
        case 'LTL_RB':
            return LTL_Bracket.Right
        case _:
            return None

""" 
OR is a function that combine filtered logs by keeping the events that satisfy at least one filter. 
Events are represented as list of lists where list i correspond to filter i .
Converting our log file to data frames allows us to use some useful preimplemented panda functions like drop_duplicates().
We return the concatenation of the data frames after the filtering happened and we drop any duplicates.
"""
def OR(file, filter: LTL_Rule, events: list[str]):
    dataframes = [convert_to_dataframe(file), convert_to_dataframe(apply_filter(file, filter, events))]
    
    if len(dataframes[0]) == 0 and len(dataframes[1]) == 0:
        return None
    elif len(dataframes[0]) == 0:
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
def AND(file, filter: LTL_Rule, events: list[str]):
    apply_filter(file, filter, events)



def parse_mod_ltl(str_LTL_Rule: str):
    parsed_LTL_Rule = []
    for subrule in str_LTL_Rule.split(" "):
        if subrule in ["LTL_LB", "LTL_RB"]:
            parsed_LTL_Rule.append(choose_Bracket(subrule))
        elif subrule in ["LTL_And", "LTL_Or"]:
            parsed_LTL_Rule.append(choose_combiner(subrule))
        elif subrule in ["LTL_A_ev_B", "LTL_A_ev_B_ev_C", "LTL_A_ev_B_ev_C_ev_D", "LTL_A_nex_B_nex_C", "LTL_Four_Eyes_Principle", "LTL_Attr_Val_Diff_Persons"]:
            parsed_LTL_Rule.append(choose_filter(subrule))
        else:
            continue
    return parsed_LTL_Rule

def apply_rule(file, str_LTL_Rule: str, events: list[list[str]]):
    pass
