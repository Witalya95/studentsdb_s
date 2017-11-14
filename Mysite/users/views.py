from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_views(request):
	""" Завершує сеанс роботи  """
	logout(request)
	return HttpResponseRedirect(reverse('students:student_list'))

def register(request):
	#Реєстрація нового користувача
	if request.method != 'POST':
		#Створюється пуста форма
		form = UserCreationForm()
	else:
		#Обробка заповненої форми
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			#Виконується вхід і перенаправлення на домашню сторіку
			authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('students:student_list'))

	context = {'form': form}
	return render(request, 'users/register.html', context)
