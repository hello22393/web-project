from django.views.generic import ListView, DetailView, View
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Avg
from .models import Project, Vote

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'

    def get_queryset(self):
        return Project.objects.annotate(avg_score=Avg('votes__score')).order_by('-avg_score')


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'


class ProjectVoteView(View):
    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        try:
            score = int(request.POST['score'])
            if score not in [1, 2, 3, 4, 5]:
                raise ValueError("Invalid score")
        except (KeyError, ValueError):
            return render(request, 'projects/project_detail.html', {
                'project': project,
                'error_message': "유효한 점수를 선택해주세요 (1~5).",
            })

        Vote.objects.create(project=project, score=score)
        return redirect('projects:project_result', pk=pk)


class ProjectResultView(DetailView):
    model = Project
    template_name = 'projects/vote_result.html'
