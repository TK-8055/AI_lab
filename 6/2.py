import collections
import collections.abc

# Fix for kanren new Python versions
collections.Iterator = collections.abc.Iterator
collections.Hashable = collections.abc.Hashable

from kanren import Relation, facts, run, var

# Knowledge Base
doctor = Relation()
treats = Relation()

facts(doctor,
    ("dr_smith",),
    ("dr_jones",),
    ("dr_lee",),
    ("dr_williams",),
    ("dr_davis",)
)

facts(treats,
    ("dr_smith", "flu"),
    ("dr_smith", "allergy"),
    ("dr_jones", "cold"),
    ("dr_lee", "covid"),
    ("dr_lee", "pneumonia"),
    ("dr_williams", "diabetes"),
    ("dr_davis", "hypertension")
)

# Query to find all doctors treating a given disease
disease = input("Enter a disease: ").strip().lower()
x = var()
result = run(0, x, treats(x, disease))

if result:
    print("\nDoctors who treat", disease, ":")
    for name in result:
        print("-", name.replace("_", " ").title())
else:
    print("\nNo doctor found for this disease.")
