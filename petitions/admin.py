from django.contrib import admin
from .models import Petition, Vote

@admin.register(Petition)
class PetitionAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'creator', 'yes_votes', 'no_votes', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('movie_name', 'description', 'creator__username')
    readonly_fields = ('created_at',)

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('petition', 'user', 'vote_type', 'voted_at')
    list_filter = ('vote_type', 'voted_at')
    search_fields = ('petition__movie_name', 'user__username')
    readonly_fields = ('voted_at',)
