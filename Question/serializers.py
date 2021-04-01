from rest_framework import serializers

from Question.models import Question, Choice


class ChoiceSerializer(serializers.Serializer):
    choice_text = serializers.CharField(max_length=1000)
    created_date = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)
    valid_answer = serializers.CharField(max_length=1)

    # DRF serializer.save() calls self.create(self.validated_data)
    def create(self, validated_data):
        return Choice.objects.create(**validated_data)

    # Add update() implementation on FeetSerializer
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class QuestionSerializer(serializers.Serializer):
    question_text = serializers.CharField(max_length=1000)
    created_date = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)
    choices = ChoiceSerializer(many=True, read_only=True)

    # DRF serializer.save() calls self.create(self.validated_data)
    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    # Add update() implementation on FeetSerializer
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class AnswerSerializer(serializers.Serializer):
    choice_id = serializers.ListField()
