import Problem

hardcoded_problems = [
    Problem.Problem("a", "...", 1900, "1901a", _tags=[1,2]),
    Problem.Problem("b", "...", 1700, "1901b", _tags=[3,4]),
    Problem.Problem("c", "...", 1500, "1901c", _tags=[1,4]),
    Problem.Problem("d", "...", 1300, "1901d", _tags=[5,2]),
    Problem.Problem("e", "...", 1400, "1901e", _tags=[4,6]),
    Problem.Problem("f", "...", 1400, "1901f", _tags=[1,6])
]

print
print(hardcoded_problems)
hardcoded_problems = Problem.sort_problems_by_tags(hardcoded_problems)
print(hardcoded_problems)
