# ============================================
# DFA MINIMIZATION - EXAMPLE 2
# ============================================

# ORIGINAL DFA
#
#        0    1
# A      B    C
# B      A    D
# C      E    F
# D      E    F
# E      E    F
# F      F    F
#
# Start state: A
# Accepting states: C, D, E
#
# MINIMIZED STATES:
# {A,B}, {C,D,E}, {F}
# ============================================


def dfa_example_1(input_string):

    state = "{A,B}"

    transitions = {

        "{A,B}": {
            "0": "{A,B}",
            "1": "{C,D,E}"
        },

        "{C,D,E}": {
            "0": "{C,D,E}",
            "1": "{F}"
        },

        "{F}": {
            "0": "{F}",
            "1": "{F}"
        }
    }

    for symbol in input_string:

        if symbol not in ["0", "1"]:
            return False

        state = transitions[state][symbol]

    return state == "{C,D,E}"


accepted_inputs = [
    "1",
    "01"
]

rejected_inputs = [
    "0",
    "11"
]

print("====================================")
print("DFA MINIMIZATION - EXAMPLE 2")
print("====================================")

print("\nACCEPTED INPUTS:")

for test in accepted_inputs:

    result = dfa_example_1(test)

    print(
        test,
        "->",
        "Accepted" if result else "Rejected"
    )


print("\nREJECTED INPUTS:")

for test in rejected_inputs:

    result = dfa_example_1(test)

    print(
        test,
        "->",
        "Accepted" if result else "Rejected"
    )