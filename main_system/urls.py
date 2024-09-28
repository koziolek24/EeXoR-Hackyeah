from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cf_users', CFUserViewSet)
router.register('cf_contests', CFContestViewSet)
router.register('cf_rating_changes', CFRatingChangeViewSet)
router.register('cf_user_and_contests', CFUserAndContestViewSet)
router.register('cf_problem', CFProblemViewSet)
router.register('cf_problem_and_tags', CFProblemAndTagViewSet)
router.register('cf_submissions', CFSubmissionViewSet)



urlpatterns = [
    path('test/', test_view),
    path('register/', request_register),
    path('login/', request_login),
    path('logout/', request_logout),
]
urlpatterns += router.urls
