from django.views.generic import TemplateView

class TopView(TemplateView):
    template_name = "top.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['h2'] = "SAMURAI"
        context['h3'] = [1,2,3]
        
        return context
        