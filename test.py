import unittest

from app import app


class FlaskTest(unittest.TestCase):

    def test_get_students(self):
        tester = app.test_client(self)
        response = tester.get('/students')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    #  Will fail after adding the user, in order to succeed again need to change params
    def test_add_student(self):
        tester = app.test_client(self)
        response = tester.post('/students', json={'first_name': 'Mo', 'last_name': 'Ka', 'email': 'aqcxz@g.com'})
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_get_student(self):
        tester = app.test_client(self)
        response = tester.get('/students/1@g.com')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_update_student(self):
        tester = app.test_client(self)
        response = tester.get('/students/1@g.com', json={'first_name': 'zar'})
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_update_student_fails_on_missing_params(self):
        tester = app.test_client(self)
        response = tester.get('/students/1@g.com')
        status_code = response.status_code
        self.assertEqual(status_code, 400)


if __name__ == "__main__":
    unittest.main()