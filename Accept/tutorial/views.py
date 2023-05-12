from django.shortcuts import render
from django.views import View
from .models import ReadingEnglish, GrammarEnglish, WritingEnglish, Pronunciation, Fun, Course


class ReadingView(View):
    template_name = 'tutorial/reading.html'

    def get(self, request):
        reads = ReadingEnglish.objects.all()
        return render(request, self.template_name, {'reads': reads})


class GrammarView(View):
    template_name = 'tutorial/grammar.html'

    def get(self, request):
        grammars = GrammarEnglish.objects.all()
        return render(request, self.template_name, {'grammars': grammars})


class WritingView(View):
    template_name = 'tutorial/writing.html'

    def get(self, request):
        writes = WritingEnglish.objects.all()
        return render(request, self.template_name, {'writes': writes})


class PronunciationView(View):
    template_name = 'tutorial/pronunciation.html'

    def get(self, request):
        pronuns = Pronunciation.objects.all()
        return render(request, self.template_name, {'pronuns': pronuns})


class FunView(View):
    template_name = 'tutorial/fun.html'

    def get(self, request):
        funs = Fun.objects.all()
        return render(request, self.template_name, {'funs': funs})


class CourseView(View):
    template_name = 'tutorial/course.html'

    def get(self, request):
        courses = Course.objects.all()
        return render(request, self.template_name, {'courses': courses})
