from django.contrib import admin
from ProposalVoting.models import User,Proposal,Comment,Vote

admin.site.register(User) 
admin.site.register(Proposal) 
admin.site.register(Comment) 
admin.site.register(Vote) 
