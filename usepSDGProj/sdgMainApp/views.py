from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

from .sqlparams import *
from .sqlcommands import * 
from sdgDashApp.sqlcommands import *
from sdgDashApp.models import sdgPolicies

# Create your views here.
def index(request):
    return render(request,'themes/index.html')

def commitment(request):
    return render(request, 'themes/commitment.html')

def strategy(request):
    return render(request, 'themes/strategy.html')

def sustainPPA(request):
    return render(request, 'themes/sustainability-ppa.html')

def contact(request):
    return render(request, 'themes/contact.html')

def scorecard(request):
    return render(request, 'themes/sdg-scorecard.html')

def goal(request, goal_id):
    goalId = goal_id
    template_name = f'themes/goal{goal_id}.html'  # Dynamically construct the template path
    return render(request, template_name,{"goalId": goalId})

def goalTopic(request,goal_id,sdgScoreId):
    return render(request,'themes/goal-topic.html', {"goal_id": goal_id,"sdgScoreId": sdgScoreId})

def goalJsonFetchPerId(request,id):
    sgdParams['sdgId'] = id
    with connection.cursor() as cursor:
        cursor.execute(sdgDetailsViewPerId(**sgdParams))
        rows = cursor.fetchall()

        sdg = {}
        target_map = {}
        indicators_map = {}

        for row in rows:
            sdgId = row[0]
            if sdgId not in sdg:
                sdg[sdgId] = {
                    "sdgId": row[0],
                    "sdgName": row[1],
                    "description": row[2],
                    "isActive": row[3],
                    "targets": []
                }

            targetId = row[4]
            if targetId:
                if targetId not in target_map:
                    tgt = {
                        "sdgId": row[0],
                        "targetId": row[4],
                        "targetCode": row[6],
                        "targetDesc": row[7],
                        "isActive": row[8],
                        "indicators": []
                    }
                    sdg[sdgId]["targets"].append(tgt)
                    target_map[targetId] = tgt
                else:
                    tgt = target_map[targetId]

                ind_id = row[9]
                if ind_id and ind_id not in indicators_map:
                    ind = {
                        "indId": row[9],
                        "targetId": row[10],
                        "indCode": row[11],
                        "indDesc": row[12],
                        "isActive": row[13],
                    }
                    tgt["indicators"].append(ind)
                    indicators_map[ind_id] = ind

        data = list(sdg.values())
        return JsonResponse({"data": data}, json_dumps_params={'indent': 2})

@csrf_exempt
def getSdgScorecardJsonList(request,id):
    sdgScorecard['sdgScoreId'] = id

    with connection.cursor() as cursor:
        cursor.execute(getSdgScorecard(**sdgScorecard))
        rows = cursor.fetchall()

    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            "sdgScoreId":row[0],
            "susStratName":row[1],
            "greenName":row[2],
            "sdgInitName":row[3],
            "sdgImpYear":row[4],
            "sdgDesc":row[5],
            "outputs":row[6],
            "outcome":row[7],
            "personnel":row[8],
            "links":row[9],
            "enCodedBy":row[10],
            "enCodedDate":row[11],
            "isActive":row[12],
            "goal":row[13],
            "target":row[14],
            "indicator":row[16],
        }

        jsonResultData.append(tempRes)

    return JsonResponse({"data":list(jsonResultData)},safe=False)

def getSDGJsonList(request):
    with connection.cursor() as cursor:
        cursor.execute(fetchSDGIds())
        rows = cursor.fetchall()

    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            "sdgScoreId":row[0],
            "sdgId":row[1],
            "targetId":row[2],
            "indId":row[3]
        }

        jsonResultData.append(tempRes)

    return JsonResponse({"data":list(jsonResultData)},safe=False)

def getGoalListJsonList(request,id):
    sgdParams['sdgId'] = id

    with connection.cursor() as cursor:
        cursor.execute(getGoalList(**sgdParams))
        rows = cursor.fetchall()

    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            "sdgScoreId":row[0],
            "susStratName":row[1],
            "greenName":row[2],
            "sdgInitName":row[3],
            "sdgImpYear":row[4],
            "sdgDesc":row[5],
            "outputs":row[6],
            "outcome":row[7],
            "personnel":row[8],
            "links":row[9],
            "enCodedBy":row[10],
            "enCodedDate":row[11],
            "isActive":row[12],
            "goal":row[13],
            "target":row[14],
            "indicator":row[16],
        }

        jsonResultData.append(tempRes)

    return JsonResponse({"data":list(jsonResultData)},safe=False)

def greenCampus(request):
    return render(request,'themes/green-campus.html' )

def campusMap(request):
    return render(request,'themes/campus-map.html')

def campusObrero(request):
    return render(request,'themes/campus-obrero.html')

def campusMalabog(request):
    return render(request,'themes/campus-malabog.html')

def campusMintal(request):
    return render(request,'themes/campus-mintal.html')

def campusTagum(request):
    return render(request,'themes/campus-tagum.html')

def campusMabini(request):
    return render(request,'themes/campus-mabini.html')


def sdgPoliciesView(request):
    policyList = sdgPolicies.objects.raw(fetchSDGPolicy())
    return render(request, 'themes/policies.html', {'policyList':policyList} )

def getSdgPoliciesJsonList(request):
    with connection.cursor() as cursor:
        cursor.execute(fetchSDGPolicy())
        rows = cursor.fetchall()

    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            "sdgPolId":row[0],
            "title":row[1],
            "description":row[2],
            "imgPath":row[3],
            "linkPath":row[4],
            "isActive":row[5]
           }
        jsonResultData.append(tempRes)
    return JsonResponse({"data":list(jsonResultData)},safe=False)


def sdgNetwork(request):
    return render(request,'themes/sdg-network.html')


def test(request):
    return render(request,'themes/test.html')

