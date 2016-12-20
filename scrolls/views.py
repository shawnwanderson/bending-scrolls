from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from scrolls.forms import QueryForm#, ScrollForm
from scrolls.models import Scroll, Episode, Bender

# Create your views here.

class QueryView(FormView):
    template_name = "scrolls/index.html"
    form_class = QueryForm

class ScrollListView(ListView):
    model = Scroll
    
    def get_queryset(self):
        queryset = super(ScrollListView, self).get_queryset()
        request_params = request.GET.copy()
        queryset = queryset.filter(
            benders__in=request_params['benders'],
            element=request_params['element'],
            book=request_params['book'],
            episode=request_params['episode'],
                )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ScrollListView, self).get_context_data(**kwargs)
        return context

class ScrollDetailView(DetailView):
    model = Scroll
    def get_context_data(self, **kwargs):
        context = super(ScrollDetailView, self).get_context_data(**kwargs)
        return context

class ScrollCreate(CreateView):
    model = Scroll
    fields = ['title']

class ScrollUpdate(UpdateView):
    model = Scroll
    fields = ['title']
    template_name_suffix = '_update_form'

class ScrollDelete(DeleteView):
    model = Scroll
    success_url = reverse_lazy('scroll-list')


#
#
#
#  def scrolls(request):
#      template = "scrolls/scrolls.html"
#      request_params = request.GET.copy()
#      results = Scroll.objects.filter(
#              benders__in=request_params['benders'],
#              element=request_params['element'],
#              book=request_params['book'],
#              episode=request_params['episode'],
#              )
#      render(request, template, {'results':results})
#
#  def scroll(request, scroll_id):
#      template = "scrolls/scroll.html"
#      if request.method == "POST":
#          #Make new scroll
#      else:
#          scroll = Scroll.objects.get_or_404(scroll_id)
#          form = ScrollForm()
#
#
