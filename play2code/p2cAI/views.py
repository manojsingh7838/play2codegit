# qna/views.py
from django.http import JsonResponse
from django.shortcuts import render
from .forms import QuestionForm
from .gemini import get_ai_response


def ask_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data["question"]
            response_text = get_ai_response(question)
            return JsonResponse({"response": response_text})
        else:
            return JsonResponse({"error": "Invalid form data"}, status=400)
    else:
        form = QuestionForm()

    return render(request, "ask_question.html", {"form": form})
