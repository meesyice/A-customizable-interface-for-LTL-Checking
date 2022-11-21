#import pm4py
import enum
from numpy import choose
import pm4py.algo.filtering.log.ltl as ltl
from pm4py import read_xes
from enum import Enum 
class LTL_Rule(Enum):
    A_ev_B = 1
    A_ev_B_ev_C = 2
    A_ev_B_ev_C_ev_D = 3
    A_nex_B_nex_C = 4
    four_eye = 5
    val_diff_person = 6
log1 = read_xes("/Users/fares/github/A-customizable-interface-for-LTL-Checking/app/backend/CRUD/Hospital_log.xes")
log2 = read_xes("/Users/fares/github/A-customizable-interface-for-LTL-Checking/app/backend/CRUD/running-example.xes")

#log_filtered = ltl.ltl_checker.A_eventually_B(log, "examine casually", "pay compensation")
#print(log_filtered)

def choose_filter(file, filter_type: LTL_Rule, A, B, C, D):
#1st rule : A eventually B
    if filter_type == LTL_Rule.A_ev_B:
        filtered_log = ltl.ltl_checker.A_eventually_B(file, A, B)
#2nd rule : A eventually B evenetually C 
    elif filter_type == LTL_Rule.A_ev_B_ev_C:
        filtered_log = ltl.ltl_checker.A_eventually_B_eventually_C(file, A, B, C)
#3rd rule : A eveventually B eventually C eventually D
    elif filter_type == LTL_Rule.A_ev_B_ev_C_ev_D:
        filtered_log = ltl.ltl_checker.A_eventually_B_eventually_C_eventually_D(file,A,B,C,D)
#4th rule : A next to B next to C 
    elif filter_type == LTL_Rule.A_nex_B_nex_C:
        filtered_log = ltl.ltl_checker.A_next_B_next_C(file,A,B,C)
#5th rule : four eyes principle
    elif filter_type == LTL_Rule.four_eye:
        filtered_log = ltl.ltl_checker.four_eyes_principle(file,A,B) 
#6th rule : value different persons
    elif filter_type == LTL_Rule.val_diff_person:
        filtered_log = ltl.ltl_checker.attr_value_different_persons(file,A)
    return filtered_log 
log_test = choose_filter(log1, LTL_Rule.four_eye ,"Nursing ward","General Lab Clinical Chemistry",None, None)

print(log1)
print('$$$$$$$$$$$$$$$$$$$$$$$$')
print(log_test)

