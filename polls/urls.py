from django.urls import path
from polls import views

app_name = 'polls'

urlpatterns = [
    path('name/', views.get_name, name='get_name'),
    path("", views.show_form),  # 또는 index
    path("form/", views.show_form, name="show_form"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
