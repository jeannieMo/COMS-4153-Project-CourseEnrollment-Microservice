from typing import Any
from framework.resources.base_resource import BaseResource
from app.models.course import CourseSection
from app.services.service_factory import ServiceFactory


class CourseResource(BaseResource):
    def __init__(self, config):
        super().__init__(config)
        self.data_service = ServiceFactory.get_service("CourseResourceDataService")
        self.database = "CloudComputing_CE"

    def create_or_update_student(self, profile: dict):
        """Create or update a student profile with new fields."""
        self.data_service.insert_or_update(
            table="students",
            data=profile,
            key_field="student_id"
        )

    def create_or_update_course(self, course: dict):
        """Create or update a course record with new fields."""
        self.data_service.insert_or_update(
            table="courses",
            data=course,
            key_field="course_code"
        )

    def get_courses(self, student_id: str):
        """Retrieve all courses a student is enrolled in from the database."""
        # Query to join enrollments and courses tables to get the courses for a specific student
        return self.data_service.get_courses_for_student(student_id)

    def get_students(self, course_code: str):
        """Retrieve all students enrolled in a specific course from the database."""
        # Query to join enrollments and students tables to get the students for a specific course
        return self.data_service.get_students_in_course(course_code)
