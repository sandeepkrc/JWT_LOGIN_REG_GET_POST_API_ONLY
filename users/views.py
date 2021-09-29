from django.http import request
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer,AuthenticationSerializer, UniversitySerializer, DepartmentSerializer,HodSerializer, FacultySerializer,StudentSerializer, CourseSerializer, EventSerializer, EventpollSerializer, StudentPasswordSerializer, ContactSerializer, PaymentSerializer, DepartmentMapperSerializer, FacultyMapperSerializer, StudentMapperSerializer, RollNoMapperSerializer, EventMapperSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User,Department, University, Hod#Otp
import jwt
#for authentication and permission
from rest_framework.permissions import IsAuthenticated,AllowAny

class RegisterView(APIView):
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RegisterUniversityView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        # return Response({"asc":"sandeep get"})
        return render(request, 'f2.html')

    def post(self, request):
        serializer=UniversitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"posted the data successfully"})
        
        # return render(request, 'f2.html')

'''class Universitylist(APIView):
    def get(self,request):        
        #snippets = University.objects.all()
        #serializer = UniversitySerializer(snippets, many=True)
        #print(serializer.data)
        # return Response(serializer.data)
        return render(request,'f1.html')
    
    def post(self,request):        
        snippets = University.objects.all()
        serializer = UniversitySerializer(snippets, many=True)
        print(serializer.data)
        # return Response(serializer.data)
        return render(request,'f1.html',{'abc':serializer.data})
'''
class Universitylist(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        students = University.objects.all()
        serialized = UniversitySerializer(students, many=True)
        return Response(serialized.data)

def homepage(request):
    return render(request, 'f1.html')

def saveData(request):
    return render(request, 'f2.html')



class RegisterDepartmentView(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer=DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class Departmentlist(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self,request):        
        snippets = Department.objects.all()
        serializer = DepartmentSerializer(snippets, many=True)
        return Response(serializer.data)
        
# def addhod(request):
    # return render(request,"r1.html")
class RegisterHodView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self,request):
        return render(request,"r1.html")
    def post(self, request):
        print("hitted")
        serializer=HodSerializer(data=request.data)
        print("request.data printed==",request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            print("serialized==")
            return Response(serializer.data)
        print("unserialized==")
        return Response(serializer.errors)

class Hodlist(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self,request):        
        snippets = Hod.objects.all()
        serializer = HodSerializer(snippets, many=True)
        return Response(serializer.data)

class RegisterFacultyView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer=FacultySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RegisterStudentView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RegisterCourseView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer=CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RegisterEventView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer=EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class EventpollView(APIView):
    def post(self, request):
        serializer=EventpollSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class StudentPasswordView(APIView):
    def post(self, request):
        serializer=StudentPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ContactView(APIView):
    def post(self, request):
        serializer=ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class PaymentView(APIView):
    def post(self, request):
        serializer=PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class DepartmentMapperView(APIView):
    def post(self, request):
        serializer=DepartmentMapperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class FacultyMapperView(APIView):
    def post(self, request):
        serializer=FacultyMapperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class StudentMapperView(APIView):
    def post(self, request):
        serializer=StudentMapperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class RollNoMapperView(APIView):
    def post(selfself, request):
        serializer=RollNoMapperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class EventMapperView(APIView):
    def post(selfself, request):
        serializer=EventMapperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
#added by sandeep login through jwt 
from rest_framework_simplejwt.views import TokenObtainPairView
class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = AuthenticationSerializer
    
# class LoginView(APIView):
    # def post(self, request):
    #     email=request.data['email']
    #     password=request.data['password']

    #     user=User.objects.filter(email=email).first()
    #     if user is None:
    #         raise AuthenticationFailed('User Not Found')

    #     if not user.check_password(password):
    #         raise AuthenticationFailed('Incorrect Passsword')

    #     #generating token
    #     payload={
    #         'id':user.id,
    #         'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
    #         'iat':datetime.datetime.utcnow()
    #     }
    #     token=jwt.encode(payload, 'secretMessage', algorithm='HS256')

    #     response=Response()
        
        

    #     #setting Cookie
    #     response.set_cookie(key='jwt', value=token, httponly=True)
    #     response.data={
    #         'jwt':token
    #     }
    #     return response

class UserView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload=jwt.decode(token, 'secretMessage', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user =User.objects.filter(id=payload['id']).first()
        serializer=UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    
    def post(self, request):
        response=Response()
        response.delete_cookie('jwt')
        response.data={
            'message':'Logout SuccessFull'
        }
        return response
    
# ########################PASSWORD RESET VIEWS #######################
# from .serializer import ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer
# from rest_framework.views import APIView
# from rest_framework import status, generics
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from .models import User

# from .email_services import sent_mail

# import random
# from django.utils import timezone
# class RequestPasswordReset(generics.GenericAPIView):

#     def post(self, request):
#         try:
#             user = User.objects.get(email=request.data['email'])
#         except User.DoesNotExist:
#             return Response({'error': "We will send you the otp if the email exist on our database."})
#         otp, created = OTP.objects.get_or_create(user=user)
#         otp.otp = random.randint(100000, 999999)
#         otp.expiry_time = timezone.now()  # add time delta
#         otp.save()
#         email_body = f'Hello,  this OTP to reset your password  {otp.otp}'
#         data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Reset your passsword'}
#         sent_mail(data)
#         return Response({'success': 'We have sent you a OTP to reset your password', 'otp': otp.otp},
#                         status=status.HTTP_200_OK)

# class SetNewPasswordAPIView(generics.GenericAPIView):
#     serializer_class = SetNewPasswordSerializer

#     def put(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.validated_data.get('otp').user.set_password(serializer.validated_data.get('password'))
#         serializer.validated_data.get('otp').delete()
#         # OTP.objects.filter(user=serializer.validated_data.get('otp').user).delete()
#         return 
    