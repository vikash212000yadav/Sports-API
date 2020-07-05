from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend

from api.models import Match, Sport, Selection, Market
from api.serializers import MatchListSerializer, MatchDetailSerializer

from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
# Create your views here.


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchListSerializer
    detail_serializer_class = MatchDetailSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    ordering_fields = '__all__'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class
        return super().get_serializer_class()

    def get_queryset(self):
        queryset = Match.objects.all()
        sport = self.request.query_params.get('sport', None)
        name = self.request.query_params.get('name', None)

        if sport is not None:
            sport = sport.title()
            queryset = queryset.filter(sport__name=sport)

        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset

    def create(self, request):
        message = request.data.pop('message_type')

        if message == "NewEvent":
            event = request.data.pop('event')
            sport = event.pop('sport')
            markets = event.pop('markets')[0]
            selections = markets.pop('selections')
            sport = Sport.objects.create(**sport)
            markets = Market.objects.create(**markets, sport=sport)

            for selection in selections:
                markets.selections.create(**selection)
            match = Match.objects.create(**event, sport=sport, market=markets)
            return Response(status=status.HTTP_201_CREATED)

        elif message == "UpdateOdds":
            event = request.data.pop('event')
            markets = event.pop('markets')[0]
            selections = markets.pop('selections')
            for selection in selections:
                s = Selection.objects.get(id=selection['id'])
                s.odds = selection['odds']
                s.save()
            match = Match.objects.get(id=event['id'])
            return Response(status=status.HTTP_201_CREATED)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
