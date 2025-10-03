from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Likes
from blog.forms import CommentForm
from blog import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from calories.forms import CreateUserForm
from django.contrib import messages
from fitforum.models import Post as fit_Post

def homepage(request):
    if request.user is not None:
        user = request.user
        username = user.username

    blog_posts = Post.objects.all().filter(enabled=True).order_by('-published',)[:3]
    fitness_posts = fit_Post.objects.all().filter(enabled=True).order_by('-pub_time',)[:3]
    form_c = CommentForm()

    try:
        post_slug = request.POST['slug']
        comment_name = request.POST['name']
        comment_email = request.POST['email']
        comment_body = request.POST['body']
    except:
        post_slug = None

    if request.method == 'POST' and post_slug is not None:
        post = models.Post.objects.get(slug=post_slug)
        comment_post = models.Comment.objects.create(post=post, name=comment_name, body=comment_body,
                                                     email=comment_email)
        comment_post.save()

    return render(request, 'main_homepage.html', locals())


@login_required(login_url='login')
def like(request, slug):
    user = request.user
    post = get_object_or_404(Post, slug=slug)
    current_likes = post.likes
    liked = Likes.objects.filter(user=user, post=post).count()

    if not liked:
        like = Likes.objects.create(user=user, post=post)
        current_likes = current_likes + 1

    else:
        Likes.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1

    post.likes = current_likes
    post.save()

    return redirect('homepage')


def LoginPage(request, page=''):
    if request.user.is_authenticated:
        if page == '':
            redirect('homepage')
        else:
            redirect(page)
    else:
        # if request.session.test_cookie_worked():
        #     request.session.delete_test_cookie()
        #     messages.info(request, "cookie supported")
        # else:
        #     messages.info(request, "cookie not supported")
        # request.session.set_test_cookie()
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                if request.POST.get('remember_me'):
                    if page == '':
                        response = redirect('homepage')
                    else:
                        response = redirect(page)

                    # expires = 'Thu, 28-May-2020 08:53:06 GMT'  # 24小时 格林威治时间
                    # expires = datetime.datetime(2020, 5, 28, 23, 44, 55))
                    expires = 60 * 60 * 24
                    max_age = 60 * 60 * 24
                    response.set_cookie('c_username', username, expires=expires, max_age=max_age)
                    response.set_cookie('c_password', password, expires=expires, max_age=max_age)
                    return response

                if page == '':
                    return redirect('homepage')
                else:
                    return redirect(page)
            else:
                messages.warning(request, 'Username or password is incorrect')
        
        if request.COOKIES.get('c_username'):
            context = {
                'c_username': request.COOKIES['c_username'],
                'c_password': request.COOKIES['c_password'],
            }
        else:
            context = {}
        return render(request, 'login/login.html', context)



def LogOutPage(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def RegisterPage(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,"Account was created for "+ user)
                return redirect('login')

        context = {'form':form}

        return render(request, 'login/register.html', context)


def login1(request):


    return render(request, 'login/login2.html', locals())
