from rest_framework import serializers
from .models import Landing, Skill, Card

class LandingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Landing
    fields = ['id', 'title', 'content']

class SkillSerializer(serializers.ModelSerializer):
  class Meta:
    model = Skill
    fields = ['id', 'skill', 'percent', 'knowledge']

class CardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Card
    fields = ['id', 'imagenProject', 'titleProject', 'contentProject', 'pdfProject']