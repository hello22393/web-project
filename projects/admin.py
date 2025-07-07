from django.contrib import admin
from .models import Project, Vote

class VoteInline(admin.TabularInline):
    model = Vote
    extra = 0

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'formatted_average_score']
    inlines = [VoteInline]

    def formatted_average_score(self, obj):
        # average_score가 메서드일 경우 호출
        score = obj.average_score() if callable(obj.average_score) else obj.average_score
        if score is not None:
            return f"{score:.2f}"
        return "N/A"
    formatted_average_score.short_description = '평균 점수'

admin.site.register(Vote)
