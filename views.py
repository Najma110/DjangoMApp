from django.shortcuts import render, HttpResponse
import random
def home(request):
   return render(request, 'home.html')

# Create your views here.
def calculate(request):
    feedback = None
    if request.method == 'POST':
        # This section is for when a quiz answer is submitted
        operation = request.POST.get('operation')
        operand1 = int(request.POST.get('operand1'))
        operand2 = int(request.POST.get('operand2'))
        user_answer = float(request.POST.get('answer'))

        # Calculate the correct answer based on the operation
        correct_answer = {
            'add': operand1 + operand2,
            'subtract': operand1 - operand2,
            'multiply': operand1 * operand2,
            'divide': operand1 / operand2,
        }.get(operation, 0)

        # Compare user's answer to the correct answer
        if user_answer == correct_answer:
            feedback = "Correct! Well done."
        else:
            feedback = f"Incorrect. The correct answer is {correct_answer}."
    
    # Generate a new question for either the initial load or after submitting an answer
    operations = ['add', 'subtract', 'multiply', 'divide']
    operation = random.choice(operations)
    operand1 = random.randint(1, 10)
    operand2 = random.randint(1, 10) if operation != 'divide' else random.randint(1, 10) * operand1  # Ensuring divisibility

    question_map = {
        'add': f"{operand1} + {operand2}",
        'subtract': f"{operand1} - {operand2}",
        'multiply': f"{operand1} × {operand2}",
        'divide': f"{operand1} ÷ {operand2}",
    }

    question = question_map[operation]

    context = {
        'question': question,
        'operation': operation,
        'operand1': operand1,
        'operand2': operand2,
        'feedback': feedback,
    }
    
    return render(request, 'calculate.html', context)
