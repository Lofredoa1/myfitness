from .models import Exercise
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exercise
        fields = ['title', 'reps', 'sets', 'rest', 'completed']