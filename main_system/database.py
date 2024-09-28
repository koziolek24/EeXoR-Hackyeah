from .models import CFUser, CFSubmission, CFProblemAndTag, CFProblem


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

def get_all_problems_of_user(cf_user: str) -> list[CFProblem]:
    user_submissions = CFSubmission.objects.all().filter(user=cf_user)
    for submission in user_submissions:
        problem = submission.problem
        problem_tag_records = CFProblemAndTag.objects.all().filter(problem=problem)
        problems = problem_tag_records.values_list('problem', flat=True)
    return problems