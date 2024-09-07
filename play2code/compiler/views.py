from django.shortcuts import render
from django.http import JsonResponse
import http.client
import json


import http.client
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

        request_body = json.dumps(
            {
                "source_code": code,
                "language_id": language_ids.get(language),
                "stdin": "",  # If you have input for the program, provide it here
                "cpu_time_limit": "5",
                "memory_limit": "128000",
            }
        )

        try:
            conn = http.client.HTTPSConnection("judge0-ce.p.rapidapi.com")
            headers = {
                "Content-Type": "application/json",
                "x-rapidapi-key": "6960b7386bmshff3ee000ba79ff0p1bf14fjsn8f994617fb47",  # Replace with your actual RapidAPI key
                "x-rapidapi-host": "judge0-ce.p.rapidapi.com",
            }

            conn.request(
                "POST",
                "/submissions/?base64_encoded=false&wait=true",
                body=request_body,
                headers=headers,
            )
            response = conn.getresponse()
            result = json.loads(response.read().decode("utf-8"))

            print("Full API Response:", result)

            status_description = result.get("status", {}).get("description")
            if status_description == "Accepted":
                output = result.get("stdout", "No Output")
            elif status_description == "Compilation Error":
                output = f"Compile Error: {result.get('compile_output', 'No Compilation Output')}"
            elif status_description == "Runtime Error":
                output = (
                    f"Runtime Error: {result.get('stderr', 'No Runtime Error Output')}"
                )
            elif status_description == "Wrong Answer":
                output = f"Wrong Answer: {result.get('stdout', 'No Output')}"
            else:
                output = f"Unexpected Result: {json.dumps(result, indent=2)}"

        except Exception as e:
            output = f"Error: {str(e)}"

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({"output": output})

    return render(request, "index.html", {"output": output})

