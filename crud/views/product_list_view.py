from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.product import Product

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 3
    
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = '__all__'
    
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'
    
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('list')
    