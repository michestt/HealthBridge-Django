from django.shortcuts import render
from fitforum import models
from datetime import datetime
# Create your views here.

def index(request):
	posts = models.Post.objects.filter(enabled = True).order_by('-pub_time')[:30]
	levels = models.Level.objects.all()
	if request.user is not None:
		user = request.user
	try:
		user_id = request.GET['user_id']
		user_post = request.GET['user_post']
		user_level = request.GET['level']
		user_byear = request.GET['byear']
	except:
		user_id = None
		message = 'If you want to post a message,you must fill in each field...'
	if user_id!=None:
		level=models.Level.objects.get(status=user_level)
		post=models.Post.objects.create(level=level,nickname=user_id,message=user_post,byear=user_byear,enabled=True)
		post.save()
		message='Successfully saved'
	years = range(1911,2021)
	now = datetime.now()
	hour = now.timetuple().tm_hour

	return render(request,"fitforum/index.html", locals())


def fitness(request,tvno=0):
	if request.user is not None:
		user = request.user
	tv_list=[{'name':'Elementary Level of Fitness ','tvcode1':'2MoGxae-zyo','tvcode2':'2pLT-olgUJs','tvcode3':'I9nG-G4B5Bs','tvcode4':'3Pr6n-nKfMA','tvcode5':'UItWltVZZmE','tvcode6':'EyQgN7WmA9g'},
	{'name':'Intermediate Level of Fitness ','tvcode1':'QwrfHQ10JXo','tvcode2':'ILrtHlhCof8','tvcode3':'08VuDZx8Mmo','tvcode4':'9GASeOEr0Hk','tvcode5':'tN2jiQ83PNw','tvcode6':'SaiiLzTNVmo'},
	{'name':'High Level of Fitness ','tvcode1':'H2iKCywfWAM','tvcode2':'Y8xi-IvY7Mw','tvcode3':'n3HN4NQdcqU','tvcode4':'S5E9bmie4qg','tvcode5':'OXvQe9payHw','tvcode6':'3jVfAywaiOE'},
	{'name':'Healthy Diet  ','tvcode1':'R0HzjcGEeLc','tvcode2':'LLVf3d0rqqY','tvcode3':'EDW90TBXgqU','tvcode4':'T4NlwdLuEfs','tvcode5':'T73jYibRws8','tvcode6':'CN6GiTISGQU'},]
	now = datetime.now()
	hour= now.timetuple().tm_hour
	tvno=tvno
	tv=tv_list[tvno]
	return render(request,'fitforum/fitness.html',locals())




def yoga(request,tvno=0):
	if request.user is not None:
		user = request.user
	tv_list=[{'name':'Elementary Level of Yoga','tvcode1':'kN6ITw_AHQQ','tvcode2':'aRSPMMYOXZI','tvcode3':'N-wQIxxE-jY','tvcode4':'k-G2PzvQf7k','tvcode5':'zzonBs06mX8','tvcode6':'W0FxPT0O0SA'},
	{'name':'Intermediate Level of Yoga','tvcode1':'ZSIp00SewO8','tvcode2':'hJjqx6YlcWs','tvcode3':'jWMtgM_8jAE','tvcode4':'uxWJRKyUNZo','tvcode5':'JAOUZR3Jw3E','tvcode6':'hmUAQIxZwXw'},
	{'name':'High Level of Yoga','tvcode1':'BaFvtLpfL9U','tvcode2':'C1uSrTmyh9E','tvcode3':'jSBSGmg9j20','tvcode4':'EzClp1CiW5o','tvcode5':'uoMXtHa3CXg','tvcode6':'Ec4RuC_5Moc'},
	{'name':'Better Sleep Yoga ','tvcode1':'v7SN-d4qXx0','tvcode2':'E9LVKL2pGmo','tvcode3':'9lNiQIEfOAU','tvcode4':'bk71G6dXemc','tvcode5':'8Bi3Q20XrBM','tvcode6':'LI9upn4t9n8'}]
	now=datetime.now()
	hour= now.timetuple().tm_hour
	tvno=tvno
	tv=tv_list[int(tvno)]
	return render(request,'fitforum/yoga.html',locals())
