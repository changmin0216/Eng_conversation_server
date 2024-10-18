from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

@login_required
def chat_room(request):
    return render(request, 'chatting/chat.html')

openai.api_key = settings.OPENAI_API_KEY

message = [
            {"role": "system", "content":
                    "I am Korean, and my English is at the level of initial."
                    "I want to practice daily English."
                    "Please help me practice the 5 English conversation patterns that native speakers usually use."
                    "And when I'm done, please correct any unnatural pronunciation, words, or grammar. "
                    "And then let me speak out and pronounce it again."
                    "Finally, after I'm done, please ask me additional questions about what I'm saying."
            },
        ]
@csrf_exempt
@login_required()
def chat(request):
    global message
    if request.method == 'OPTIONS' or request.method == 'POST':

        dic__q = json.loads(request.body)
        user_message = dic__q['message']

        message.append({"role": "user", "content" : user_message})
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=message
        )
        print(response)
        message.append({"role": "assistant", "content": response.choices[0].message.content})
        return JsonResponse({"response": response.choices[0].message.content})
