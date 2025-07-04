from django.contrib import admin
from .models import Project, Vote

class VoteInline(admin.TabularInline):
    model = Vote
    extra = 0

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'average_score']
    inlines = [VoteInline]

admin.site.register(Vote)
