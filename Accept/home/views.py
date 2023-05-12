from django.shortcuts import render
from django.views import View
from .forms import SearchForm
from .models import Introduction
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Greatest



class HomeView(View):
    template_name = 'home/index.html'
    form_class = SearchForm

    def get(self, request):
        intros = Introduction.objects.all()
        form = self.form_class
        if 'search' in request.GET:
            form = self.form_class(request.GET)
            if form.is_valid():
                cd = form.cleaned_data['search']
                intros = intros.annotate(similarity=Greatest(
                    TrigramSimilarity('name', cd),
                    TrigramSimilarity('description', cd),
                )).filter(similarity__gt=0).order_by('-similarity')
        return render(request, self.template_name, {'form': form, 'intros': intros})
