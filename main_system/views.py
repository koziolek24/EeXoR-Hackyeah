from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import *
from .serializers import *

# Other views functions

def test_view(request):
    return HttpResponse("test")

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


class CFProblemAndTagViewSet(viewsets.ModelViewSet):
    queryset = CFProblemAndTag.objects.all()
    serializer_class = CFProblemAndTagSerializer


class CFSubmissionViewSet(viewsets.ModelViewSet):
    queryset = CFSubmission.objects.all()
    serializer_class = CFSubmissionSerializer