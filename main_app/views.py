from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from main_app.models import Recipe, Member
from main_app.serializers import RecipeSerializer, MemberSerializer

from django.core.files.storage import default_storage


# Create your views here.

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def RecipeAPI(request, id=0):
    if request.method=='GET':
        Recipes = Recipe.objects.all()
        recipes_serializer = RecipeSerializer(Recipes, many=True)
        return JsonResponse(recipes_serializer.data, safe=False)
    
    elif request.method=='POST':
        Recipes_data = JSONParser().parse(request)
        Recipes_serializer = RecipeSerializer(data=Recipes_data)
        if Recipes_serializer.is_valid():
            Recipes_serializer.save()
            return JsonResponse("Added new recipe successfully!!", safe=False)
        return JsonResponse("Failed to create new recipe")
    
    elif request.method=='PUT':
        Recipes_data = JSONParser().parse(request)
        Recipes = Recipe.objects.get(RecipeId= Recipes_data['RecipeId'])
        Recipes_serializer = RecipeSerializer(Recipes, data=Recipes_data)
        if Recipes_serializer.is_valid():
            Recipes_serializer.save()
            return JsonResponse("Updated recipe successfully!!", safe=False)
        return JsonResponse("Failed to update recipe.", safe=False)
    
    elif request.method=='DELETE':
        Recipes = Recipe.objects.get(RecipeId=id)
        Recipes.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)
    

@csrf_exempt
def MemberAPI(request, id=0):
    if request.method=='GET':
        Members = Member.objects.all()
        Members_serializer = MemberSerializer(Members, many=True)
        return JsonResponse(Members_serializer.data, safe=False)
    
    elif request.method=='POST':
        Members_data = JSONParser().parse(request)
        Members_serializer = MemberSerializer(data=Members_data)
        if Members_serializer.is_valid():
            Members_serializer.save()
            return JsonResponse("Added new Member successfully!!", safe=False)
        return JsonResponse("Failed to create new Member")
    
    elif request.method=='PUT':
        Members_data = JSONParser().parse(request)
        Members = Member.objects.get(MemberId= Members_data['MemberId'])
        Members_serializer = MemberSerializer(Members, data=Members_data)
        if Members_serializer.is_valid():
            Members_serializer.save()
            return JsonResponse("Updated Member successfully!!", safe=False)
        return JsonResponse("Failed to update Member.", safe=False)
    
    elif request.method=='DELETE':
        Members = Member.objects.get(MemberId=id)
        Members.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)
    

@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)
    
    return JsonResponse(file_name, safe=False)