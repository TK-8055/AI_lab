import collections
import collections.abc

# Fix for kanren compatibility
collections.Iterator = collections.abc.Iterator
collections.Hashable = collections.abc.Hashable

from kanren import Relation, facts, run, var, conde

# ---------------------- KNOWLEDGE BASE ----------------------

doctor = Relation()
treats = Relation()

# Facts — doctors in hospital
facts(doctor,
    ("dr_smith",),
    ("dr_jones",),
    ("dr_lee",),
    ("dr_williams",),
    ("dr_davis",)
)

# Facts — diseases treated by each doctor
facts(treats,
    ("dr_smith", "flu"),
    ("dr_smith", "allergy"),
    ("dr_jones", "cold"),
    ("dr_lee", "covid"),
    ("dr_lee", "pneumonia"),
    ("dr_williams", "diabetes"),
    ("dr_davis", "hypertension")
)

# Rule: A doctor is skilled if they treat at least one disease
def is_skilled(person):
    return conde((doctor(person), treats(person, var())),)


# ---------------------- USER QUERY HANDLING ----------------------

query = input("Enter query (e.g., Who is skilled? / Is dr_lee skilled?): ").strip().lower()
x = var()

# WHO query
if query.startswith("who"):
    result = run(0, x, is_skilled(x))
    if result:
        print("\n✓ Skilled doctors found:")
        for name in result:
            print(f"- {name.replace('_', ' ').title()}")
    else:
        print("\nX No skilled doctors found.")

# IS query
elif query.startswith("is"):
    words = query.replace("?", "").split()
    if len(words) >= 2:
        name = words[1]
        skilled_list = run(0, x, is_skilled(x))
        if name in skilled_list:
            print(f"\n✓ Yes, {name.replace('_', ' ').title()} is skilled.")
        else:
            print(f"\nX No, {name.replace('_', ' ').title()} is not skilled.")
    else:
        print("\nX Invalid query format.")

else:
    print("\nX Invalid query type.")
