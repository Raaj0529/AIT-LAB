def cf_combine(cf1, cf2):
    if cf1 >= 0 and cf2 >= 0:
        return cf1 + cf2 * (1 - cf1)
    if cf1 < 0 and cf2 < 0:
        return cf1 + cf2 * (1 + cf1)
    return (cf1 + cf2) / (1 - min(abs(cf1), abs(cf2)))

def cf_rule(cf_evidence, cf_rule_strength):
    return cf_evidence * cf_rule_strength

n = int(input("Enter number of evidences: "))

final_cf = 0

for i in range(n):
    e = float(input(f"Evidence {i+1} CF (-1 to 1): "))
    r = float(input(f"Rule Strength {i+1} CF (-1 to 1): "))
    this_cf = cf_rule(e, r)
    final_cf = cf_combine(final_cf, this_cf)

print("Final Certainty Factor:", round(final_cf, 4))
