from django.shortcuts import render, redirect

from .models import Candidates, Votes
from django.http.response import HttpResponseRedirect

# Create your views here.
def index(request):

    candidate_one = Candidates.objects.get(pk=1)
    candidate_two = Candidates.objects.get(pk=2)
    candidate_three = Candidates.objects.get(pk=3)
    candidate_four = Candidates.objects.get(pk=4)

    if request.method == 'POST':

        voters = Votes()

        voters.first_name = request.POST.get('first_name')
        voters.last_name = request.POST.get('last_name')
        voters.voter_id = request.POST.get('voter_id')
        voters.voter_choice = request.POST.get('voter_choice')

        print (voters.first_name)
        print (voters.last_name)
        print (voters.voter_id)
        print (voters.voter_choice)

        voters.save()

        return render(request, "thanks.html")

    context = {
        "candidate_one" : candidate_one,
        "candidate_two" : candidate_two,
        "candidate_three" : candidate_three,
        "candidate_four" : candidate_four,
    }

    return render(request, "index.html", context)

def results(request):

    candidate_one_total = Votes.objects.filter(voter_choice="Reilly").count()
    candidate_two_total = Votes.objects.filter(voter_choice="Arjun").count()
    candidate_three_total = Votes.objects.filter(voter_choice="Sullivan").count()
    candidate_four_total = Votes.objects.filter(voter_choice="Leilani").count()

    context = {
        "candidate_one_total" : candidate_one_total,
        "candidate_two_total" : candidate_two_total,
        "candidate_three_total" : candidate_three_total,
        "candidate_four_total" : candidate_four_total,
    }

    return render(request, "results.html", context)
