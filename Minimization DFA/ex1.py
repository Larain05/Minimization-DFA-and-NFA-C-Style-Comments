# ============================================
# DFA MINIMIZATION - EXAMPLE 1
# ============================================

# ORIGINAL DFA
#
#        0    1
# A      B    C
# B      B    D
# C      B    C
# D      B    E
# E      B    C
#
# Start state: A
# Accepting state: E
#
# MINIMIZED STATES:
# {A,C}, {B}, {D}, {E}


def dfa_example_2(input_string):

    state = "{A,C}"

    transitions = {

        "{A,C}": {
            "0": "{B}",
            "1": "{A,C}"
        },

        "{B}": {
            "0": "{B}",
            "1": "{D}"
        },

        "{D}": {
            "0": "{B}",
            "1": "{E}"
        },

        "{E}": {
            "0": "{B}",
            "1": "{A,C}"
        }
    }

    for symbol in input_string:

        if symbol not in ["0", "1"]:
            return False

        state = transitions[state][symbol]
    return state == "{E}"


accepted_inputs = [
    "011",
    "0011"
]

rejected_inputs = [
    "1",
    "01"
]

print("====================================")
print("DFA MINIMIZATION - EXAMPLE 1")
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