# Create your views here.
from django.views.generic import ListView
from django.views.generic.edit import FormView
from books.forms import PublisherForm
from books.models import Publisher

class PublisherList(ListView):
    model = Publisher

class PublisherView(FormView):
    template_name = 'form.html'
    form_class = PublisherForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.add_to_db()
        return super(PublisherView, self).form_valid(form)
