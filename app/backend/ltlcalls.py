import pm4py.algo.filtering.log.ltl as ltl
from enum import Enum 
from pm4py import read_xes
class LTL_Rule(Enum):
    A_ev_B = 1
    A_ev_B_ev_C = 2
    A_ev_B_ev_C_ev_D = 3
    A_nex_B_nex_C = 4
    four_eye = 5
    val_diff_person = 6
""" 
choose_filter is a function that recieves a log file and an ltl rule and some activities and then based on what ltl rule has been chosen the log file will get filtered
"""
filtered_log = None
def choose_filter(file, filter_type: LTL_Rule,*args):
                  
    match filter_type :
       #1st rule : A eventually B
        case LTL_Rule.A_ev_B:
            filtered_log = ltl.ltl_checker.A_eventually_B(file, *args)
       #2nd rule : A eventually B evenetually C 
        case LTL_Rule.A_ev_B_ev_C:
            filtered_log = ltl.ltl_checker.A_eventually_B_eventually_C(file, *args)
        #3rd rule : A eveventually B eventually C eventually D
        case LTL_Rule.A_ev_B_ev_C_ev_D:
            filtered_log = ltl.ltl_checker.A_eventually_B_eventually_C_eventually_D(file,*args)
        #4th rule : A next to B next to C 
        case  LTL_Rule.A_nex_B_nex_C:
            filtered_log = ltl.ltl_checker.A_next_B_next_C(file,*args)
        #5th rule : four eyes principle
        case  LTL_Rule.four_eye:
            filtered_log = ltl.ltl_checker.four_eyes_principle(file,*args) 
        #6th rule : value different persons
        case  LTL_Rule.val_diff_person:
            filtered_log = ltl.ltl_checker.attr_value_different_persons(file,*args)
        case _ :
            filtered_log = None

    return filtered_log 
