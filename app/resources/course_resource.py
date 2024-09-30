from typing import Any
from framework.resources.base_resource import BaseResource
from app.models.course import CourseSection
from app.services.service_factory import ServiceFactory

"""
    Currently not in use because we are just focusing on the API aspect of feeding the user their dashboard + the 
    students in their class, not the database.
"""


class CourseResource(BaseResource):

    def __init__(self, config):
        super().__init__(config)

        # TODO -- Replace with dependency injection.
        #
        self.data_service = ServiceFactory.get_service("CourseResourceDataService")
        self.database = "CloudComputing_CE"
        #self.collection = "course_sections"
        #self.key_field="sis_course_id"

    def get_by_key(self, key: str) -> CourseSection:

        d_service = self.data_service

        result = d_service.get_data_object(
            self.database, self.collection, key_field=self.key_field, key_value=key
        )

        result = CourseSection(**result)
        return result