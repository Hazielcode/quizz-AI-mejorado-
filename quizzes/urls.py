from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuestionViewSet, ChoiceViewSet, api_root

# Router principal para las rutas de los viewsets
router = DefaultRouter()
router.register(r'quizzes', QuizViewSet, basename='quiz')
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'choices', ChoiceViewSet, basename='choice')

urlpatterns = [
    path('', api_root, name='api-root'),       # 📌 Endpoint raíz con info de la API
    path('', include(router.urls)),            # 📌 Endpoints CRUD (quizzes, questions, choices)
]
