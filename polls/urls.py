# polls/urls.py

from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.show_form, name='index'),  # ✅ 이 라인 추가!
    path('name/', views.get_name, name='get_name'),
    path('form/', views.show_form, name='show_form'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
