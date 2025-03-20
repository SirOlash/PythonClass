from models.user import User
from services.course_manager import CourseManager


class Facilitator(User):
    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email, password)
        self.created_courses = []

    def create_course(self, course_name):
        from models.courses import Course

        for course in self.created_courses:
            if course.course_name.lower().strip() == course_name.lower().strip():
                raise Exception('Course already exists')

        new_course = Course(course_name, self)
        self.created_courses.append(new_course)
        CourseManager.add_course(new_course)
        return new_course

    def view_registered_students(self):
        if not self.created_courses:
            return "You haven't created any courses"
        result_lines = []
        for course in self.created_courses:
            result_lines.append(f"Course: {course.course_name}")
            if not course.registrations:
                result_lines.append("  No students registered.")
            else:
                for registration in course.registrations:
                    student = registration.student
                    result_lines.append(
                        f"  Student: {student.first_name} {student.last_name} - Grade: {registration.get_grade()}")
        return "\n".join(result_lines)


    def assign_grade(self,course_name: str, student_email: str, score: float):
        selected_course = None
        for course in self.created_courses:
            if course.course_name.lower().strip() == course_name.lower().strip():
                selected_course = course
                break

        if selected_course is None:
            raise Exception("Course not found")

        selected_registration = None
        for registration in selected_course.registrations:
            if registration.student.email.lower().strip() == student_email.lower().strip():
                selected_registration = registration
                break

        if selected_registration is None:
            raise Exception("Student not registered in this course")

        selected_registration.set_grade(score)
        return selected_registration

