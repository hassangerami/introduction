from django.contrib import admin
from .models import ReadingEnglish, GrammarEnglish, WritingEnglish, Pronunciation, Fun, Course


admin.site.register(ReadingEnglish)
admin.site.register(GrammarEnglish)
admin.site.register(WritingEnglish)
admin.site.register(Pronunciation)
admin.site.register(Fun)
admin.site.register(Course)
