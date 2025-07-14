from django.apps import AppConfig

class BooksConfig(AppConfig):
    default = True  # ✅ 명시적으로 True 설정
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'
    verbose_name = 'Book-Author-Publisher App'  # ✅ 원하는 이름
