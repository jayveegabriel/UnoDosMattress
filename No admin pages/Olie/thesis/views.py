from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
       'temperature': reverse('unodosmattress:temperature-list', request=request, format=format),
       'bed': reverse('unodosmattress:bed-list', request=request, format=format),
       'heartRate': reverse('unodosmattress:heartRate-list', request=request, format=format),
})
