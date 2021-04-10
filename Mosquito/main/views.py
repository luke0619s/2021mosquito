from django.shortcuts import render
from django.http import HttpResponse

import json
from pyecharts.charts import Bar
from pyecharts import options as opts
from rest_framework.views import APIView
from django.template.context_processors import request
from main import models


def main(request):
    return render(request, 'main/index.html', locals())

def maps(request):
    return render(request, 'main/map.html', locals())

def base(request):
    return render(request, 'main/base.html', locals())

def search(request): 
    
    try:
        name  = request.GET['name']
        year  = request.GET['year']
        month  = request.GET['month']
        day  = request.GET['day']
        result = models.local.objects.filter(name=name, year=year, month=month, day=day)
    except:
        name = 'fail'      
        
    return render(request, 'main/search.html', locals())

def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response

def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)

def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)

JsonResponse = json_response
JsonError = json_error

def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["2014", "2016", "2017", "2018", "2019", "2020"])
        .add_yaxis("臺北監測站(溫度)", [30,25,27,36,32,41])
        .set_global_opts(title_opts=opts.TitleOpts(title="測試", subtitle="測試副標題"))
        .dump_options_with_quotes()
    )
    return c
def bar_base2() -> Bar:
    c = (
        Bar()
        .add_xaxis(["2015", "2016", "2017", "2018", "2019", "2020"])
        .add_yaxis("新莊監測站(溫度)", [30,25,27,36,32,41])
        .set_global_opts(title_opts=opts.TitleOpts(title="測試", subtitle="測試副標題"))
        .dump_options_with_quotes()
    )
    return c
def bar_base3() -> Bar:
    c = (
        Bar()
        .add_xaxis(["2015", "2016", "2017", "2018", "2019", "2020"])
        .add_yaxis("南港監測站(溫度)", [30,25,27,36,32,41])
        .set_global_opts(title_opts=opts.TitleOpts(title="測試", subtitle="測試副標題"))
        .dump_options_with_quotes()
    )
    return c
def bar_base4() -> Bar:
    c = (
        Bar()
        .add_xaxis(["2015", "2016", "2017", "2018", "2019", "2020"])
        .add_yaxis("中山監測站(溫度)", [22,23,21,45,38,66])
        .set_global_opts(title_opts=opts.TitleOpts(title="測試", subtitle="測試副標題"))
        .dump_options_with_quotes()
    )
    return c
def bar_base5() -> Bar:
    c = (
        Bar()
        .add_xaxis(["2016", "2017", "2018", "2019", "2020"])
        .add_yaxis("信義監測站(溫度)", [77,55,67,56,52,21])
        .set_global_opts(title_opts=opts.TitleOpts(title="測試", subtitle="測試副標題"))
        .dump_options_with_quotes()
    )
    return c
def bar_base6() -> Bar:
    c = (
        Bar()
        .add_xaxis(["2015", "2016", "2017", "2018", "2019", "2020"])
        .add_yaxis("永春監測站(溫度)", [11,45,77,56,22,41])
        .set_global_opts(title_opts=opts.TitleOpts(title="測試", subtitle="測試副標題"))
        .dump_options_with_quotes()
    )
    return c

class ChartView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base()))

class ChartView2(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base2()))
class ChartView3(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base3()))
class ChartView4(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base4()))
class ChartView5(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base5()))
class ChartView6(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base6()))  

class data(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/data.html')