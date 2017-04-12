from django.http import HttpResponseRedirect
from django.shortcuts import render

__author__ = 'jhonjairoroa87'

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jsonp.renderers import JSONPRenderer

from .form import NameForm


class Multiply(APIView):

    renderer_classes = (JSONPRenderer,)

    @staticmethod
    def get(request):
        form = NameForm()

        return render(request, 'name.html', {'form': form})

    @staticmethod
    def post(request):
        print 'asdsadsadsdasadsad'
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            a = form.cleaned_data['one']
            b = form.cleaned_data['second']
            data = a*b 
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'name.html', {'data': data})


class Divide(APIView):

    renderer_classes = (JSONPRenderer,)

    @staticmethod
    def get(request):
        try:
            first_number = int(request.GET.get('a'))
            second_number = int(request.GET.get('b'))
            return Response({'result': first_number / second_number})
        except Exception as e:
            return Response({'result': 'there was an error ' + str(e)})

