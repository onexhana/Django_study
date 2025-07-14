from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.apps import apps  # 📌 추가
from books.models import Book, Author, Publisher

# --- TemplateView ---
class BooksModelView(TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Book', 'Author', 'Publisher']
        return context

# --- ListView ---
class BookList(ListView):
    model = Book

class AuthorList(ListView):
    model = Author

class PublisherList(ListView):
    model = Publisher

# --- DetailView ---
class BookDetail(DetailView):
    model = Book

class AuthorDetail(DetailView):
    model = Author

class PublisherDetail(DetailView):
    model = Publisher

# --- HomeView ---
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dictVerbose = {}

        for app in apps.get_app_configs():
            if 'site-packages' not in app.path:
                dictVerbose[app.label] = app.verbose_name

        print("📦 verbose_dict:", dictVerbose)  # ✅ 이 줄 추가!!

        context['verbose_dict'] = dictVerbose
        return context
