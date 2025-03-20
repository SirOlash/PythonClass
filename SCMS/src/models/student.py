from models.user import User
from services.course_manager import CourseManager


class Student(User):
    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email, password)
        self.registered_courses = []

    @staticmethod
    def view_available_courses():
        courses = CourseManager.get_all_courses()
        if not courses:
            return "No courses available yet!! Chill"

        course_list = []
        for course in courses:
            course_description = (f"{course.course_name} (Facilitator: "
                                  f"{course.facilitator.first_name} {course.facilitator.last_name})")

            course_list.append(course_description)

        result = "\n".join(course_list)
        return result

    def register_for_course(self, course_name: str):
        from models.course_registration import CourseRegistration

        available_courses = CourseManager.get_all_courses()
        selected_course = None
        for course in available_courses:
            if course.course_name.lower().strip() == course_name.lower().strip():
                selected_course = course
                break

        if selected_course is None:
            raise Exception("Course not found among available courses.")

        for registration in self.registered_courses:
            if registration.course.course_name.lower().strip() == course_name.lower().strip():
                raise Exception("Student has already registered for this course.")

        new_registration = CourseRegistration(selected_course, self)
        self.registered_courses.append(new_registration)

        selected_course.registrations.append(new_registration)
        return new_registration

    def view_registered_courses(self):
        if len(self.registered_courses) == 0:
            return "No courses registered yet!! Go and register"

        result_lines = []
        for registration in self.registered_courses:
            course = registration.course
            description = (f"{course.course_name} (Facilitator: "
                           f"{course.facilitator.first_name} {course.facilitator.last_name}) "
                           f"- Grade: {registration.get_grade()}")

            result_lines.append(description)
            return "\n".join(result_lines)



