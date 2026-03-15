from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from courses.models import Course
from lessons.models import Lesson
from lessons.serializers import LessonSerializer


class CourseSerializer(ModelSerializer):
    """Сериализатор по курсам"""

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    """Сериализатор c предоставлением информации по урокам их количеству в курсе"""

    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lessons_count(self, course):
        """функция возвращает количество уроков по курсу"""
        return Lesson.objects.filter(course=course.pk).count()

    class Meta:
        model = Course
        fields = ("id", "name", "description", "lessons_count", "lessons")
