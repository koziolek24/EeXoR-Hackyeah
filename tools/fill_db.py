import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EeXoR.settings')
django.setup()
from main_system.database import add_problem
import requests

tags = [
    "implementation",
    "math",
    "greedy",
    "dp",
    "data structures",
    "brute force",
    "constructive algorithms",
    "graphs",
    "sortings",
    "binary search",
    "dfs and similar",
    "trees",
    "strings",
    "number theory",
    "combinatorics",
    "geometry",
    "bitmasks",
    "two pointers",
    "dsu",
    "shortest paths",
    "probabilities",
    "divide and conquer",
    "hashing",
    "games",
    "flows",
    "interactive",
    "matrices",
    "string suffix structures",
    "fft",
    "graph matchings",
    "ternary search",
    "expression parsing",
    "meet-in-the-middle",
    "2-sat",
    "chinese remainder theorem",
    "schedules"
]

def add_task_db(tag):
    url = f'https://codeforces.com/api/problemset.problems?tags={tag}'
    response = requests.get(url)
    try:
        response = response.json()
        problems = response['result']['problems']
        for i in range(min(len(problems), 100)):
            problem = problems[i]
            Id = problem.get('contestId')
            index = problem.get('index')
            name = problem.get('name')
            points = problem.get('points')
            rating = problem.get('rating')
            tags = problem.get('tags', [])

            add_problem(Id, index, name, points, rating, tags)
    except Exception as e:
        print(e)
        return None


for tag in tags:
    add_task_db(tag)
