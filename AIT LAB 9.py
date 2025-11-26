def diagnose(symptoms):
    rules = [
        ({"fever", "cough", "cold"}, "You may have FLU"),
        ({"fever", "headache", "nausea"}, "You may have DENGUE"),
        ({"stomach pain", "vomiting", "diarrhea"}, "You may have FOOD POISONING"),
        ({"fatigue", "weight loss", "thirst"}, "You may have DIABETES"),
        ({"chest pain", "shortness of breath"}, "You may have HEART PROBLEM")
    ]

    for cond, result in rules:
        if cond.issubset(symptoms):
            return result
    return "No diagnosis found. Consult a doctor."

print("Medical Diagnosis Expert System")
print("Enter symptoms separated by commas.")
user_input = input("Symptoms: ").lower().split(",")

symptoms = {s.strip() for s in user_input}
print("\nDiagnosis:", diagnose(symptoms))
