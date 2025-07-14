# mysite/urls.py
from django.contrib import admin
from django.urls import path, include
from books import views  # ✅ HomeView가 여기에 있으므로 books에서 import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),  # 루트 URL이 HomeView
    path('polls/', include('polls.urls')),
    path('books/', include('books.urls')),
]
