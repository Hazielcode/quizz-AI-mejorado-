from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.URLField(
        blank=True, null=True,
        help_text="URL de una imagen representativa del quiz (ej. portada)"
    )  # 👈 Imagen opcional para mostrar en el frontend
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def question_count(self):
        """Devuelve el número de preguntas asociadas al quiz"""
        return self.questions.count()


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, related_name='questions', on_delete=models.CASCADE
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"
        ordering = ['id']

    def __str__(self):
        return self.text[:50]


class Choice(models.Model):
    question = models.ForeignKey(
        Question, related_name='choices', on_delete=models.CASCADE
    )
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Opción"
        verbose_name_plural = "Opciones"
        ordering = ['id']

    def __str__(self):
        return self.text
