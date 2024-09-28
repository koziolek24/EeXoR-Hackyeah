import Problem

hardcoded_problems = [
    Problem.Problem({"name": "a",
                     "link": "...",
                     "rating": 1900,
                     "is_solved": True,
                     "time": 100,
                     "problem_id": "9309a",
                     "tags": [1,2]}),
    Problem.Problem({"name": "b",
                     "link": "...",
                     "rating": 1900,
                     "is_solved": True,
                     "time": 5000,
                     "problem_id": "9309a",
                     "tags": [2,3]}),
    Problem.Problem({"name": "c",
                     "link": "...",
                     "rating": 1900,
                     "is_solved": True,
                     "time": 5000,
                     "problem_id": "9309a",
                     "tags": [2,3]}),
    Problem.Problem({"name": "d",
                     "link": "...",
                     "rating": 1900,
                     "is_solved": True,
                     "time": 100,
                     "problem_id": "9309a",
                     "tags": [6,7]}),
    Problem.Problem({"name": "e",
                     "link": "...",
                     "rating": 1900,
                     "is_solved": True,
                     "time": 100,
                     "problem_id": "9309a",
                     "tags": [3,5]}),
    Problem.Problem({"name": "f",
                     "link": "...",
                     "rating": 1900,
                     "is_solved": True,
                     "time": 100,
                     "problem_id": "9309a",
                     "tags": [1,2]}),
]

print(hardcoded_problems[0].convert_to_json())
print(Problem.get_random_problem_with_tag(hardcoded_problems, 1).stringify())
print([x.stringify() for x in Problem.filter_problems_by_rating(hardcoded_problems, 1400, 1700)])
print([x.stringify() for x in hardcoded_problems])
hardcoded_problems = Problem.sort_problems_by_tags(hardcoded_problems)
