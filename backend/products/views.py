from django.contrib.auth.models import User
from django.http.response import JsonResponse
from .models import *
from django.conf import settings
from django.core.mail import message, send_mail
from rest_framework import generics, status
from rest_framework.response import Response
from .serializer import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,BasePermission
from rest_framework.authentication import TokenAuthentication
class WriteByAdminOnly(BasePermission):
    def has_permission(self,request,view):
        user = request.user
        if request.method == 'GET':
            return True
        if user.is_staff and (request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE'):
            return True
        return False
class Registration(generics.GenericAPIView):
    def post(self,request):
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            resp={
                "success":"registration succesfully"
            }
            return JsonResponse(resp,safe=False,status=200)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST) 
class Product(generics.ListCreateAPIView):
    queryset = product_master.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,WriteByAdminOnly]
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class ProductwithParamter(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,WriteByAdminOnly]
    queryset = product_master.objects.all()
    serializer_class = ProductSerializer
    def get(self,request,pk):
            try:
                allProduct = product_master.objects.get(id=pk)
                allAuctioninfo=Auction_info.objects.get(product=allProduct)
                resp={
                  'id':allProduct.id,
                  'name':allProduct.name,
                  'company_name':allProduct.company_name,
                  'model_year':allProduct.model_year,
                  'subcategory_name':allProduct.subcategory.subcategory_name,
                  'category_name':allProduct.subcategory.category.category_name,
                  'running_km':allProduct.running_km,
                  'fuel_type':allProduct.fuel_type,
                  'p_reg_date':allProduct.p_reg_date,
                  'price':allAuctioninfo.basePrice
                }
                print(resp)
                return JsonResponse(resp,safe=False,status=200)
            except product_master.DoesNotExist:
                resp={
                    "error":"Id not found"
                }
                return JsonResponse(resp,safe=False,status=404)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)
class Category(generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly,WriteByAdminOnly]
    queryset = category_master.objects.all()
    serializer_class = CategorySerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)  
class CategoryWithParameters(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly,WriteByAdminOnly]
    queryset = category_master.objects.all()
    serializer_class = CategorySerializer
    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk) 
class SubCategory(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,WriteByAdminOnly]
    queryset = subcategory_master.objects.all()
    serializer_class = SubCategorySerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class SubCategorywithParamter(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,WriteByAdminOnly]
    queryset = subcategory_master.objects.all()
    serializer_class = SubCategorySerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)
class Auctioninfo(generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated,WriteByAdminOnly]
    queryset = Auction_info.objects.all()
    serializer_class = AuctionSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        import json
        data = json.loads(request.body)
        productDetails = product_master.objects.get(id=data['product'])
        subject='welcome to sabert Bet'
        email_form =settings.EMAIL_HOST_USER
        for i in User.objects.all():
             message = f'Hi{i.first_name}  {productDetails.name}'
             reciver=[i.email,]
             send_mail(subject,message,email_form,reciver)
        return self.create(request)
class AuctionwithParamter(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,WriteByAdminOnly]
    queryset = Auction_info.objects.all()
    serializer_class = AuctionSerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)
