from django.shortcuts import render, redirect
from django.views.generic import View
from models import User, Picture
import requests


class IndexView(View):
    url = 'show_gallery/index.html'
    def get(self, request):
        return render(request, self.url)

class Check_UserView(View):
    url = 'show_gallery/index.html'
    def get(self, request, pk):
        return render(request, self.url)

    def post(self, request):
        # Get username from html
        username = request.POST.get('username')
        # Check if username is empty
        if (username != ''):
            # Look for username in the database
            # Filter by username
            user = User.objects.filter(user_name=username)
            # If username exists in the database return its account_id
            if (user.count()>0):
                return redirect('show_gallery:template1', pk=user.values('account_id')[0]['account_id'])
            else:
                r = requests.get('https://api.instagram.com/v1/users/search?access_token=1497402817.1fb234f.1b8969bb3b304945a6782ae574069017&q={}' .format(username))
                # Check if the API request returns any data, meaning that the user exists in instagram
                data = r.json()['data']
                if (data != []):
                    # Add user to database
                    user = getUser(data, username)
                    username = user['username']
                    id = user['id']
                    new_user = User(account_id='{}'.format(id), user_name='{}' .format(username))
                    new_user.save()
                    # Get the pictures
                    r = requests.get('https://api.instagram.com/v1/users/{}/media/recent?access_token=1497402817.1fb234f.1b8969bb3b304945a6782ae574069017' .format(id))
                    r = r.json()
                    for picture in r['data']:
                        picture_name = picture['images']['standard_resolution']['url']
                        new_pic = Picture(user_name=new_user, picture_name='{}' .format(picture_name))
                        new_pic.save()
                    return redirect('show_gallery:template1', pk=id)
                # User does not exist
                else:
                    return render(request, 'show_gallery/index.html', {
                        'error_message': "User does not exist",
                    })
        else:
            return render(request, 'show_gallery/index.html', {
                'error_message': "Empty field",
            })

class TemplatesView(View):
    url = ''
    def get(self, request, pk):
        user = User.objects.filter(account_id=pk)
        return render(request, self.url, {'account_id': pk, 'picture_list': Picture.objects.filter(user_name=user)})

class Template1View(TemplatesView):
    url = 'show_gallery/template1.html'
class Template2View(TemplatesView):
    url = 'show_gallery/template2.html'
class Template3View(TemplatesView):
    url = 'show_gallery/template3.html'
class Template4View(TemplatesView):
    url = 'show_gallery/template4.html'
class Template5View(TemplatesView):
    url = 'show_gallery/template5.html'

# data is a list that contains all the users
def getUser(data, username_entered_by_user):
    for user in data:
        if user['username'] == username_entered_by_user:
            return user
