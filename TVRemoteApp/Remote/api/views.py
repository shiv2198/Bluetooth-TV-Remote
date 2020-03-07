from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView
from Remote.models import Show,Customer
from .serializers import ListSerializersShow,ListSerializersUser
from rest_framework.filters import SearchFilter

class ShowList(ListAPIView):
	queryset=Show.objects.all()
	serializer_class=ListSerializersShow



class ShowDetailList(ListAPIView):
	queryset=Show.objects.all()
	serializer_class=ListSerializersShow
	filter_backends=[SearchFilter]
	search_fields=['S_name']
	'''
	def get(self,request,pk):
		query=request.GET.get("q")
		if query:
			queryset=queryset.filter(S_name__icontains=query)
		
	'''




class UserDetailList(ListAPIView):
	serializer_class=ListSerializersUser

	def get_queryset(self,*args,**kwargs):
		queryset=Customer.objects.filter(username = self.request.GET.get("u"),password=self.request.GET.get("p"))
		return queryset


	#lookup_field=('username','password')
'''
class BlogUpdateList(UpdateAPIView):
	queryset=Pst.objects.all()
	serializer_class=ListSerializers
	lookup_field='title'

'''