from random import randint

class Problem:
    def __init__(self, _name: str, _link: str, _rating: int, _problem_id: str,
                 _is_solved = False, _time_begin = 0, _time_end = 0,
                 _tags = None):
        self.name = _name
        self.link = _link
        self.rating = _rating
        self.is_solved = _is_solved
        self.time_begin = _time_begin
        self.time_end = _time_end
        self.problem_id = _problem_id
        self.tags = _tags
        if self.tags == None:
            self.tags = []

    def get_name(self) -> str:
        return self.name

    def get_link(self) -> str:
        return self.link

    def get_rating(self) -> int:
        return self.rating
    
    def get_link(self) -> str:
        return self.link

    def get_time(self) -> int:
        return self.time
    
    def get_tags(self) -> list[str]:
        return self.tags
    
    def get_problem_id(self) -> str:
        return self.problem_id
    
    def stringify(self) -> str:
        output_string = ""
        output_string += str(self.get_name()) + " "
        output_string += str(self.get_problem_id()) + " "
        output_string += str(self.get_rating()) + " "
        output_string += str(self.get_tags()) + " "
        return output_string

def calculate_performence(problem: list[Problem]) -> int:
    performence = problem.getRating() * 10
    performence //= problem.getTime()
    return performence

# there for sure are more than 0 problems
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


def get_random_problem_with_tag(problems: list[Problem], tag: str) -> Problem:
    filtered_problems = filter_problems_by_tag(problems, tag)

    ammount_of_problems = len(filtered_problems)

    if ammount_of_problems == 0:
        return None
    
    random_number = randint(0, ammount_of_problems-1)
    return filtered_problems[random_number]