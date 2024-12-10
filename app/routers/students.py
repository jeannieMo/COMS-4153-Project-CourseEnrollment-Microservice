from fastapi import APIRouter, HTTPException, Header
from app.services.courseworks_api import CourseWorksAPI
import uuid
"""
    Router in charge of connecting with `courseworks_api.py` to get the courses a student is enrolled in.
"""
router = APIRouter()


# Fetch courses for a student by student_id (uni)
@router.get("/users/{student_id}/courses", tags=["students"])
async def get_student_courses(student_id: str, token: str = Header(...)):
    correlation_id = request.headers.get("X-Correlation-ID", str(uuid.uuid4()))
    print(f"Correlation ID: {correlation_id} - Fetching students for course: {course_code}")
    api = CourseWorksAPI(token)
    try:
        courses = api.get_student_courses(student_id)
        return {"student_id": student_id, "courses": courses}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error fetching courses for student {student_id}: {str(e)}")

