import os
from collections import Counter

def get_score(template, rules, steps):
    for j in range(steps):  
        length = len(template)
        new_template = ""
        for i in range(length):
            if i+1 != length and template[i] + template[i+1] in rules:
                new_template += template[i] + rules[template[i] + template[i+1]]
            else:
                new_template += template[i]
        template = new_template
        print("step:", j)
    template = Counter(template)
    return template[max(template, key=lambda x: template[x])] - template[min(template, key=lambda x: template[x])]



if __name__ == "__main__":
    rules = {}
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        template = f.readline().strip()
        f.readline()
        for line in f:
            rule = line.strip().split(" -> ")
            rules[rule[0]] = rule[1]
    
    print(get_score(template, rules, 40))

