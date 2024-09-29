from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .models import *
from .serializers import *
from .responses import (FrontendMessage, get_ok_response,
                        get_bad_request_error, get_internal_server_error,
                        get_custom_response, get_json_response_from)
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt
from .database import add_cf_user, get_user_problem_list_by_tag
from .database import user_exists, handle_from_user_id
from .auth import (login_user, logout_user,
                   get_csrf_token, get_drf_token, get_auser)
from rest_framework.decorators import action
from .database import add_submission
from .Problem import get_problem_with_tag, get_recommended_problem, get_random_problem

# Informacje zwrotne

USER_ALREADY_REGISTERED = 'Użytkownik o podanym handlu  już jest zarejestrowany'
PASSWORD_IS_BAD = 'Hasło jest nie prawidłowe. Hasło nie może być puste.'
ONLY_POST_WORKS = 'Nieprawidłowa metoda, tylko POST działa.'
USER_DOESNT_EXISTS = 'Użytkownik o podanym handlu nie istnieje.'
INCCORECT_PASSWORD = 'Nieprawidłowe hasło'

# Authentication system

@csrf_exempt
def request_register(request):
    try:
        if request.method == "POST":
            # pobieranie danych
            data = request.POST.copy()
            try:
                handle = data["handle"]
                rank = data["rank"]
                rating = int(data["rating"])
            except MultiValueDictKeyError:
                return get_bad_request_error('Pola POSTu handle, rank, rating są wymagane.')


            if user_exists(handle):
                print("already exists")
                return get_bad_request_error(USER_ALREADY_REGISTERED)

            # zapis danych w bazie
            result = add_cf_user(handle, rank, rating)
            if result is None:
                return get_internal_server_error("Nie udało się stworzyć użytkownika")
            else:
                return get_ok_response("Użytkownik utworzony poprawnie")
            
        else:
            return get_bad_request_error(ONLY_POST_WORKS)
    except Exception as e:
        return get_internal_server_error(e)


@csrf_exempt
def request_login(request):
    try:
        if request.user.is_authenticated:
            return get_bad_request_error("Użytkownik jest już zalogowany")

        if request.method == "POST":
            try:
                handle = request.POST["handle"]
            except MultiValueDictKeyError:
                return get_bad_request_error("handle jest wymagane.")

            if login_user(request, handle):
                auser = get_auser(handle)
                # dodawanie tokenów CSRF i DRF
                csrf_token = get_csrf_token(request)
                drf_token = get_drf_token(auser)
                msg = FrontendMessage(csrf_token=csrf_token,
                                      drf_token=drf_token.key)
                msg.add_field('user_id', CFUser.objects.all().get(handle=handle).id)
                # wysylanie odpowiedzi
                response = get_custom_response(msg, 200)
                return response
            else:
                return get_bad_request_error(USER_DOESNT_EXISTS)
        else:
            return get_bad_request_error(ONLY_POST_WORKS)
    except Exception as e:
        return get_internal_server_error(e)

# Other views functions

def test_view(request):
    return HttpResponse("test")

def is_logged_test_view(request):
    if request.user.is_authenticated:
        return HttpResponse("Jest zalogowany")
    else:
        return HttpResponse("Nie jest zalogowany")

# DRF Viewsets

class CFUserViewSet(viewsets.ModelViewSet):
    queryset = CFUser.objects.all()
    serializer_class = CFUserSerializer


class CFContestViewSet(viewsets.ModelViewSet):
    queryset = CFContest.objects.all()
    serializer_class = CFContestSerializer


class CFRatingChangeViewSet(viewsets.ModelViewSet):
    queryset = CFRatingChange.objects.all()
    serializer_class = CFRatingChangeSerializer


class CFUserAndContestViewSet(viewsets.ModelViewSet):
    queryset = CFUserAndContest.objects.all()
    serializer_class = CFUserAndContestSerializer


class CFProblemViewSet(viewsets.ModelViewSet):
    queryset = CFProblem.objects.all()
    serializer_class = CFProblemSerializer
    authentication_classes = []

    @csrf_exempt
    @action(detail=True, methods=['post'])
    def start(self, request, pk=None):
        problem = self.get_object()
        handle = handle_from_user_id(int(request.data['user_id']))
        result = add_submission(problem.name, handle)
        if result is not None:
            return get_ok_response('Ok')
        else:
            return get_internal_server_error('Operacja się nie powiodła')
    
    @csrf_exempt
    @action(detail=True, methods=['post'])
    def end(self, request, pk=None):
        problem = self.get_object()
        handle = handle_from_user_id(int(request.data['user_id']))
        result = add_submission(problem.name, handle)
        if result is None:
            return get_ok_response('Ok')
        else:
            return get_internal_server_error('Operacja się nie powiodła')
    
    @csrf_exempt
    @action(detail=False, methods=['get'])
    def started(self, request):
        handle = handle_from_user_id(int(request.data['user_id']))
        tag = request.query_params['tag']
        started, solved = get_user_problem_list_by_tag(handle, tag)
        return get_json_response_from(started, 200, iterate=True)
    
    @csrf_exempt
    @action(detail=False, methods=['get'])
    def finished(self, request):
        handle = handle_from_user_id(int(request.data['user_id']))
        tag = request.query_params['tag']
        started, solved = get_user_problem_list_by_tag(handle, tag)
        return get_json_response_from(solved, 200, iterate=True)
        


class CFProblemAndTagViewSet(viewsets.ModelViewSet):
    queryset = CFProblemAndTag.objects.all()
    serializer_class = CFProblemAndTagSerializer


class CFSubmissionViewSet(viewsets.ModelViewSet):
    queryset = CFSubmission.objects.all()
    serializer_class = CFSubmissionSerializer

class CFTagViewSet(viewsets.ModelViewSet):
    queryset = CFTag.objects.all()
    serializer_class = CFTagSerializer