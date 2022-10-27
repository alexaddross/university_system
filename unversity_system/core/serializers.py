from rest_framework import serializers
from core.models import Discipline, StudentGroup, StudyingDirection


class StudyingDirectionSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    disciplines = serializers.ForeignKey()
    groups = serializers.ManyToManyField()

    class Meta:
        model = StudyingDirection
        fields = '__all__'


class StudentGroupSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    students = serializers.ManyToManyField()

    class Meta:
        model = StudentGroup
        fields = '__all__'


class DisciplineSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()

    class Meta:
        model = Discipline
        fields = '__all__'
