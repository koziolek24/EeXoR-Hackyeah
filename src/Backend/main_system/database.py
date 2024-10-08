from .models import CFUser, CFSubmission, CFProblemAndTag, CFProblem, CFTag
from django.utils import timezone
from django.contrib.auth.models import User as AUser
from django.http import JsonResponse
from datetime import timedelta


# def get_problems_by_user_and_tags(cf_user, tags : list[str]) -> list[CFProblem]:
#     user_submissions = CFSubmission.objects.all().filter(user=cf_user)
#     matching_problems = []
#     for submission in user_submissions:
#         problem = submission.problem
#         problem_tag_records = CFProblemAndTag.objects.all().filter(problem=problem)
#         problem_tags = problem_tag_records.values_list('tag', flat=True)
#         common_tags = list(set(tags).intersection(problem_tags))
#         if (len(common_tags) > 0):
#             matching_problems.append(problem)
#     return matching_problems

def add_cf_user(handle: str, rank: str, rating: int):
    try:
        new_user = CFUser.objects.create(handle=handle, rank=rank, rating=rating)
        new_user.save()

        # tworzenie użytkownika autentykacji
        auser = AUser.objects.create_user(handle, handle, handle)
        auser.save()

        return new_user
    except Exception as e:
        print(e)
        return None

def add_problem_tag(problem: CFUser, tag: str):
    try:
        new_problem_tag = CFProblemAndTag.objects.create(problem=problem, tag=tag)
        new_problem_tag.save()
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
            new_problem.save()
            return new_problem
    except Exception as e:
        print(e)
        return None

def add_tags(tag: str):
    try:
        new_tag = CFTag.objects.create(tag=tag)
        new_tag.save()
        return new_tag
    except Exception as e:
        print(e)
        return None

def add_submission(name: str, handle: str):
    try:
        problem = CFProblem.objects.get(name=name)
        user = CFUser.objects.get(handle=handle)
        if not CFSubmission.objects.filter(user=user, problem=problem).exists():
            submit_time = timezone.now()
            new_submission = CFSubmission.objects.create(problem=problem,user=user, submit_time=submit_time)
            new_submission.save()
            return new_submission
        else:
            accept_time = timezone.now()
            CFSubmission.objects.filter(problem=problem, user=user).update(verdict=True, accept_time=accept_time)
    except Exception as e:
        print(e)
        return None


def user_exists(handle):
    try:
        return CFUser.objects.all().get(handle=handle) is not None
    except CFUser.DoesNotExist:
        return False

def get_problem_by_user(handle: str):
    try:
        user = CFUser.objects.get(handle=handle)
        user_problems = CFProblem.objects.filter(cfsubmission__user=user, cfsubmission__verdict=True)
        user_problems_list = list(user_problems.values('name', 'rating', 'points', 'index'))
        return user_problems_list

    # TODO
    except Exception as e:
        print(e)
        return None

def get_problem_with_rating_and_tag(min_rating: int, max_rating, tag: str):
    # TODO
    try:
        user_problems = CFProblem.objects.filter(rating__range=(min_rating, max_rating), cfproblemandtag__tag=tag).all()
        user_problems_list = list(user_problems.values('name', 'rating', 'points', 'index'))
        return JsonResponse({'user_problems_list': user_problems_list})
    except Exception as e:
        print(e)
        return None

def get_problem_by_tag(handle: str, tag: str):
    # TODO
    # every task with tag not started by user
    try:
        problems_w_tag = CFProblem.objects.filter(cfproblemandtag__tag=tag)
        user = CFUser.objects.get(handle=handle)
        solved_problems = CFSubmission.objects.filter(user=user, verdict=True).values_list('problem', flat=True)
        unsolved_problems = problems_w_tag.exclude(id__in=solved_problems)
        unsolved_problems_list = list(unsolved_problems.values('name', 'rating', 'points', 'index'))
        return unsolved_problems_list
    except Exception as e:
        return None

def get_problem_by_rating(handle: str, min_rating: int, max_rating: int):
    # TODO
    # every task between rating not started
    try:
        problems_w_rating = CFProblem.objects.filter(rating__range=(min_rating, max_rating))
        user = CFUser.objects.get(handle=handle)
        solved_problems = CFSubmission.objects.filter(user=user, verdict=True).values_list('problem', flat=True)
        unsolved_problems = problems_w_rating.exclude(id__in=solved_problems)
        unsolved_problems_list = list(unsolved_problems.values('name', 'rating', 'points', 'index'))
        return unsolved_problems_list
    except Exception as e:
        return None

def get_tags_to_a_problem(name: str):
    # TODO
    try:
        problem = CFProblem.objects.get(name=name)
        tags = CFProblemAndTag.objects.filter(problem=problem).all()
        tags_list = list(tags.values_list('tag', flat=True))
        return tags_list
    except Exception as e:
        print(e)
        return None

def handle_from_user_id(id : int):
    return CFUser.objects.all().get(id=id).handle

def get_user_rating(handle: str):
    try:
        rating = CFUser.objects.get(handle=handle).rating
        return rating
    except Exception as e:
        print(handle)
        print("alle")
        print(e)
        return None

def get_user_data(handle: str):
    try:
        user_data = {
            'handle': None,
            'rank': None,
            'rating': None,
            'solved': None,
            'started': None,
            'Time': None
        }
        user = CFUser.objects.get(handle=handle)
        user_data['handle'] = user.handle
        user_data['rank'] = user.rank
        user_data['rating'] = user.rating
        user_data['solved'] = len(CFSubmission.objects.filter(user=user, verdict=True).values_list('problem', flat=True))
        user_data['started'] = len(CFSubmission.objects.filter(user=user).values_list('problem', flat=True))
        return user_data
    except Exception as e:
        print(e)
        return None
    # TODO pierdolnac tu cos

def get_user_problem_list(handle: str):
    try:
        user = CFUser.objects.get(handle=handle)
        problem_list_solved = CFProblem.objects.filter(cfsubmission__user=user, cfsubmission__verdict=True)
        problem_list_started = CFProblem.objects.filter(cfsubmission__user=user)
        return problem_list_started, problem_list_solved
    except Exception as e:
        print(e)
        return None

def get_user_problem_list_by_tag(handle: str, tag: str):
    try:
        user = CFUser.objects.get(handle=handle)
        problem_list_solved = CFProblem.objects.filter(cfsubmission__user=user, cfsubmission__verdict=True)
        problem_list_started = CFProblem.objects.filter(cfsubmission__user=user)
        return problem_list_started, problem_list_solved
    except Exception as e:
        print(e)
        return None


def get_time_per_tag(handle: str, tag: str):
    try:
        user = CFUser.objects.get(handle=handle)
        submit_list = list(CFSubmission.objects.filter(user=user, verdict=True, problem__cfproblemandtag__tag=tag).values_list('submit_time', 'accept_time'))
        return submit_list
    except Exception as e:
        print(e)
        return None
    
def get_time_problem(handle: str, name: str):
    try:
        user = CFUser.objects.get(handle=handle)
        problem = CFProblem.objects.get(name=name)
        time_submit = list(CFSubmission.objects.filter(user=user, problem=problem).values("submit_time"))
        time_accept = list(CFSubmission.objects.filter(user=user, problem=problem).values("accept_time"))
        return (time_submit, time_accept)
    except Exception as e:
        print(e)
        return None