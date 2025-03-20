from models.facilitator import Facilitator
from models.student import Student
from models.user import User

class Registration:
    STUDENT_REGISTRY = []
    FACILITATOR_REGISTRY = []

    @classmethod
    def register_facilitator(cls,first_name, last_name, email, password):
        new_facilitator = Facilitator(first_name, last_name, email, password)
        cls.FACILITATOR_REGISTRY.append(new_facilitator)
        return new_facilitator

    @classmethod
    def register_student(cls,first_name, last_name, email, password):
        new_student = Student(first_name, last_name, email, password)
        cls.STUDENT_REGISTRY.append(new_student)
        return new_student

    @classmethod
    def login_student(cls,email, password):
        for student in cls.STUDENT_REGISTRY:
            if student.email == email and student.verify_password(password):
                return student
        raise Exception("Invalid email or password")

    @classmethod
    def login_facilitator(cls, email, password):
        for facilitator in cls.FACILITATOR_REGISTRY:
            if facilitator.email == email and facilitator.verify_password(password):
                return facilitator
        raise Exception("Invalid email or password")

