from rest_framework import serializers
from .models import Quiz, Question, Choice

# --- Serializers básicos ---
class QuizSerializer(serializers.ModelSerializer):
    """Serializer para lista de quizzes"""
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'image', 'created_at', 'updated_at']  # 👈 incluye image
        read_only_fields = ['created_at', 'updated_at']


class QuestionSerializer(serializers.ModelSerializer):
    """Serializer simple para crear/editar preguntas"""
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'text', 'created_at']
        read_only_fields = ['created_at']


class ChoiceSerializer(serializers.ModelSerializer):
    """Serializer simple para crear/editar opciones"""
    class Meta:
        model = Choice
        fields = ['id', 'question', 'text', 'is_correct']


# --- Serializers detallados (para mostrar quiz con preguntas y opciones) ---
class ChoiceDetailSerializer(serializers.ModelSerializer):
    """Serializer para opciones en detalle de pregunta (sin mostrar la correcta)"""
    class Meta:
        model = Choice
        fields = ['id', 'text']


class QuestionDetailSerializer(serializers.ModelSerializer):
    """Serializer para preguntas con sus opciones"""
    choices = ChoiceDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'choices']


class QuizDetailSerializer(serializers.ModelSerializer):
    """Serializer para ver un quiz con preguntas y contador"""
    questions = QuestionDetailSerializer(many=True, read_only=True)
    question_count = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'image', 'created_at', 'updated_at', 'question_count', 'questions']  # 👈 incluye image

    def get_question_count(self, obj):
        return obj.questions.count()


# --- Serializer para validar respuestas ---
class SubmitAnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    choice_id = serializers.IntegerField()
