from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from .models import Landing, Skill, Card
from .serializers import LandingSerializer, SkillSerializer, CardSerializer


# Create your views here.
class LandingViewSet(viewsets.ModelViewSet):
  queryset = Landing.objects.all()
  serializer_class = LandingSerializer

class SkillViewSet(viewsets.ModelViewSet):
  queryset = Skill.objects.all()
  serializer_class = SkillSerializer

class CardViewSet(viewsets.ModelViewSet):
  queryset = Card.objects.all()
  serializer_class = CardSerializer
  parser_classes = [MultiPartParser]
  permission_classes = [AllowAny]
