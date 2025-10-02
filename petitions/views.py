from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Petition, Vote
from django.db import IntegrityError

def petition_list(request):
    petitions = Petition.objects.all()

    # Add user vote status to each petition
    if request.user.is_authenticated:
        for petition in petitions:
            try:
                user_vote = Vote.objects.get(petition=petition, user=request.user)
                petition.user_vote = user_vote.vote_type
            except Vote.DoesNotExist:
                petition.user_vote = None

    return render(request, 'petitions/petition_list.html', {'petitions': petitions})

@login_required
def create_petition(request):
    if request.method == 'POST':
        movie_name = request.POST.get('movie_name')
        description = request.POST.get('description')

        if movie_name and description:
            petition = Petition.objects.create(
                movie_name=movie_name,
                description=description,
                creator=request.user
            )
            messages.success(request, f'Petition for "{movie_name}" created successfully!')
            return redirect('petition_list')
        else:
            messages.error(request, 'Please fill in all fields.')

    return render(request, 'petitions/create_petition.html')

@login_required
def vote_petition(request, petition_id):
    petition = get_object_or_404(Petition, id=petition_id)

    if request.method == 'POST':
        vote_type = request.POST.get('vote_type')

        if vote_type in ['yes', 'no']:
            try:
                # Check if user already voted
                existing_vote = Vote.objects.filter(petition=petition, user=request.user).first()

                if existing_vote:
                    # Update vote if different
                    if existing_vote.vote_type != vote_type:
                        # Decrease old vote count
                        if existing_vote.vote_type == 'yes':
                            petition.yes_votes -= 1
                        else:
                            petition.no_votes -= 1

                        # Increase new vote count
                        if vote_type == 'yes':
                            petition.yes_votes += 1
                        else:
                            petition.no_votes += 1

                        existing_vote.vote_type = vote_type
                        existing_vote.save()
                        petition.save()
                        messages.success(request, 'Your vote has been updated!')
                    else:
                        messages.info(request, 'You have already voted this way.')
                else:
                    # Create new vote
                    Vote.objects.create(
                        petition=petition,
                        user=request.user,
                        vote_type=vote_type
                    )

                    # Update vote count
                    if vote_type == 'yes':
                        petition.yes_votes += 1
                    else:
                        petition.no_votes += 1
                    petition.save()

                    messages.success(request, 'Your vote has been recorded!')

            except IntegrityError:
                messages.error(request, 'An error occurred while recording your vote.')
        else:
            messages.error(request, 'Invalid vote type.')

    return redirect('petition_list')
