import pandas as pd
import pm4py.algo.filtering.log.ltl as ltl
from enum import Enum
from pm4py import convert_to_dataframe, read_xes

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
def OR(files):
    dataframes = [convert_to_dataframe(files[0]),convert_to_dataframe(files[1])]
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

def AND(files):
    dataframes = [convert_to_dataframe(files[0]),convert_to_dataframe(files[1])]
    if len(dataframes[0]) == 0 or len(dataframes[1]) == 0:
        return pd.DataFrame()
    else:
        return pd.merge(dataframes[0],dataframes[1], how='inner').drop_duplicates()



def apply_rule(file, parsed_LTL_Rule, events):
    st = []
    for i in parsed_LTL_Rule:
        if i.startswith('LTL_Rule_') :
            st.append(apply_filter(file,choose_filter(i),events[i]))
           
        elif i == 'LTL_And':
            op1 = st.pop()
            op2 = st.pop()
            st.append(AND([op1,op2]))
        elif i == 'LTL_Or': 
            op1 = st.pop()
            op2 = st.pop()
            st.append(OR([op1,op2]))   
    return st.pop()

# file = read_xes("tests/data/running-example.xes")
# parsed_LTL_Rule = parse_mod_ltl("LTL_LB LTL_A_ev_B LTL_Or LTL_A_ev_B_ev_C LTL_And LTL_A_ev_B_ev_C_ev_D LTL_RB")
# events = [
#             ["register request", "check ticket"], 
#             ["decide", "pay compensation", "examine casually"], 
#             ["decide", "pay compensation", "examine casually", "reject request"]
#          ]

# print(apply_rule(file, parsed_LTL_Rule, events))


class Conversion:
 
    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
        # Precedence setting
        self.output = []
        self.precedence = {'LTL_And': 1, 'LTL_Or': 1}
 
    # check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False
 
    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]
 
    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
 
    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)
 
    # A utility function to check is the given character
    # is operand
    def isOperand(self, ch):
        return ch.isalpha()
 
    # Check if the precedence of operator is strictly
    # less than top of stack or not
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False
 
    # The main function that
    # converts given infix expression
    # to postfix expression
    def infixToPostfix(self, exp):
        res = exp.split()
        # Iterate over the expression for conversion
        for i in res:
            # If the character is an operand,
            # add it to output
            if self.isOperand(i):
                self.output.append(i+' ')
 
            # If the character is an '(', push it to stack
            elif i == 'LTL_LB':
                self.push(i)
 
            # If the scanned character is an ')', pop and
            # output from the stack until and '(' is found
            elif i == 'LTL_RB':
                while((not self.isEmpty()) and
                      self.peek() != 'LTL_LB'):
                    a = self.pop()
                    self.output.append(a+' ')
                if (not self.isEmpty() and self.peek() != 'LTL_LB'):
                    return -1
                else:
                    self.pop()
 
            # An operator is encountered
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop()+' ')
                self.push(i)
 
        # pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop()+' ')
 
        return ("".join(self.output).strip())

 
# Driver's code
if __name__ == '__main__':
    exp = 'LTL_Rule_A_ev_B_ev_C_0 LTL_Or LTL_LB LTL_Rule_A_ev_B_0 LTL_And LTL_Rule_Attr_Val_Diff_Persons_0 LTL_RB LTL_Or LTL_Rule_A_ev_B_1'
    events = {
         'LTL_Rule_A_ev_B_ev_C_0' :["decide", "pay compensation", "examine casually"], 
         'LTL_Rule_A_ev_B_0' : ["register request", "check ticket"],
         'LTL_Rule_Attr_Val_Diff_Persons_0' : ["register request"],
         'LTL_Rule_A_ev_B_1' : ["decide", "pay compensation"]
         }
    obj = Conversion(len(exp))
 #LTL_OrLTL_LBcLTL_OrdLTL_OreLTL_RB
    # Function call
    file = read_xes('tests/data/running-example.xes')
    var= obj.infixToPostfix(exp)
    log =apply_rule(file,var,events)
    print(convert_to_dataframe(log))
