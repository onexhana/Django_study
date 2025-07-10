from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice

# ➊ Choice 모델을 Question 모델 안에서 함께 보이도록 인라인 설정
class ChoiceInline(admin.TabularInline):  # StackedInline → TabularInline로 변경됨
    model = Choice
    extra = 2  # 기본으로 표시될 빈 Choice 폼 수

# ➋ Question 모델에 대한 관리자 설정 클래스 정의
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [  # 필드 순서 및 UI 설정
        ('Question Statement', {'fields': ['question_text']}),  # 질문 입력 영역
        ('Date Information', {
            'fields': ['pub_date'],
            'classes': ['collapse'],  # 이 영역은 접혀서 표시됨
        }),
    ]
    inlines = [ChoiceInline]  # ➌ Choice 모델 클래스 같이 보기
    list_display = ('question_text', 'pub_date')  # ➍ 리스트 컬럼 설정
    list_filter = ['pub_date']  # ➎ 사이드 필터 추가
    search_fields = ['question_text']  # ➏ 검색창에서 question_text로 검색 가능

# ➐ 실제 관리자 사이트에 모델 등록
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
