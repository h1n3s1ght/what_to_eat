from rest_framework import serializers
from main_app.models import Recipe, Member

class RecipeSerializer(serializers.ModelSerializer):
    RecipeDateAdded = serializers.DateField(required=False, allow_null=True)
    
    class Meta:
        model = Recipe
        fields = ('RecipeName', 'RecipeId', 'RecipeDateAdded')
        

class MemberSerializer(serializers.ModelSerializer):
    MemberPhoto_name = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = Member
        fields = ('MemberId', 'MemberFName', 'MemberLName', 'MemberPhoto_name')