from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import students, courses

"""
    Entrypoint to the Course Enrollment interface! 
    For examples on what you can do with this, try running this `main.py` then go to your browser and do:
    
    See the list of classmates in COMSW4153 and their IDs:
        http://127.0.0.1:8000/course/COMSW4153/students`
    
    See the list of courses Jeannie is in (has been in since Freshman year, i'll figrue out how to do it by term later):
        http://127.0.0.1:8000/users/jam2492/courses
        
    The output is JSON.
"""

app = FastAPI()

# Enable CORS for development purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for simplicity during development
    allow_methods=["*"],
    allow_headers=["*"],
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
