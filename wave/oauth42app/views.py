from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
import requests

def home(request):
    return render(request, 'home.html')

def user(request):
    return render(request, 'user.html')

def login(request):
    auth_url = f"https://api.intra.42.fr/oauth/authorize?client_id={settings.INTRA42_CLIENT_ID}&redirect_uri={settings.INTRA42_REDIRECT_URI}&response_type=code"
    return redirect(auth_url)

def callback(request):
    code = request.GET.get('code')
    if not code:
        return JsonResponse({'error': 'No code provided'}, status=400)

    token_url = 'https://api.intra.42.fr/oauth/token'
    data = {
        'grant_type': 'authorization_code',
        'client_id': settings.INTRA42_CLIENT_ID,
        'client_secret': settings.INTRA42_CLIENT_SECRET,
        'code': code,
        'redirect_uri': settings.INTRA42_REDIRECT_URI
    }

    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data.get('access_token')
        # Here you can store the access token in the session or return it to the client
        user_info_url = 'https://api.intra.42.fr/v2/me'
        requests_headers = {
			'Authorization': f'Bearer {access_token}'
		}
        userData = requests.get(user_info_url, headers=requests_headers)
        return JsonResponse(userData.json())
    else:
        return JsonResponse({'error': 'Failed to obtain access token'}, status=400)