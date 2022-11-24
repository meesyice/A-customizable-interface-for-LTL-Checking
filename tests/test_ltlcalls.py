import sys
from pm4py import read_xes

sys.path.append('.')

from app.backend.ltlcalls import apply_filter, LTL_Rule

def test_choose_filter():
    file = read_xes('tests/data/running-example.xes')
    for rule in LTL_Rule:
        print('testing rule: ', rule)
        assert apply_filter(file, rule, ['decide', 'check ticket', 'pay compensation', 'examine casually']) is not None
