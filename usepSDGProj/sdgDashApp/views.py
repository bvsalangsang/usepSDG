import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt


from .forms import *
from .sqlparams import * 
from .sqlcommands import *

# Create your views here.
def dashboard(request):
    return render(request,'sdgDashApp/themes/dashboard.html' )

def login(request):
    return render(request, 'sdgDashApp/themes/login.html')


# SDG 
def sdgView(request):
    form = SDGForms()
    # sdgList = SDGoals.objects.raw(fetchSDG())
    return render(request, 'sdgDashApp/themes/goals.html', {'form':form})

def sdgJsonList(request):
    with connection.cursor() as cursor:
        cursor.execute(fetchSDG())
        rows = cursor.fetchall()

    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            "sdgId":row[0],
            "sdgName":row[1],
            "description":row[2],
            "isActive":row[3]
        }

        jsonResultData.append(tempRes)

    return JsonResponse({"data":list(jsonResultData)},safe=False)

def sdgSaveUpdateParams(request):
    cursor = connection.cursor()
    form  = SDGForms()
    if(request.POST):
        form = SDGForms(request.POST)
        try:
            if form.is_valid():
                sgdParams['sdgId'] = request.POST['sdgId']
                sgdParams['sdgName'] = form['sdgName'].value()
                sgdParams['description'] = form['description'].value()
                sgdParams['isActive'] = 'Y'
                form = SDGForms()
                print("Debug: " + saveUpdateSDG(**sgdParams))
                cursor.execute(saveUpdateSDG(**sgdParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt
def sdgDeleteParams(request, id):
    cursor = connection.cursor()
    try:
        sgdParams["sdgId"] = id
        sgdParams["isActive"] = 'N'
        print("Debug: " + deleteSDG(**sgdParams))
        cursor.execute(deleteSDG(**sgdParams))
        return JsonResponse({"Status":"Deleted"})
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"Error":err}) 


#SDG TARGET 
def sdgTargetView(request):
    form = SDGTargetForms()
    sdgList = SDGoals.objects.raw(fetchSDG())
    return render(request, 'sdgDashApp/themes/target.html', {'form':form, 'sdgList':sdgList})

def sdgTargetJsonList(request):
    with connection.cursor() as cursor:
        cursor.execute(fetchSDGTarget())
        rows = cursor.fetchall()

    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            "targetId":row[0],
            "goal":row[2],
            "targetCode":row[3],
            "targetDesc":row[4],
            "isActive":row[5]
        }

        jsonResultData.append(tempRes)

    return JsonResponse({"data":list(jsonResultData)},safe=False)

def sdgTargetSaveUpdateParams(request):
    cursor = connection.cursor()
    form  = SDGTargetForms()
    if(request.POST):
        form = SDGTargetForms(request.POST)
        try:
            if form.is_valid():
                sgdTargetParams['targetId'] = request.POST['targetId']
                sgdTargetParams['sdgId'] = request.POST['sdgId']
                sgdTargetParams['targetCode'] = form['targetCode'].value()
                sgdTargetParams['targetDesc'] = form['targetDesc'].value()
                sgdTargetParams['isActive'] = 'Y'
                form = SDGTargetForms()
                print("Debug: " + saveUpdateSDGTarget(**sgdTargetParams))
                cursor.execute(saveUpdateSDGTarget(**sgdTargetParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt
def sdgTargetDeleteParams(request, id):
    cursor = connection.cursor()
    try:
        sgdTargetParams["targetId"] = id
        sgdTargetParams["isActive"] = 'N'
        print("Debug: " + deleteSDGTarget(**sgdTargetParams))
        cursor.execute(deleteSDGTarget(**sgdTargetParams))
        return JsonResponse({"Status":"Deleted"})
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"Error":err}) 

#SDG INDICATOR
def sdgIndicatorView(request):
    form = SDGIndicatorForms()
    sdgTargetList = SDGoals.objects.raw(fetchSDGTarget())
    return render(request, 'sdgDashApp/themes/indicator.html', {'form':form, 'sdgTargetList':sdgTargetList})

def sdgIndicatorJsonList(request):
    with connection.cursor() as cursor:
        cursor.execute(fetchSDGIndicator())
        rows = cursor.fetchall()

    tempRes = None
    jsonResultData = []

    for row in rows:
        tempRes = {
            "indId":row[0],
            "target":row[1],
            "indCode":row[2],
            "indDesc":row[3],
            "isActive":row[4]
        }

        jsonResultData.append(tempRes)

    return JsonResponse({"data":list(jsonResultData)},safe=False)

