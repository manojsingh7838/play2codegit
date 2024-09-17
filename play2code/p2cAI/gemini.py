import google.generativeai as genai

api_key = "AIzaSyBZVdiBJjgoV6V8y8oVMy9vUogdgkrZkMI"
genai.configure(api_key=api_key)


def get_ai_response(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
