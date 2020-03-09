from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Question
from django.template import loader
from django.views import generic
from django.utils import timezone

# with django generic views
class IndexView(generic.ListView):
    """!!!! ZMIENNE MUSZA SIE TAK NAZYWAC !!!!!"""
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    # pokazuje tylko do obecnego czasu pytania
    def get_queryset(self):
        """Return the last five published questions."""
        # lte -  znaczy less or queal to
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    # # pokazuje wszystkie pytania
    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    """!!!! ZMIENNE MUSZA SIE TAK NAZYWAC !!!!!"""
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    """!!!! ZMIENNE MUSZA SIE TAK NAZYWAC !!!!!"""
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    # full
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    #
    # shortcut
    question = get_object_or_404(Question, pk=question_id)
    # zbieramy wybyr uzytkownika
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "you didnt select choice",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))

# no django generic views
# def index(request):
#     # full
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     # context = {
#     #     'latest_question_list': latest_question_list,
#     # }
#     # return HttpResponse(template.render(context, request))
#     # shortcut
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     # full
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # template = loader.get_template('polls/detail.html')
#     # return HttpResponse(template.render({'question': question}, request))
#     # shortcut
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
#     # full
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # template = loader.get_template('polls/results.html')
#     # return HttpResponse(template.render({'question': question}, request))
#     # shortcut
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
