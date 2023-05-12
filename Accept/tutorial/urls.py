from django.urls import path
from . import views


app_name = 'tutorial'
urlpatterns = [
    path('reading/', views.ReadingView.as_view(), name='read_english'),
    path('grammar/', views.GrammarView.as_view(), name='grammar_english'),
    path('write/', views.WritingView.as_view(), name='write_english'),
    path('Pronunciation/', views.PronunciationView.as_view(), name='pronunciation_english'),
    path('fun/', views.FunView.as_view(), name='fun_english'),
    path('Course/', views.CourseView.as_view(), name='course_english'),
]
