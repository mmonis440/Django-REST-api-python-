from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import question, choice
from django.template import loader
from django.http import Http404
from django.views import generic
from django.urls import reverse


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return question.objects.order_by('-publication_date')[:5]


class DetailView(generic.DetailView):
    model = question
    template_name = 'polls/details.html'


class ResultsView(generic.DetailView):
    model = question
    template_name = 'polls/results.html'


def vote(request, question_id):
    return HttpResponse("you are voting on question %s " % question_id)


def vote(request, question_id):
    question = get_object_or_404(question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
