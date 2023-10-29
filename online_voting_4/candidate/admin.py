from django.contrib import admin
from .models import Candidate, Position, Vote


class VoteAdmin(admin.ModelAdmin):
	model = Vote
	list_display = ['user', 'position', 'selected_choice',]
	
admin.site.register(Vote, VoteAdmin)

class CandidateAdmin(admin.ModelAdmin):
	model = Candidate
	list_display = ['first_name','votes',]
admin.site.register(Candidate, CandidateAdmin)

class ChoiceInLine(admin.StackedInline):
	model = Candidate
	extra = 0
	
class PositionAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['positions']}), 
	             ('Date Information', {'fields': ['pub_date']}),
		   ]
	inlines = [ChoiceInLine]

admin.site.register(Position, PositionAdmin)







