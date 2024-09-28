from django.contrib import admin
from .models import *


@admin.register(CFUser)
class CFUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'handle', 'rank', 'rating']
    search_fields = ['id', 'handle']
    list_filter = ['rank']

@admin.register(CFProblem)
class CFProblemAdmin(admin.ModelAdmin):
    list_display = ['id', 'problemset_name', 'index', 'name',
                  'points', 'rating']
    search_fields = []
    list_filter = []

@admin.register(CFProblemAndTag)
class CFProblemAndTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'problem', 'tag']
    search_fields = []
    list_filter = []

@admin.register(CFSubmission)
class CFSubmissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'problem',
                  'user', 'verdict']
    search_fields = []
    list_filter = []
