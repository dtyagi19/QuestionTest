from django.urls import path

from Question import apiviews

urlpatterns = [
    path('questions/', apiviews.question_view, name='question_view'),
    path('questions/<int:question_id>/', apiviews.question_detail_view,
         name='question_detail_view'),
    path('questions/<int:question_id>/choices/', apiviews.choices_view,
         name='choices_view'),
    path('questions/<int:question_id>/answer/', apiviews.answer_view,
         name='answer_view'),
]
