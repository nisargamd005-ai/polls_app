from django.shortcuts import render, get_object_or_404, redirect
from .models import Question

def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice_id = request.POST.get('choice')
    if choice_id:
        selected_choice = question.choices.get(pk=choice_id)
        selected_choice.votes += 1
        selected_choice.save()
    return redirect('polls:index')