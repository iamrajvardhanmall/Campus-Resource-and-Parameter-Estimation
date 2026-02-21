from django.db import models

class Block(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Classroom(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=20)
    capacity = models.IntegerField()
    def __str__(self):
        return f"{self.block.name} - {self.room_number}"
    @property
    def name(self):
        return self.room_number
    def capacity_utilization(self):
        if self.capacity == 0:
            return 0
        total_enrolled = 0
        for course in self.course_set.all():
            total_enrolled += course.student_set.count()
        utilization = (total_enrolled / self.capacity) * 100
        return min(utilization, 999)  
    def utilization_status(self):
        util = self.capacity_utilization()
        if util == 0:
            return "Empty"
        elif util <= 50:
            return "Under-utilized" 
        elif util <= 80:
            return "Well-utilized"
        elif util <= 100:
            return "Fully-utilized"
        else:
            return "Over-capacity"

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def total_workload(self):
        courses = self.course_set.all()
        return sum(course.credits for course in courses)
    def workload_status(self):
        total = self.total_workload()
        if total == 0:
            return "No Load"
        elif total <= 12:
            return "Light Load"
        elif total <= 18:
            return "Normal Load"
        elif total <= 24:
            return "Heavy Load"
        else:
            return "Overloaded"

class Course(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True)
    credits = models.IntegerField()
    def __str__(self):
        return self.name
    def capacity_utilization(self):
        enrolled = self.student_set.count()
        capacity = self.classroom.capacity if self.classroom else 0
        if capacity > 0:
            return (enrolled / capacity) * 100
        return 0
    
    def utilization_status(self):
        util = self.capacity_utilization()
        if util == 0:
            return "Empty"
        elif util <= 50:
            return "Under-utilized"
        elif util <= 80:
            return "Well-utilized"
        elif util <= 100:
            return "Fully-utilized"
        else:
            return "Over-capacity"
    
    def enrolled_count(self):
        return self.student_set.count()

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course)
    def __str__(self):
        return self.name
