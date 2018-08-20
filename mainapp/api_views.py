from .models import Person, RescueCamp
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .models import RescueCamp, Person

class RescueCampSerializer(serializers.ModelSerializer):
    class Meta:
        model = RescueCamp
        fields = '__all__'

class RescueCampShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = RescueCamp
        fields = ('id', 'name', 'district')

class PersonSerializer(serializers.ModelSerializer):

	class Meta:
		model = Person
		fields = '__all__'

class CampListSerializer(serializers.Serializer):
	district = serializers.CharField()

class RescueCampViewSet(viewsets.ModelViewSet):
    queryset = RescueCamp.objects.filter()
    serializer_class = RescueCampSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['get', 'put', 'patch']

    """
        This view should return a list of all the RescueCamp
        for the currently user.
    """
    def get_queryset(self):
        return RescueCamp.objects.order_by('-id')


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.filter()
    serializer_class = PersonSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['post']

    def create(self, request):
        for data in request.data:
            serializer = PersonSerializer(data=data)

            data['age'] =  data['age'] or None

            if serializer.is_valid(raise_exception=True):

                camped_at = serializer.validated_data.get('camped_at', None)

                if camped_at :
                    serializer.save()
                else:
                    return Response({'error' : 'Rescue Camp is required field.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status':'success','message' : 'Person(s) added'}, status=status.HTTP_201_CREATED)

class CampList(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['get']

    def get(self, request):

        district = request.GET.get('district', None)

        if district :
            camps = RescueCamp.objects.filter(district=district)
            serializer = RescueCampShortSerializer(camps, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response({'error' : 'District Code is Required'}, status=status.HTTP_400_BAD_REQUEST)
