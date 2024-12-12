from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import students, courses

"""
    Group Project for Cloud Computing Course!!
    
    Entrypoint to the Course Enrollment interface! 
    For examples on what you can do with this, try running this `main.py` then go to your browser and do:
    
    See the list of classmates in COMSW4153 and their IDs:
        http://127.0.0.1:8000/course/COMSW4153/students`
    
    See the list of students a course has this semester:
        curl -X GET "http://localhost:8000/course/<course id until the first '_'>/students" -H "token: 1396~yFrVF9nYzKV6YyrAtaZccFcLATt84zMcLJehYX7Y26z7RGuCnuAmGQQmCJtN8H6C"
        
    The output is JSON.
"""

app = FastAPI()

# Enable CORS for development purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Your React app's URL
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
    expose_headers=["*"]
)

# Include the routes from the students and courses routers
app.include_router(students.router)
app.include_router(courses.router)

@app.get("/")
async def root():
    return {"message": "Course Enrollment Microservice is Running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
