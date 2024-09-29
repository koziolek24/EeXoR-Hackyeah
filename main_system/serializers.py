from .models import *
from rest_framework import serializers


class CFUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CFUser
        fields = ['id', 'handle', 'rank', 'rating']


class CFContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CFContest
        fields = ['id', 'contest_id', 'duration', 'difficulty']


class CFRatingChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CFRatingChange
        fields = ['id', 'contest', 'user', 'rank', 'old_rating', 
                  'new_rating']


class CFUserAndContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CFUserAndContest
        fields = ['id', 'user', 'contest', 'participant_type']


class CFProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CFProblem
        fields = ['id', 'problemset_name', 'index', 'name',
                  'points', 'rating']


class CFProblemAndTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CFProblemAndTag
        fields = ['id', 'problem', 'tag']


class CFSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CFSubmission
        fields = ['id', 'cf_id', 'creation_time', 'problem',
                  'user', 'verdict']

class CFTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CFTag
        fields = ['id', 'tag']


