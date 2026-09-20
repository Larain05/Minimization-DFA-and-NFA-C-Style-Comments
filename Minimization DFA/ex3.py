# ============================================
# DFA MINIMIZATION - EXAMPLE 3
# Language: Strings containing "101"
# ============================================

# Original DFA:
#
#        0    1
# A      A    C
# B      A    C
# C      E    C
# D      E    C
# E      A    G
# F      A    G
# G      G    G
#
# Start state: A
# Accepting state: G
#
# Minimization:
#
# {A,B}
# {C,D}
# {E,F}
# {G}



def dfa_example_1(input_string):

    state = "{A,B}"

    transitions = {
        "{A,B}": {
            "0": "{A,B}",
            "1": "{C,D}"
        },

        "{C,D}": {
            "0": "{E,F}",
            "1": "{C,D}"
        },

        "{E,F}": {
            "0": "{A,B}",
            "1": "{G}"
        },

        "{G}": {
            "0": "{G}",
            "1": "{G}"
        }
    }

    for symbol in input_string:

        if symbol not in ["0", "1"]:
            return False

        state = transitions[state][symbol]

    return state == "{G}"


accepted_inputs = [
    "101",
    "0101"
]

rejected_inputs = [
    "100",
    "111"
]


print("====================================")
print("DFA MINIMIZATION - EXAMPLE 3")
print("Language: Contains 101")
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