from django.views.generic.base import TemplateView

# --- TemplateView ---
class HomeView(TemplateView):
    template_name = 'home.html'  # 렌더링할 템플릿 파일

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_list'] = ['polls', 'books']  # 템플릿에서 사용할 데이터
        return context
