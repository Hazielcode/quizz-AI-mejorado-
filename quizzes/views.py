from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Quiz, Question, Choice
from .serializers import (
    QuizSerializer, QuestionSerializer, ChoiceSerializer,
    QuizDetailSerializer, SubmitAnswerSerializer
)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'message': '🧠 Bienvenido a Quiz.AI API',
        'version': 'v1.0',
        'description': 'Sistema Inteligente de Gestión de Cuestionarios',
        'workflow': [
            '1️⃣ Crear un quiz (POST /quizzes/)',
            '2️⃣ Agregar preguntas (POST /questions/)',
            '3️⃣ Agregar opciones (POST /choices/)',
            '4️⃣ Ver quiz completo (GET /quizzes/{id}/)',
            '5️⃣ Enviar respuestas (POST /quizzes/{id}/submit/)'
        ],
        'endpoints': {
            'quizzes': reverse('quiz-list', request=request, format=format),
            'questions': reverse('question-list', request=request, format=format),
            'choices': reverse('choice-list', request=request, format=format),
        }
    })


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return QuizDetailSerializer
        return QuizSerializer

    @action(detail=True, methods=['post'])
    def submit(self, request, pk=None):
        quiz = self.get_object()

        # 👉 Aceptar tanto {"answers": [...]} como directamente [...]
        data = request.data.get('answers', request.data)

        serializer = SubmitAnswerSerializer(data=data, many=True)
        if not serializer.is_valid():
            return Response(
                {'error': '❌ Formato inválido', 'detalles': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        answers = serializer.validated_data
        results, correct_count = [], 0

        for answer in answers:
            try:
                question = Question.objects.get(id=answer['question_id'], quiz=quiz)
                choice = Choice.objects.get(id=answer['choice_id'], question=question)

                is_correct = choice.is_correct
                if is_correct:
                    correct_count += 1

                results.append({
                    'question_id': question.id,
                    'question_text': question.text,
                    'choice_id': choice.id,
                    'choice_text': choice.text,
                    'is_correct': is_correct,
                    'emoji': '✅' if is_correct else '❌'
                })
            except (Question.DoesNotExist, Choice.DoesNotExist):
                results.append({
                    'question_id': answer['question_id'],
                    'error': '⚠️ Pregunta u opción inválida'
                })

        total = len(results)
        percentage = round((correct_count / total) * 100, 2) if total else 0

        # Sistema de notas 🎓
        if percentage >= 90:
            grade, emoji, msg = 'A', '🏆', 'Sobresaliente'
        elif percentage >= 80:
            grade, emoji, msg = 'B', '🎉', 'Muy bien'
        elif percentage >= 70:
            grade, emoji, msg = 'C', '👍', 'Aceptable'
        elif percentage >= 60:
            grade, emoji, msg = 'D', '📚', 'Regular'
        else:
            grade, emoji, msg = 'F', '💪', 'Reintenta'

        return Response({
            'quiz_id': quiz.id,
            'quiz_title': quiz.title,
            'total_questions': total,
            'correct_answers': correct_count,
            'incorrect_answers': total - correct_count,
            'score': f"{correct_count}/{total}",
            'percentage': percentage,
            'grade': grade,
            'emoji': emoji,
            'message': f"{emoji} {msg}. Sacaste {correct_count} de {total} correctas.",
            'results': results
        })


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