def sdgIndicatorSaveUpdateParams(request):
    cursor = connection.cursor()
    form  = SDGIndicatorForms()
    if(request.POST):
        form = SDGIndicatorForms(request.POST)
        try:
            if form.is_valid():
                sgdIndicatorParams['indId'] = request.POST['indId']
                sgdIndicatorParams['targetId'] = request.POST['targetId']
                sgdIndicatorParams['indCode'] = form['indCode'].value()
                sgdIndicatorParams['indDesc'] = form['indDesc'].value()
                sgdIndicatorParams['isActive'] = 'Y'
                form = SDGIndicatorForms()
                print("Debug: " + saveUpdateIndicatorTarget(**sgdIndicatorParams))
                cursor.execute(saveUpdateIndicatorTarget(**sgdIndicatorParams))
                return (JsonResponse({"Status": "Saved"}))
            else:
                print(form.errors)
                return JsonResponse({"Status":"Error"})
        except Exception as err:
            print(f"{type(err).__name__} was raised: {err}")
            return JsonResponse ({"err":err})
    else:
        return JsonResponse({"Status":"Wrong Request"})

@csrf_exempt
def sdgIndicatorDeleteParams(request, id):
    cursor = connection.cursor()
    try:
        sgdIndicatorParams["indId"] = id
        sgdIndicatorParams["isActive"] = 'N'
        print("Debug: " + deleteIndicatorTarget(**sgdIndicatorParams))
        cursor.execute(deleteIndicatorTarget(**sgdIndicatorParams))
        return JsonResponse({"Status":"Deleted"})
    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
        return JsonResponse ({"Error":err}) 


#SDG treeview
def sdgTreeView(request):
    return render(request, 'sdgDashApp/themes/goals-tree.html')

def sdgTreeJsonList(request):
    with connection.cursor() as cursor:
        cursor.execute(sdgDetailsView())
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



#login
# def logView(request):

#     if request.method=='POST':
#         employee_id = request.POST['EmployeeID']
#         password = request.POST['Password']
       
#         apiUrl = 'https://hris.usep.edu.ph/api/auth/login'  
#         apiToken = '496871859d96697ba10536775445fd8f'  

#         apiData = {
#             'pmaps_id': employee_id,
#             'password': password,
#             'token': apiToken
#         }
#         print(apiData)
#         try:
#             # Sending POST request to the external API
#             response = requests.post(apiUrl, data=apiData)

#             # Debug: Print raw response content
#             print("Status code:", response.status_code)
#             print("Headers:", response.headers)

#             # Check if the response is JSON
#             if response.status_code == 200 and response.headers.get('Content-Type') == 'application/json':
#                 response_data = response.json()

#                 # Handle successful authentication
#                 if response_data.get('status') == 'success':
#                     # Store the token or user info in the session
#                     token = response_data.get('token')  # Example: Assuming API returns a token
#                     request.session['api_token'] = token
#                     request.session['user_authenticated'] = True

#                     return JsonResponse({'status': 'success', 'message': 'Login successful'})
#                 else:
#                     return JsonResponse({'status': 'fail', 'message': response_data.get('message', 'Invalid credentials')})
#             else:
#                 return JsonResponse({'status': 'fail', 'message': 'Invalid response from authentication server'})

#         except requests.exceptions.RequestException as e:
#             print(e)
#             return JsonResponse({'status': 'fail', 'message': 'Authentication server error', 'error': str(e)})

#     return JsonResponse({'csrf_token': get_token(request)})
#     # return render(request, 'sdgDashApp/themes/login.html')  # Your login template

@csrf_exempt
def logView(request):
    if request.method == 'POST':
        employee_id = request.POST.get('EmployeeID')
        password = request.POST.get('Password')

        apiUrl = 'https://hris.usep.edu.ph/api/auth/login'
        apiToken = '496871859d96697ba10536775445fd8f'
        
        apiData = {
            'pmaps_id': employee_id,
            'password': password,
            'token': apiToken
        }
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

        try:
            # Sending POST request to the external API
            response = requests.post(apiUrl, json=apiData, headers=headers)

            # Debug: Print raw response content
            print("Status code:", response.status_code)
            print("Headers:", response.headers)
            print("Response content:", response.text)

            if response.status_code == 403:
                return JsonResponse({'status': 'fail', 'message': 'Access forbidden. Please check your credentials.'})

            # Check if the response is JSON
            if response.headers.get('Content-Type', '').startswith('application/json'):
                response_data = response.json()

                # Handle successful authentication
                if response_data.get('status') == 'success':
                    # Store the token or user info in the session
                    token = response_data.get('token')  # Example: Assuming API returns a token
                    request.session['api_token'] = token
                    request.session['user_authenticated'] = True

                    return JsonResponse({'status': 'success', 'message': 'Login successful'})
                else:
                    return JsonResponse({'status': 'fail', 'message': response_data.get('message', 'Invalid credentials')})
            else:
                return JsonResponse({'status': 'fail', 'message': 'Invalid response from authentication server'})

        except requests.exceptions.RequestException as e:
            print(e)
            return JsonResponse({'status': 'fail', 'message': 'Authentication server error', 'error': str(e)})

    return JsonResponse({'csrf_token': get_token(request)})

