from rest_framework import serializers
from ProposalVoting.models import User,Proposal,Vote,Comment

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ('id','title','description', 'location','proposed_by','closed')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
            model = User
            fields = ('id', "user_name", "register_date","mail")

class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id','body','author','publication_date')

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('id','proposal_ID','user','value','date')



