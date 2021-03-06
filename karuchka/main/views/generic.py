from django.views import generic as views

from karuchka.common.view_mixins import RedirectToDashboard



class HomeView(RedirectToDashboard, views.TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context

