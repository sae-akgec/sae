from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .permission import IsAdminOrReadOnly, IsSuperuserOrWriteOnly, IsUserEnrolled
from django.contrib.auth.models import User
from ..models import (Workshop, Project, Member, Timeline, Organiser, Event,
 WorkshopFaqs, WorkshopPlan, EventTeam, ProjectMaterial, PreWorkshopMaterial, WorkshopEnrollment, UserProfile)
from .serializers import ( WorkshopModelSerializer, ProjectModelSerializer,
                            MemberModelSerializer, TimelineModelSerializer,OrganiserModelSerializer,EventModelSerializer,
                             WorkshopFaqsModelSerializer, WorkshopPlanModelSerializer, EventTeamModelSerializer,
                             UserRegisterSerializer,UserLoginSerializer, ProjectMaterialModelSerializer,  PreWorkshopMaterialModelSerializer,
                             WorkshopEnrollmentModelSerializer, UserProfileModelSerializer, UserModelSerializer)

from .token import account_activation_token
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.http import HttpResponse
from django.views import View



class WorkshopListAPIView(APIView):
    """
    docstring here
        :param APIView: 
    """
    serializer_class = WorkshopModelSerializer
    permission_classes = (IsAdminOrReadOnly,permissions.IsAuthenticatedOrReadOnly)
    def get(self, request):
        workshops = Workshop.objects.all()
        serializer = WorkshopModelSerializer(workshops, many=True)
        return Response({"workshops":serializer.data})

    def post(self, request):
        serializer = WorkshopModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkshopDetailAPIView(APIView):
    """
    docstring here
    :param APIView: 
    """
    permission_classes = (permissions.AllowAny,)
    def get_workshop(self, workshop_name):
        try:
            return Workshop.objects.get(name=workshop_name)
        except Workshop.DoesNotExist:
            raise Http404
    
    def get_projects(self, workshop_id):
        try:
            return Project.objects.filter(workshop=workshop_id)
        except Project.DoesNotExist:
            raise Http404

    def get_organisers(self, workshop_id):
        try:
            return Organiser.objects.filter(workshop=workshop_id)
        except Organiser.DoesNotExist:
            raise Http404

    def get_member(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get_plans(self, workshop_id):
        try:
            return WorkshopPlan.objects.filter(workshop=workshop_id)
        except Organiser.DoesNotExist:
            raise Http404

    def get_faqs(self, workshop_id):
        try:
            return WorkshopFaqs.objects.filter(workshop=workshop_id)
        except Organiser.DoesNotExist:
            raise Http404

    def get(self, request, name):
        workshop = self.get_workshop(name)
        workshop_serializer = WorkshopModelSerializer(workshop)
        workshop_id = workshop_serializer.data['id']
        projects = self.get_projects(workshop_id)
        projects_serializer = ProjectModelSerializer(projects, many=True)
        organisers = self.get_organisers(workshop_id)
        organisers_serializer = OrganiserModelSerializer(organisers, many=True)
        plans = self.get_plans(workshop_id)
        plans_serializer = WorkshopPlanModelSerializer(plans, many=True)
        faqs = self.get_faqs(workshop_id)
        faqs_serializer = WorkshopFaqsModelSerializer(faqs, many=True)

        members = []
        # Fetching team member details on basis of orgnaiser
        for organiser in organisers_serializer.data:
            member_id = organiser['member_id']
            member = self.get_member(member_id)
            member_serializer = MemberModelSerializer(member)
            members.append(member_serializer.data)
        
        workshop_response = workshop_serializer.data
        workshop_response.update({"projects":projects_serializer.data})
        workshop_response.update({"organisers":members})
        workshop_response.update({"plans":plans_serializer.data})
        workshop_response.update({"faqs":faqs_serializer.data})
        
        return Response(workshop_response)


class EventListAPIView(APIView):
    """
    docstring here
        :param APIView: 
    """
    
    serializer_class = EventModelSerializer
    permission_classes = (IsAdminOrReadOnly,permissions.IsAuthenticatedOrReadOnly,)
    def get(self, request):
        events = Event.objects.all()
        serializer = EventModelSerializer(events, many=True)
        return Response({"events":serializer.data})

    def post(self, request):
        serializer=EventModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetailAPIView(APIView):
    """
    docstring here
    :param APIView: 
    """
    permission_classes = (permissions.AllowAny,)
    def get_event(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404
    
    def get_timeline(self, event_id):
        try:
            return Timeline.objects.filter(event=event_id)
        except Timeline.DoesNotExist:
            raise Http404

    def get_team(self, event_id):
        try:
            return EventTeam.objects.filter(event=event_id)
        except EventTeam.DoesNotExist:
            raise Http404

    def get_member(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        event = self.get_event(pk)
        event_serializer = EventModelSerializer(event)
        event_id = event_serializer.data['id']
        timeline = self.get_timeline(event_id)
        timeline_serializer = TimelineModelSerializer(timeline, many=True)
        team = self.get_team(event_id)
        team_serializer = EventTeamModelSerializer(team, many=True)

        members = []
        # Fetching team member details on basis of orgnaiser
        for team_member in team_serializer.data:
            member_id = team_member['member_id']
            member = self.get_member(member_id)
            member_serializer = MemberModelSerializer(member)
            members.append(member_serializer.data)
        
        timeline_response = event_serializer.data
        timeline_response.update({"timeline":timeline_serializer.data})
        timeline_response.update({"team":members})
        return Response(timeline_response)


class MemberListAPIView(APIView):
    """
    docstring here
        :param APIView: 
    """
    
    serializer_class = MemberModelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsAdminOrReadOnly)
    def get(self, request):
        members = Member.objects.all()
        serializer = MemberModelSerializer(members, many=True)
        return Response({"members":serializer.data})

    def post(self, request):
        serializer = MemberModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegisterAPIView(APIView):
    """
    docstring here
        :param APIView: 
    """
    serializer_class = UserRegisterSerializer
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
    """
    docstring here
        :param APIView: 
    """
    serializer_class = UserLoginSerializer
    permission_classes = (IsSuperuserOrWriteOnly,)
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        users = User.objects.all()
        serializer = UserRegisterSerializer(users, many=True)
        return Response({"user":serializer.data})

class UserEmailVerificationView(View):
            
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse("Thank you for your email confirmation. Now you can login your account.")
        return HttpResponse("Activation link is invalid!")

# User View Goes here

class ClassRoomView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get_workshop(self, pk):
        try:
            return Workshop.objects.get(pk=pk)
        except Workshop.DoesNotExist:
            raise Http404

    def get_enrollment(self,user_id):
        try:
            return WorkshopEnrollment.objects.filter(user_id=user_id, enroll_status=True)
        except EventTeam.DoesNotExist:
            raise Http404
    def get(self,request):
        user = User.objects.get(username=request.user.username)
        user_serializer = UserModelSerializer(user)
        user_id =  user_serializer.data['id']

        #Getting  Workshop in which user is enrolled 
        enrollments = self.get_enrollment(user_id)
        enrollments_serializer = WorkshopEnrollmentModelSerializer(enrollments, many=True)
        workshops = []
        for enrollment in enrollments_serializer.data:
            workshop = self.get_workshop(enrollment['workshop_id'])
            workshop_serializer = WorkshopModelSerializer(workshop)
            workshops.append(workshop_serializer.data)

        classroom_response ={}
        classroom_response.update({"enrollments":enrollments_serializer.data})
        classroom_response.update({"workshops":workshops}) 
        return Response(classroom_response)


class ClassCourseView(APIView):

    permission_classes = (permissions.IsAuthenticated,IsUserEnrolled,)
    def get_workshop(self, pk):
        try:
            return Workshop.objects.get(pk=pk)
        except Workshop.DoesNotExist:
            raise Http404
    def get_projects(self, workshop_id):
        try:
            return Project.objects.filter(workshop=workshop_id)
        except Project.DoesNotExist:
            raise Http404
    def get_project_material(self, project):
        try:
            return ProjectMaterial.objects.filter(project=project)
        except ProjectMaterial.DoesNotExist:
            raise Http404
            
    def get_pre_workshop_material(self, workshopid):
        try:
            return PreWorkshopMaterial.objects.filter(workshop=workshopid)
        except PreWorkshopMaterial.DoesNotExist:
            raise Http404

    def get(self,request,workshopid):
        workshop = self.get_workshop(workshopid)
        workshop_serializer = WorkshopModelSerializer(workshop)
        pre_material = self.get_pre_workshop_material(workshopid)
        pre_material_serializer = PreWorkshopMaterialModelSerializer(pre_material,many=True)
        projects = self.get_projects(workshopid)
        projects_serializer = ProjectModelSerializer(projects, many=True)


        # Give projects with material emmbeded in them
        projects_response = []
        for project in projects_serializer.data:
            project_materials = self.get_project_material(project['id'])
            material_serializer = ProjectMaterialModelSerializer(project_materials, many=True)
            project['materials'] = material_serializer.data
            projects_response.append(project)

        course_response = {}
        course_response.update(workshop_serializer.data)
        course_response.update({"pre_material": pre_material_serializer.data})
        course_response.update({"projects":projects_response})
        return Response(course_response)
        
        


