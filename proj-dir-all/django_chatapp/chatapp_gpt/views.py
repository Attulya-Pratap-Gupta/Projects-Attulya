from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI


def get_completion(prompt):
    print(prompt)
    client = OpenAI(api_key="API KEY")
    completion = client.chat.completions.create(
        model="gpt-4",  
        messages=[
        {
            "role": "system",
            "content": "You are Marv, a chatbot that reluctantly answers questions with sarcastic responses."
        },
        {
            "role": "user", 
            "content": prompt
        }
        ],
        max_tokens=1024,
        temperature=0.5,
    )
    
    completion = completion.choices[0].message.content
    print(completion)
    return completion
  
  
def query_view(request): 
    if request.method == 'POST': 
        prompt = request.POST.get('prompt') 
        response = get_completion(prompt) 
        return JsonResponse({'response': response}) 
    return render(request, 'index.html')