relationships = {
    "batsman":"cricketer",
    "Sachin":"batsman"
    }
def derive_predicate(subject):
    if subject in relationships:
        predicate = relationships[subject]
        return f"{subject} is {predicate}"
    else:
        return f"No information available for {subject}"
subject_to_derive="Sachin"
result = derive_predicate(subject_to_derive)
print(result)