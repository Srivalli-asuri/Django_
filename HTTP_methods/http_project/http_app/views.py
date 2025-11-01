from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

# @csrf_exempt   #for ignoring the security for this view
# def welcome(self):
#     return HttpResponse("welcome to django app!!")

@csrf_exempt
def welcome(req):
    if req.method=="GET":
        return HttpResponse("welcome to get request")
    else:
        return HttpResponse("Invalid Method")
    

details=[
    {
        "id_":1,
        "name":"srivalli",
        "class":"42r"
        
    },
    {
        "id_":2,
        "name":"sri",
        "class":"42"
       
    }
]
@csrf_exempt
def details_view(req):
    return JsonResponse({"response":details})


@csrf_exempt
def singleuser(req,id):
    for user in details:
        if id==user["id_"]:
            return JsonResponse({"userdata" : user}) 
       
    return JsonResponse({"msg":"user doesnt exist"})
    # return JsonResponse({"user":id})


@csrf_exempt
def register_user(req):
    # for prop in dir(req):
    #     print(prop,req[prop])

    user_data=json.loads(req.body)
    for user in details:
        if user_data["id_"]==user["id_"]:
            return JsonResponse({"message":"user already exists"})

    ##else append it 
    details.append(user_data)
    print(details)
    return HttpResponse({"message":"registartion succesfull"})
