from .models import CFUser, CFSubmission, CFProblemAndTag, CFProblem
from django.utils import timezone
from django.contrib.auth.models import User as AUser
from django.http import JsonResponse


def get_problems_by_user_and_tags(cf_user, tags : list[str]) -> list[CFProblem]:
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
            CFSubmission.objects.filter(problem=problem, user=user).update(verdict=True)
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
        return JsonResponse({'user_problems_list': user_problems_list})

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
        return JsonResponse({'unsolved_problems_list': unsolved_problems_list})
    except Exception as e:
        print(e)
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
        return JsonResponse({'unsolved_problems_list': unsolved_problems_list})
    except Exception as e:
        print(e)
        return None

def get_tags_to_a_problem(name: str):
    # TODO
    try:
        problem = CFProblem.objects.get(name=name)
        tags = CFProblemAndTag.objects.filter(problem=problem).all()
        tags_list = list(tags.values_list('tag', flat=True))
        return JsonResponse({'tags_list': tags_list})
    except Exception as e:
        print(e)
        return None