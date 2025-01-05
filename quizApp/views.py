from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def create_quiz(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', "")

        # It savs automatically
        quiz = Quiz.objects.create(
            title = title,
            description = description,
            created_by = request.user
        )

        for i in range(1,6):
            q_name = request.POST.get(f'question_{i}')

            if not q_name:
                continue

            question = Questions.objects.create(
                text = q_name,
                quiz = quiz, # directly pass the quiz instance
                created_by = request.user
            )
            
            options = [
                request.POST.get(f'option_{i}_1'),
                request.POST.get(f'option_{i}_2'),
                request.POST.get(f'option_{i}_3'),
                request.POST.get(f'option_{i}_4')
            ]
            
            correct_answer = int(request.POST.get(f'correct_{i}'))

            if correct_answer < 1 or correct_answer > 4:
                continue

            Options.objects.create(
                option1 = options[0],
                option2 = options[1],
                option3 = options[2],
                option4 = options[3],
                correct_answer = correct_answer,
                question = question
            )

        return redirect('/home/')

    return render(request, 'create.html', {'range':range(1,6)})

