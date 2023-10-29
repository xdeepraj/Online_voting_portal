from django.shortcuts import get_object_or_404, render, redirect
from datetime import datetime
from . models import Candidate, Position, Vote
from . forms import CandidateForm
from django.contrib import messages
from django.http import Http404
# from django.http import HttpResponseRedirect
# import os
from twilio.rest import Client
# from users.models import CustomUser



def candidate_list(request):
    # Get current year
    now = datetime.now()
    current_year = now.year
    
    candidate_list = Candidate.objects.all()
    position_list = Position.objects.all()
    
    return render(request, 'candidate_list.html', {
        "candidate_list": candidate_list,
	    "position_list": position_list,
        "current_year": current_year,
    })

def add_candidate(request):
    # Get current year
    now = datetime.now()
    current_year = now.year
    #Form content
    submitted = False
    if request.method == "POST":
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added a voter!!!")
            return render(request, 'home.html')
    else:
        form = CandidateForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'authenticate/add_candidate.html', {
        "current_year": current_year,
        "form": form,
        "submitted": submitted,
    })

def vote_index(request):
	latest_position_list = Position.objects.order_by('-pub_date')[:5]
	context = {'latest_position_list': latest_position_list}
	return render(request, 'authenticate/vote_index.html', context)

def detail(request, position_id):
    candidate = Candidate.objects.all()
    try:
        position = Position.objects.get(pk = position_id)
    except Position.DoesNotExist:
        raise Http404("Position does not exist")
    return render(request, 'authenticate/details.html', {
         'position': position,
         'candidate': candidate,
         })


def vote(request, position_id):
    user = request.user
    position = get_object_or_404(Position, pk = position_id)
    selected_choice = position.candidate_set.get(pk = request.POST['choice'])
    
    vote, created = Vote.objects.get_or_create(
                    user = user,        
                    position = position,  
                    defaults={'selected_choice': selected_choice},)
    
    if not created:
        messages.success(request, ("You already voted for this."))
        return redirect('home')
        
    else:
        selected_choice.votes += 1
        selected_choice.save()
        messages.success(request, ("Thanks for voting!!!"))

        message_to_broadcast = ("You have successfully voted for " + str(selected_choice))
        temp = ord('+') 
        number_to_broadcast = f"{chr(temp)}{91}{user.mobile_no}"
        account_sid = "AC53913ee84be4bae338fd7f809d381843"
        auth_token = "2ddfaab8953a18e0652beede3a15ec21"
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body=message_to_broadcast,
                            from_='+14454477602',
                            to=number_to_broadcast
                        )
        return redirect('home')
        

# def results(request, position_id):
# 	position = get_object_or_404(Position, pk = position_id)
# 	return render(request, 'authenticate/results.html', {'position': position})







