from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Course, Faculty, Block, Classroom, Student
import logging

logger = logging.getLogger(__name__)
def dashboard(request):
    try:
        courses = Course.objects.select_related('faculty', 'classroom', 'classroom__block').all()
        faculty = Faculty.objects.prefetch_related('course_set').all()
        blocks = Block.objects.all()
        classrooms = Classroom.objects.all()
        students = Student.objects.all()
        try:
            total_capacity = sum(c.classroom.capacity for c in courses if c.classroom)
            total_enrolled = sum(c.enrolled_count() for c in courses)
            avg_utilization = (total_enrolled / total_capacity * 100) if total_capacity > 0 else 0
        except Exception as e:
            logger.warning(f"Error calculating capacity statistics: {e}")
            total_capacity = 0
            total_enrolled = 0
            avg_utilization = 0
        try:
            total_credits = sum(f.total_workload() for f in faculty)
            avg_workload = (total_credits / len(faculty)) if faculty else 0
        except Exception as e:
            logger.warning(f"Error calculating workload statistics: {e}")
            total_credits = 0
            avg_workload = 0
        context = {
            'courses': courses,
            'faculty': faculty,
            'blocks': blocks,
            'classrooms': classrooms,
            'students': students,
            'summary_stats': {
                'total_capacity': total_capacity,
                'total_enrolled': total_enrolled,
                'avg_utilization': round(avg_utilization, 1),
                'total_credits': total_credits,
                'avg_workload': round(avg_workload, 1),
            }
        }
        return render(request, 'dashboard.html', context)
    except Exception as e:
        logger.error(f"Error in dashboard view: {e}")
        return render(request, 'dashboard.html', {
            'courses': Course.objects.none(),
            'faculty': Faculty.objects.none(),
            'blocks': Block.objects.none(),
            'classrooms': Classroom.objects.none(),
            'students': Student.objects.none(),
            'summary_stats': {
                'total_capacity': 0,
                'total_enrolled': 0,
                'avg_utilization': 0,
                'total_credits': 0,
                'avg_workload': 0,
            },
            'error_message': 'Unable to load dashboard data. Please try again later.'
        })
