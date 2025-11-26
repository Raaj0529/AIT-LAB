import itertools

def truth_table_entails(kb, query):
    symbols = list({s for clause in kb for s in clause})
    if query not in symbols:
        symbols.append(query)

    for values in itertools.product([False, True], repeat=len(symbols)):
        model = dict(zip(symbols, values))

        if all(model[s] for s in kb if isinstance(s, str)):
            pass

        kb_true = all(eval_clause(clause, model) for clause in kb)
        if kb_true and not model[query]:
            return False
    return True

def eval_clause(clause, model):
    if len(clause) == 1:
        return model[clause[0]]
    if clause[0] == "not":
        return not model[clause[1]]

kb = [
    "P",
    ("not","Q"),
]

query = "P"
print("Truth Table:", truth_table_entails(kb, query))

def resolution(kb, query):
    clauses = kb + [[f"not_{query}"]]

    while True:
        new = []
        for i in range(len(clauses)):
            for j in range(i+1, len(clauses)):
                resolvents = resolve(clauses[i], clauses[j])
                if [] in resolvents:
                    return True
                for r in resolvents:
                    if r not in new:
                        new.append(r)

        if all(r in clauses for r in new):
            return False

        for r in new:
            if r not in clauses:
                clauses.append(r)

def resolve(c1, c2):
    res = []
    for x in c1:
        for y in c2:
            if x == "not_"+y or y == "not_"+x:
                new_clause = list(set(c1 + c2))
                new_clause.remove(x)
                new_clause.remove(y)
                res.append(new_clause)
    return res

kb_r = [
    ["P","Q"],
    ["not_Q","R"],
    ["not_P"]
]

query_r = "R"
print("Resolution:", resolution(kb_r, query_r))

