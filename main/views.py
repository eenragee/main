from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from .models import UserFirst, UserReview
from django.db.models import Q
from django.http import JsonResponse


class HomePageView(TemplateView):
    template_name = 'main/index.html'


class SearchResultsView(ListView):
    model = UserFirst
    template_name = 'main/search_results.html'

    # def get_queryset(self):
        # query = self.request.GET.get('q')
        # object_list = UserFirst.objects.filter(
        #     Q(name__icontains=query) | Q(phone__icontains=query))
        #
        # object_list_user = UserReview.objects.filter(
        #     Q(name_user__icontains=query) | Q(phone_user__icontains=query)
        # )
        # return object_list


    # model = UserReview
    # template_name = 'main/search_results.html'
    # queryset = Serch.objects.filter(name__icontains='f')
    # def get_queryset(self):
    #     query = self.request.GET.get('q')
    #     object_list = UserReview.objects.filter(
    #         Q(name_user__icontains=query) | Q(phone_user__icontains=query)
    #     )
    #     return object_list
