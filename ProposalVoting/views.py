from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from ProposalVoting.models import User,Proposal,Vote,Comment
from ProposalVoting.serializers import ProposalSerializer, UserSerializer, CommentSerializer, VoteSerializer

#FunctionBasedView implementation
@api_view(['GET','POST'])
def proposal_list(request, format=None):
        """
        List all the proposal or create a new one.
        """
        if request.method == 'GET':
            proposal = Proposal.objects.all()
            serializer = ProposalSerializer(proposal, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = ProposalSerializer(data=request.DATA)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#ClassBasedView implementations using generic API defined by Django-REST-Framework
class proposal_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a proposal
    """
    model = Proposal
    serializer_class = ProposalSerializer

class user_list(generics.ListCreateAPIView):
    """
    List all the proposal or create a new one.
    """
    model = User
    serializer_class = UserSerializer


class user_detail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an user
    """
    model = User
    serializer_class = UserSerializer