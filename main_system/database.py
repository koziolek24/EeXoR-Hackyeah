from .models import CFUser, CFSubmission, CFProblemAndTag, CFProblem


def get_problems_by_user_and_tags(cf_user, tags):
    user_submissions = CFSubmission.objects.all().filter(user=cf_user)
    matching_problems = []
    for submission in user_submissions:
        problem = submission.problem
        problem_tag_records = CFProblemAndTag.objects.all().filter(problem=problem)
        problem_tags = problem_tag_records.values_list('tag', flat=True)
        common_tags = list(set(tags).intersection(problem_tags))
        if (len(common_tags) > 0):
            matching_problems.append(problem)
    return matching_problems

def add_cf_user(handle: str, rank: str, rating: int):
    try:
        new_user = CFUser.objects.create(handle=handle, rank=rank, rating=rating)
        return new_user
    except Exception as e:
        print(e)
        return None

def add_problem_tag(problem: CFUser, tag: str):
    try:
        new_problem_tag = CFProblemAndTag.objects.create(problem=problem, tag=tag)
        return new_problem_tag
    except Exception as e:
        print(e)
        return None

def add_problem(problemset_name: str, index: str, name: str, points: int, rating: int, tags: list):
    try:
        if not CFProblem.objects.filter(name=name).exists():
            new_problem = CFProblem.objects.create(problemset_name=problemset_name, index=index, name=name, points=points, rating=rating)
            for tag in tags:
                add_problem_tag(new_problem, tag)
            return new_problem
    except Exception as e:
        print(e)
        return None
