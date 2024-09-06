# views.py
from django.shortcuts import render
import requests
import json


def code_compiler(request):
    output = None
    if request.method == "POST":
        code = request.POST.get("code")
        language = request.POST.get("language")

        language_ids = {
            "python": 71,
            "java": 62,
            "cpp": 54,
            "c": 50,
            "sql": 82,
        }

        # Prepare the request body for Judge0 API
        request_body = {
            "source_code": code,
            "language_id": language_ids.get(language),
            "stdin": "",
            "expected_output": "",
            "cpu_time_limit": "5",
            "memory_limit": "128000",
        }

        # Make the request to the Judge0 API
        try:
            response = requests.post(
                "https://api.judge0.com/submissions/?base64_encoded=false&wait=true",
                headers={"Content-Type": "application/json"},
                data=json.dumps(request_body),
            )
            result = response.json()

            if result.get("stderr"):
                output = f"Error: {result['stderr']}"
            elif result.get("compile_output"):
                output = f"Compile Error: {result['compile_output']}"
            else:
                output = result.get("stdout", "No Output")

        except Exception as e:
            output = f"Error: {str(e)}"

    return render(request, "index.html/", {"output": output})
