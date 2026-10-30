
# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import F
from django.shortcuts import get_object_or_404, redirect, render

from .forms import VoteForm
from .models import Question


def index(request):
    """Show all poll questions, newest first."""
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'polls/index.html', {'questions': questions})


def detail(request, question_id):
    """Show one question with its voting form."""
    question = get_object_or_404(Question, pk=question_id)
    form = VoteForm(question)
    return render(request, 'polls/detail.html', {'question': question, 'form': form})


@login_required  # only logged-in users can vote (authentication)
def vote(request, question_id):
    """Validate the submitted form and record the vote."""
    question = get_object_or_404(Question, pk=question_id)

    if request.method != 'POST':
        return redirect('polls:detail', question_id=question.id)

    form = VoteForm(question, request.POST)
    if form.is_valid():
        choice = form.cleaned_data['choice']
        choice.votes = F('votes') + 1  # safe, database-level increment
        choice.save()
        return redirect('polls:results', question_id=question.id)

    # Invalid form: show the page again with error messages
    return render(request, 'polls/detail.html', {'question': question, 'form': form})


def results(request, question_id):
    """Show the vote count for each choice."""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def signup(request):
    """Let new users create an account so they can vote."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('polls:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})