from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login as log_in, logout as log_out
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.decorators.http import require_http_methods
from rest_framework.exceptions import ValidationError

from django.views.generic import ListView
from .forms import LoginForm, RegisterForm
from .models import Profile, Image, Comments, Setting, Like
from .serializers import SettingSerializers, LikeSerializer
from rest_framework import generics, permissions


########################################################################################################################################################
def user_register(request):
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        User.objects.create_user(email=email, password=password, username=username)
    return render(request, 'register_login/register.html', {'form': register_form})


# @require_http_methods(["POST"])
# def user_register(request):
#     print("")
#     if request.method == "POST":
#         email = request.POST.get("email", None)
#         print("email")
#         phone = request.POST.get("phone", None)
#         if email:
#             if User.objects.filter(email__iexact=email).count() == 0:
#                 password = request.POST.get('password', None)
#                 repeated_password = request.POST.get('repeat_password', None)
#                 if password:
#                     if password == repeated_password:
#                         user = User.objects.create_user(email=email, password=password, username=phone,
#                                                         is_active=False)
#
#     else:
#         form = LoginForm()
#         return render(request, 'register_login/register.html', {'form': form})


###################################################################################################################################
def user_login(request):
    if request.method == 'POST':
        '''
         Instantiate the form with the submitted data with
         form = LoginForm(request.POST).
        '''
        form = LoginForm(request.POST or None)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticate'
                                        'successfully')
                else:
                    return HttpResponse('Disable account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'register_login/login.html', {
            'form': form})


######################################################################################################################################
####neshan dadan safheye home userha va posthashoon
class ImageList(ListView):
    model = Image
    template_name = 'register_login/images_list.html'
    context_object_name = 'image_list'

    def get_queryset(self):
        qs = Image.objects.filter(imageuploader_profile_id=self.request.user.id)

        return qs


########################################################################################################

#####neshan dadane posthaye followerha khode user


class MyFollowerImages(ListView):
    model = Profile
    template_name = "register_login/myfollowerimages.html"
    context_object_name = 'my_follower_images'

    def get_queryset(self):
        queryset = Profile.objects.filter(user_id=self.request.user.id).prefetch_related("followers").first()
        return queryset


#############################################################################################
###search

# def search(request, id):
#     print(id)
#     select = Profile.objects.filter(id=id)
#     sele = select[0].user
#     user_search_qs = Profile.objects.filter(first_name__icontains=sele)
#     print(user_search_qs)
#     return render(request, "register_login/search.html", {
#         "users_finded": user_search_qs
#     })


def search(request):
    if request.GET.get("q"):
        user_search_qs = User.objects.filter(username__icontains=request.GET.get("q", None))
        context = {
            "users_finded": user_search_qs,
        }
    else:
        user_search_qs = User.objects.all()
        context = {
            "users_finded": user_search_qs,
        }

    return render(request, "register_login/search.html", context)


################################################################################################################
####setting

class SettingList(generics.ListCreateAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializers


class SettingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializers


########################################################################################


class LikeCreate(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        post = Image.objects.get(pk=self.kwargs["pk"])
        return Like.objects.filter(liker=user, post=post)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError("you already liked for this post")
        serializer.save(liker=self.request.user, post=Image.objects.get(pk=self.kwargs["pk"]))
