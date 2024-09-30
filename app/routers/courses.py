from fastapi import APIRouter
from app.services.courseworks_api import CourseWorksAPI
"""
    Router in charge of connecting with `courseworks_api.py` to get the students enrolled in a class
"""
router = APIRouter()


# Fetch students enrolled in a course by course code (e.g., COMSW4153)
@router.get("/course/{course_code}/students", tags=["courses"])
async def get_course_students(course_code: str):
    api = CourseWorksAPI()
    students = api.get_course_students_by_code(course_code)
    return {"course_code": course_code, "students": students}
