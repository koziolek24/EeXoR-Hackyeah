import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EeXoR.settings')
import django
django.setup()

from random import randint
import json
from main_system.database import get_problem_by_tag, get_problem_by_rating, get_user_rating, get_problem_by_user, get_tags_to_a_problem
import tools.fill_db

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
        return get_tags_to_a_problem(self.name)
    
    def get_points(self) -> int:
        if self.points is None:
            return -1
        return self.points
    
    def get_index(self) -> str:
        return self.index
    
    def convert_to_dict(self):
        if self.name is None:
            return {}
        data = {
            'name': self.get_name(),
            'rating': self.get_rating(),
            'points': self.get_points(),
            'index': self.get_index(),
        }
        return data


def calculate_performence(problem: list[Problem]) -> int:
    performence = problem.getRating() * 20
    performence //= problem.getTime()
    return performence

def evaluate_problems(problems: list[Problem]) -> int:
    performence = 0
    ammount_of_problems = len(problems)
    if ammount_of_problems == 0:
        return 100000000

    for problem in problems:
        performence += calculate_performence(problem)
    
    performence //= ammount_of_problems
    return performence

def get_tags_from_problems(problems: list[Problem]) -> list[str]:
    print('ochuj')
    print(len(problems))
    all_tags = []
    if problems is not None:
        for problem in problems:
            print()
            print()
            print(type(problem))
            print()
            print()
            problem_tags = problem.get_tags()
            for tag in problem_tags:
                if tag in all_tags:
                    continue
                all_tags.append(tag)

    return all_tags

def sort_problems_by_difficulty(problems: list[Problem]) -> list[Problem]:
    return sorted(problems, key=lambda x : x.rating)

def sort_problems_by_tags(problems: list[Problem]) -> list[Problem]:
    print(problems)
    for problem in problems:
        print('kutasiatko')
        print(type(problem))
    all_tags = get_tags_from_problems(problems)
    print('chuju zloty')
    sorted_problems = {}

    for tag in all_tags:
        sorted_problems[tag] = []

    for problem in problems:
        problem_tags = get_tags_to_a_problem(problem.get_name())
        for tag in problem_tags:
            sorted_problems[tag].append(problem)
    
    for tag in all_tags:
        sorted_problems[tag] = sort_problems_by_difficulty(sorted_problems[tag])
    
    return sorted_problems

def get_worst_tags(problems: list[Problem]):
    sorted_tagwise = sort_problems_by_tags(problems)
    evaluated_tags = []
    for tag in sorted_tagwise:
        evaluated_tags.append([evaluate_problems([sorted_tagwise[x] for x in range(min([len(sorted_tagwise[tag])-1, 10]))]), tag])
    
    sorted(evaluated_tags, key=lambda x: x[0])

    worst_tags = []
    for i in range(min([len(evaluated_tags), 3])):
        worst_tags.append(evaluated_tags[i][1])
    
    return worst_tags
        

def filter_problems_by_tag(problems: list[Problem], tag: str) -> list[Problem]:
    filtered_problems = []

    for problem in problems:
        problem_tags = problem.get()
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

def find_random_problem(problems: list[Problem]) -> Problem:
    ammount_of_problems = len(problems)
    if ammount_of_problems == 0:
        return None
    
    random_number = randint(0, ammount_of_problems-1)
    return problems[random_number]

def get_rating_range(user_rating):
    if user_rating is None:
        user_rating = 800
    user_rating//=100
    min_rating = max([800, (user_rating - 2)*100])
    max_rating = max([1000, (user_rating + 2)*100])
    return [min_rating, max_rating]

def list_to_problems(problems_list: list[dict]) -> list[Problem]:
    if problems_list is None:
        return []
    all_problems = []
    for problem in problems_list:
        current_problem = Problem(problem['name'], problem['rating'], problem['points'], problem['index'])
        all_problems.append(current_problem)
    
    return all_problems

def get_problem_with_tag(username: str, tags: list[str]) -> dict:
    all_problems = []
    for tag in tags:
        response = get_problem_by_tag(username, tag)
        tmp = list_to_problems(response)
        for problem in tmp:
            all_problems.append(problem)
    
    rating_range = get_rating_range(get_user_rating(username))
    all_problems = filter_problems_by_rating(all_problems, rating_range[0], rating_range[1])
    final_problem = get_random_problem(username)
    if final_problem is None:
        return {}
    return final_problem

def get_recommended_problem(username: str) -> dict:
    print(username)
    response = get_problem_by_user(username)
    print(type(response))
    print(response)
    if len(response) == 0:
        return get_problem_with_tag(username, ['math'])
    print(str(response) + 'resp')
    all_problems = list_to_problems(response)
    print('kuuutas')
    print(type(all_problems))
    for problem in all_problems:
        print('kukukutas')
        print(problem)
        print(type(problem))
    tags = get_worst_tags(all_problems)
    return get_problem_with_tag(username, tags)

def get_random_problem(username: str) -> dict:
    rating_range = get_rating_range(get_user_rating(username))
    print("hello world")
    response = get_problem_by_rating(username, rating_range[0], rating_range[1])
    if response is None:
        return None
    problems = list_to_problems(response)
    random_problem = find_random_problem(problems)
    return random_problem.convert_to_dict()

def get_unused_tags(username: str) -> list[str]:
     response = get_problem_by_user(username)
     problems = list_to_problems(response)
     all_tags = tools.fill_db.tags
     for problem in problems:
         tags = get_tags_from_problems(problem.get_name())
         for tag in tags:
             if tag in all_tags:
                 all_tags.remove(tag)
     return all_tags

print(get_unused_tags('cacteyy'))
