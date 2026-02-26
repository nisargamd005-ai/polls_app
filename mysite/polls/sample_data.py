from polls.models import Question, Choice
from django.utils import timezone

def create_sample_poll():
    if Question.objects.exists():
        print("Sample poll already exists")
        return

    # Create question
    q = Question.objects.create(
        question_text="What is your favourite language?",
        pub_date=timezone.now()
    )

    # Add choices
    Choice.objects.create(question=q, choice_text="Python", votes=0)
    Choice.objects.create(question=q, choice_text="Java", votes=0)
    Choice.objects.create(question=q, choice_text="C++", votes=0)

    print("Sample poll created successfully!")