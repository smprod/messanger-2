from django.shortcuts import get_object_or_404, render

from .forms import MessageForm
from .untils import FormListView
from .models import *
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView


        #class MessageList(CreateView):
            #model = Message
            #form_class = MessageForm
            #template_name = 'index.html'
            #success_url = reverse_lazy('home')

            #def get_context_data(self, **kwargs):
                #context = super().get_context_data(**kwargs)
                #context["object_list"] = Message.objects.all().filter(to_who=self.request.user).order_by('-id')
                #return context
            

            #def form_valid(self, form):
                #form.instance.from_who = self.request.user

                #return super().form_valid(form)


class ProfileAddMessage(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'show_chat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, id=self.kwargs['pk'])
        context["object_list"] = Message.objects.all().filter(Q(to_who=user) | Q(from_who=user)).order_by('id')
        context['prof'] = user
        return context
    

    def form_valid(self, form):
        user = User.objects.all().get(id=self.kwargs['pk'])
        form.instance.from_who = self.request.user
        form.instance.to_who = user

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('chat', kwargs={'pk': self.kwargs['pk']})

def index(request):
    return render(request, 'index.html')

def accounts(request):
    user = User.objects.all()
    return render(request, 'accounts.html', {'accounts': user})