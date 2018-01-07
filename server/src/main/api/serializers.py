from rest_framework import serializers

from ..models import (Workshop, Project, Event, Timeline, Member, Organiser, WorkshopPlan, WorkshopFaqs)


class WorkshopModelSerializer(serializers.ModelSerializer):
    """
    docstring here
        :param serializers.ModelSerializer: 
    """
    class Meta: 
        model = Workshop
        fields = [
            'id',
            'name',
            'venue',
            'logo_url',
            'background_url',
            'short_description',
            'description',
            'reg_start_date',
            'reg_end_date',
            'start_date',
            'end_date',
            'reg_status',
            'status',
            'theme_color'
            ]


class EventModelSerializer(serializers.ModelSerializer):
    """
    docstring here
        :param serializers.ModelSerializer: 
    """
    
    class Meta:
        model = Event
        fields = [
            'id',
            'name',
            'short_description',
            'description',
            'date',
            'status',
            'img',
            'logo',
            'offical_link',
            'theme_color'
            ]


class ProjectModelSerializer(serializers.ModelSerializer):
    """
    docstring here
        :param serializers.ModelSerializer: 
    """
    
    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'tech',
            'details',
            'img',
            'workshop'
        ]


class TimelineModelSerializer(serializers.ModelSerializer):
    """
    docstring here
        :param serializers.ModelSerializer: 
    """
    
    class Meta:
        model = Timeline
        fields = [
            'id',
            'date',
            'venue',
            'event',
            'achievement'
        ]


class MemberModelSerializer(serializers.ModelSerializer):
    """
    docstring here
    :param serializers.ModelSerializer: 
    """
    class Meta:
        model = Member
        fields = [
            'id',
            'name',
            'student_no',
            'year',
            'branch',
            'img',
            'category',
            'contact',
            'department',
            'fb_id',
            'gender'
        ]


class OrganiserModelSerializer(serializers.ModelSerializer):
    """
    docstring here
    :param serializers.ModelSerializer: 
    """
    class Meta:
        model = Organiser
        fields = [
            'id',
            'workshop',
            'member_id'
        ]

class WorkshopPlanModelSerializer(serializers.ModelSerializer):
    """
    docstring here
    :param serializers.ModelSerializer: 
    """
    class Meta:
        model = WorkshopPlan
        fields = [
            'id',
            'workshop',
            'team_limit',
            'details',
            'title',
            'price',
        ]

class WorkshopFaqsModelSerializer(serializers.ModelSerializer):
    """
    docstring here
    :param serializers.ModelSerializer: 
    """
    class Meta:
        model = WorkshopFaqs
        fields = [
            'id',
            'workshop',
            'question',
            'answer',
        ]