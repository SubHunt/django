from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# from django.template import loader

from django.views.generic.edit import CreateView
from .forms import BbForm
from .models import Bb, Rubric
from django.urls import reverse_lazy

def index(request):
    # template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    # return HttpResponse(template.render(context, request))
    return render (request, 'bboard/index.html', context)

def rubric_bbs(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get (pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render (request, 'bboard/rubric_bbs.html', context)

class BbCreateView(CreateView):
    template_name = 'bboard/bb_create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


