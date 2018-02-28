from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView, CreateView, ListView, View
from .models import *
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'core/index.html'


class CreateBets(View):
    
    template_name = "core/bet_form.html"
    context = {
            'categories_list' : Category.objects.all(),
            'nominees_list' : Nominee.objects.all(),
            }

    def get(self, request, *args, **kwargs):
        self.context['user_bets'] = self.user_bets()
        return render(request, self.template_name, self.context)
        
    def post(self, request, *args, **kwargs):
        
        form = request.POST
        
        for k,v in form.items():
            if k != 'csrfmiddlewaretoken':
                user = request.user
                category = Category.objects.get(pk=k)
                nominee = Nominee.objects.get(pk=v[0])
                bet = Bet.objects.update_or_create(defaults={'nominee':nominee}, user=user, category=category)
        self.context['user_bets'] = self.user_bets()
        return render(request, self.template_name, self.context)
    
    def user_bets(self):
        dic = {}
        user_bets = Bet.objects.filter(user=self.request.user)
        
        for bet in user_bets:
            dic[bet.category.pk] = bet.nominee.pk
        return dic
        
        

class ListBet(ListView):
    model = Bet
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)