# ============================================
# DFA MINIMIZATION - NEW EXAMPLE 2
# Language: Strings ending in "01"
# ============================================

# Original DFA:
#
#        0    1
# A      B    D
# B      E    C
# C      E    F
# D      B    D
# E      E    C
# F      E    D
#
# Start state: A
# Accepting states: C, F
#
# Final equivalence classes:
#
# {A,D}
# {B,E}
# {C,F}


def dfa_example_2(input_string):

    state = "{A,D}"\
        
    transitions = {

        "{A,D}": {
            "0": "{B,E}",
            "1": "{A,D}"
        },

        "{B,E}": {
            "0": "{B,E}",
            "1": "{C,F}"
        },

        "{C,F}": {
            "0": "{B,E}",
            "1": "{A,D}"
        }
    }
    for symbol in input_string:

        if symbol not in ["0", "1"]:
            return False

        state = transitions[state][symbol]
    return state == "{C,F}"


accepted_inputs = [
    "01",
    "101"
]

rejected_inputs = [
    "10",
    "011"
]

print("====================================")
print("DFA MINIMIZATION - EXAMPLE 4")
print("Language: Strings ending in 01")
print("====================================")

print("\nACCEPTED INPUTS:")

for test in accepted_inputs:

    result = dfa_example_2(test)

    print(
        test,
        "->",
        "Accepted" if result else "Rejected"
    )


print("\nREJECTED INPUTS:")

for test in rejected_inputs:

    result = dfa_example_2(test)

    print(
        test,
        "->",
        "Accepted" if result else "Rejected"
    )