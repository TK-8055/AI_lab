def implies(p, q):
    return (not p) or q

def iff(p, q):
    return (p and q) or (not p and not q)

def get_user_propositions():
    props = {}
    variables = ['A', 'B', 'C']
    print("Enter truth values for propositions (True/False):")
    for var in variables:
        while True:
            val = input(f"Value of {var}: ").strip().lower()
            if val in ['true', 't', '1']:
                props[var] = True
                break
            elif val in ['false', 'f', '0']:
                props[var] = False
                break
            else:
                print("Please enter True or False.")
    return props

def evaluate_expressions(props):
    A = props["A"]; B = props["B"]; C = props["C"]
    print("\n--- Propositional Logic Evaluation ---")
    print("1) A ∧ ¬C      =", A and not C)
    print("2) (A ∨ B) ∧ C =", (A or B) and C)
    print("3) ¬B ∨ A      =", (not B) or A)
    print("4) A → C       =", implies(A, C))
    print("5) B ↔ C       =", iff(B, C))

propositions = get_user_propositions()
evaluate_expressions(propositions)
