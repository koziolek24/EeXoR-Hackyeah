import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EeXoR.settings')
import django
django.setup()

from random import randint
import json
from main_system.database import get_problem_by_tag, get_problem_by_rating, get_user_rating

class Problem:
    def __init__(self, _name, _rating, _points, _index):
        self.name = _name
        self.rating = _rating
        self.time = 100
        self.points = _points
        self.index = _index
        self.tags = []

    def get_name(self) -> str:
        return self.name

    def get_link(self) -> str:
        return self.link

    def get_rating(self) -> int:
        if self.rating is None:
            return -1
        return self.rating
    
    def get_time(self) -> int:
        return self.time
    
    def get_tags(self) -> list[str]:
        return self.tags
    
    def convert_to_dict(self):
        data = {
            "name": self.name,
            "rating": self.rating,
            "points": self.points,
            "index": self.index,
        }
        return data


def calculate_performence(problem: list[Problem]) -> int:
    performence = problem.getRating() * 20
    performence //= problem.getTime()
    return performence

# there for sure are more than 0 problems (checked earlier)
def evaluate_problems(problems: list[Problem]) -> int:
    performence = 0
    ammount_of_problems = len(problems)

    for problem in problems:
        performence += calculate_performence(problem)
    
    performence //= ammount_of_problems
    return performence

def get_tags_from_problems(problems: list[Problem]) -> list[str]:
    all_tags = []

    for problem in problems:
        problem_tags = problem.get_tags()
        for tag in problem_tags:
            if tag in all_tags:
                continue
            all_tags.append(tag)

    return all_tags

def sort_problems_by_difficulty(problems: list[Problem]) -> list[Problem]:
    return sorted(problems, key=lambda x : x.rating)

def sort_problems_by_tags(problems: list[Problem]) -> list[Problem]:
    all_tags = get_tags_from_problems(problems)
    sorted_problems = {}

    for tag in all_tags:
        sorted_problems[tag] = []

    for problem in problems:
        problem_tags = problem.get_tags()
        for tag in problem_tags:
            sorted_problems[tag].append(problem)
    
    for tag in all_tags:
        sorted_problems[tag] = sort_problems_by_difficulty(sorted_problems[tag])
    
    return sorted_problems

def get_worst_tags(problems: list[Problem]):
    sorted_tagwise = sort_problems_by_tags(problems)
    evaluated_tags = []
    for tag in sorted_tagwise:
        evaluated_tags.append([evaluate_problems([sorted_tagwise[x] for x in range(min([sorted_tagwise[tag], 10]))]), tag])
    
    sorted(evaluated_tags, key=lambda x: x[0])

    worst_tags = []
    for i in range(min([len(evaluated_tags), 3])):
        worst_tags.append(evaluated_tags[i][1])
    
    return worst_tags
        

def filter_problems_by_tag(problems: list[Problem], tag: str) -> list[Problem]:
    filtered_problems = []

    for problem in problems:
        problem_tags = problem.get_tags()
        if tag in problem_tags:
            filtered_problems.append(problem)
    
    return filtered_problems

def filter_problems_by_rating(problems: list[Problem], min_rating: int, max_rating: int) -> list[Problem]:
    filtered_problems = []

    for problem in problems:
        if problem.get_rating() < min_rating:
            continue
        if problem.get_rating() > max_rating:
            continue

        filtered_problems.append(problem)
    
    return filtered_problems

def calculate_average(values):
    average = sum(values) / len(values)
    return average

def get_random_problem(problems: list[Problem]) -> Problem:
    # filtered_problems = filter_problems_by_tag(problems, tag)
    ammount_of_problems = len(problems)
    if ammount_of_problems == 0:
        return None
    
    random_number = randint(0, ammount_of_problems-1)
    return problems[random_number]

def get_rating_range(user_rating):
    user_rating//=100
    min_rating = max([0, (user_rating - 2)*100])
    max_rating = (user_rating + 2)*100
    return [min_rating, max_rating]
    

def get_problem_with_tag(username: int, tags: list[str]) -> dict:
    all_problems = []
    for tag in tags:
        response = get_problem_by_tag(username, tag)
        for problem in response:
            current_problem = Problem(problem["name"], problem["rating"], problem["points"], problem["index"])
            all_problems.append(current_problem)
    
    rating_range = get_rating_range(get_user_rating(username))
    all_problems = filter_problems_by_rating(all_problems, rating_range[0], rating_range[1])
    final_problem = get_random_problem(all_problems)
    return final_problem.convert_to_dict()

def get_recommended_problem(username: str) -> dict:
    pass

def get_random_problem(username: str) -> dict:
    pass