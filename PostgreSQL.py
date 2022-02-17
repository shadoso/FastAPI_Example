import psycopg2
from models import Role, Courses

# PostgreSQL access
HOST_NAME = 'localhost'
DATABASE_NAME = 'College'
DATABASE_USER = 'postgres'
DATABASE_PASSWORD = 'shadobot'
PORT_ID = 5432

# PostgreSQL commands
UPDATE_USER_SALARY = 'UPDATE users SET salary = '
WHERE_USER_UID = ' WHERE user_uid = '
UPDATE_USER_MONTHLY_PAYMENT = 'UPDATE users SET monthly_payment = '
CREATE_USER = 'INSERT INTO users ' \
              '(user_uid, name, gender, role, course, salary, monthly_payment, scholarship, disabilities) ' \
              'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'

# Warning messages
MSG_LENGTH_LIMIT = "The name cannot be bigger than 56 digits or smaller than 6"
MSG_STUDENT_COURSES = "Students must have only 1 course."
MSG_GUEST_COURSES = "Guests are not allowed to have a course."
MSG_MAX_COURSES = "You are not allowed to have more than 3 courses."

# Monthly Payments
PAYMENT = {
    Courses.cs: 1175.00,
    Courses.ds: 1175.50,
    Courses.anth: 1065.00,
    Courses.bioeng: 1245.00,
    Courses.ling: 975.00,
    Courses.psyc: 1036.00
}

# Constants
SALARY = 3638.50
MAX_NAME_LENGTH = 56
MIN_NAME_LENGTH = 6
MIN_COURSE_AMOUNT = 1
MAX_COURSE_AMOUNT = 3
NO_COURSE = 0

INVALID = "User structures doesn't match with rules "


class DataBase:
    def __init__(self,
                 user_uid=None, name=None, gender=None, role=None, course=None, salary=None, monthly_payment=None,
                 scholarship=None, disabilities=None
                 ):

        # User data
        self.__user_uid = user_uid
        self._name = name
        self._gender = gender
        self._role = role
        self._course = course
        self._salary = salary
        self._monthly_payment = monthly_payment
        self._scholarship = scholarship
        self._disabilities = disabilities

        # Database name = varchar(56)
        assert MAX_NAME_LENGTH >= len(self._name) >= MIN_NAME_LENGTH, MSG_LENGTH_LIMIT

        # DB connection
        self.conn = psycopg2.connect(
            host=HOST_NAME, dbname=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASSWORD, port=PORT_ID
        )
        self.cur = self.conn.cursor()

    def close_db(self):
        """
        :return: Close the database query
        """
        self.cur.close()
        self.conn.close()

    def salary(self):
        if self._role == Role.teacher or self._role == Role.coordinator:
            self._salary = None

            if MAX_COURSE_AMOUNT <= len(self._course) >= MIN_COURSE_AMOUNT:
                self._salary = len(self._course) * SALARY

    def monthly_payment(self):
        if self._role == Role.student and self._scholarship is not None:
            self._monthly_payment = PAYMENT[self._course] - (PAYMENT[self._course] * self._scholarship)

    def validate_user(self):
        if self._role == Role.admin:
            return True

        if self._role == Role.teacher or Role.coordinator:
            if NO_COURSE <= len(self._course) <= MAX_COURSE_AMOUNT:
                return True

        if self._role == Role.student and len(self._course) == MIN_COURSE_AMOUNT:
            return True

        if self._role == Role.guest and self._course is None:
            return True

        else:
            return False

    def register_user(self):
        """
        :return: Append user to database
        """
        if self.validate_user():
            self.salary()
            self.monthly_payment()

            values = [
                str(self.__user_uid),  # Converting UUID to str might not be the best solution
                self._name,
                self._gender,
                self._role,
                self._course,
                self._salary,
                self._monthly_payment,
                self._scholarship,
                self._disabilities
            ]

            self.cur.execute(CREATE_USER, values)
            self.conn.commit()
            return True

        else:
            raise INVALID
