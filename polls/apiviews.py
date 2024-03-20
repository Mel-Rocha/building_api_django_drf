from rest_framework import generics

from polls.models import Poll, Choice
from polls.serializers import PollSerializer, ChoiceSerializer, \
    VoteSerializer

class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer



class PollDetail(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer