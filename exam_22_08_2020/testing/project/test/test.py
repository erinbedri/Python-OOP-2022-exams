import unittest

from project.student_report_card import StudentReportCard


class StudentReportCardTest(unittest.TestCase):
    STUDENT_NAME = "Test Name"
    SECOND_STUDENT_NAME = "Second Test Name"
    SCHOOL_YEAR = 10
    SECOND_SCHOOL_YEAR = 5
    SUBJECT = "Math"
    SECOND_SUBJECT = "History"
    GRADE = 5.00
    SECOND_GRADE = 6.00

    def setUp(self) -> None:
        self.student_report_card = StudentReportCard(self.STUDENT_NAME, self.SCHOOL_YEAR)

    def test_init__when_valid__expect_initialization(self):
        self.assertEqual(self.STUDENT_NAME, self.student_report_card.student_name)
        self.assertEqual(self.SCHOOL_YEAR, self.student_report_card.school_year)
        self.assertEqual({}, self.student_report_card.grades_by_subject)

    def test_name_setter__when_name_is_empty__expect_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.student_report_card.student_name = ""
        self.assertEqual("Student Name cannot be an empty string!", str(context.exception))
        self.assertEqual(self.STUDENT_NAME, self.student_report_card.student_name)

    def test_name_setter__when_name_is_valid__expect_value_error(self):
        self.student_report_card.student_name = self.SECOND_STUDENT_NAME
        self.assertEqual(self.SECOND_STUDENT_NAME, self.student_report_card.student_name)

    def test_year_setter__when_value_less_than_one__expect_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.student_report_card.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(context.exception))
        self.assertEqual(self.SCHOOL_YEAR, self.student_report_card.school_year)

    def test_year_setter__when_value_bigger_than_12__expect_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.student_report_card.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(context.exception))
        self.assertEqual(self.SCHOOL_YEAR, self.student_report_card.school_year)

    def test_year_setter__when_value_valid(self):
        self.student_report_card.school_year = self.SECOND_SCHOOL_YEAR
        self.assertEqual(self.SECOND_SCHOOL_YEAR, self.student_report_card.school_year)

    def test_add_grade__when_subject_not_in_grades_by_subject(self):
        self.student_report_card.add_grade(self.SUBJECT, self.GRADE)
        self.assertEqual([self.GRADE], self.student_report_card.grades_by_subject[self.SUBJECT])

    def test_add_grade__when_subject_in_grades_by_subject(self):
        self.student_report_card.grades_by_subject[self.SUBJECT] = [self.GRADE]

        self.student_report_card.add_grade(self.SUBJECT, self.GRADE)
        self.assertEqual([self.GRADE, self.GRADE], self.student_report_card.grades_by_subject[self.SUBJECT])

    def test_average_grade_by_subject__when_no_grades(self):
        expected = ""
        result = self.student_report_card.average_grade_by_subject()
        self.assertEqual(expected, result)

    def test_average_grade_by_subject__when_one_subject_with_grades(self):
        self.student_report_card.grades_by_subject[self.SUBJECT] = [self.GRADE, self.SECOND_GRADE]
        expected = f"Math: {sum([self.GRADE, self.SECOND_GRADE]) / len([self.GRADE, self.SECOND_GRADE]):.2f}"
        result = self.student_report_card.average_grade_by_subject()
        self.assertEqual(expected, result)

    def test_average_grade_by_subject__when_two_subject_with_grades(self):
        self.student_report_card.grades_by_subject[self.SUBJECT] = [self.GRADE, self.SECOND_GRADE]
        self.student_report_card.grades_by_subject[self.SECOND_SUBJECT] = [self.GRADE]
        expected = f"Math: {sum([self.GRADE, self.SECOND_GRADE]) / len([self.GRADE, self.SECOND_GRADE]):.2f}\n" \
                   f"History: {self.GRADE:.2f}"
        result = self.student_report_card.average_grade_by_subject()
        self.assertEqual(expected, result)

    def test_average_grade_for_all_subjects__when_no_subject__expect_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError) as context:
            self.student_report_card.average_grade_for_all_subjects()
        self.assertEqual("division by zero", str(context.exception))

    def test_average_grade_for_all_subjects__when_one_subject(self):
        self.student_report_card.grades_by_subject[self.SUBJECT] = [self.GRADE, self.SECOND_GRADE]
        expected = f"Average Grade: {sum([self.GRADE, self.SECOND_GRADE]) / len([self.GRADE, self.SECOND_GRADE]):.2f}"
        result = self.student_report_card.average_grade_for_all_subjects()
        self.assertEqual(expected, result)

    def test_average_grade_for_all_subjects__when_two_subject(self):
        self.student_report_card.grades_by_subject[self.SUBJECT] = [self.GRADE, self.SECOND_GRADE]
        self.student_report_card.grades_by_subject[self.SECOND_SUBJECT] = [self.GRADE]
        expected = f"Average Grade: " \
                   f"{sum([self.GRADE, self.SECOND_GRADE, self.GRADE]) / len([self.GRADE, self.SECOND_GRADE, self.GRADE]):.2f}"
        result = self.student_report_card.average_grade_for_all_subjects()
        self.assertEqual(expected, result)

    def test_repr__when_no_subject__expect_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError) as context:
            repr(self.student_report_card)
        self.assertEqual("division by zero", str(context.exception))

    def test_repr__when_one_subject(self):
        self.student_report_card.grades_by_subject[self.SUBJECT] = [self.GRADE, self.SECOND_GRADE]
        expected = f"Name: {self.STUDENT_NAME}\n" \
                   f"Year: {self.SCHOOL_YEAR}\n" \
                   f"----------\n" \
                   f"{self.SUBJECT}: {sum([self.GRADE, self.SECOND_GRADE]) / len([self.GRADE, self.SECOND_GRADE]):.2f}\n" \
                   f"----------\n" \
                   f"Average Grade: {sum([self.GRADE, self.SECOND_GRADE]) / len([self.GRADE, self.SECOND_GRADE]):.2f}"
        result = repr(self.student_report_card)
        self.assertEqual(expected, result)

    def test_repr__when_two_subject(self):
        self.student_report_card.grades_by_subject[self.SUBJECT] = [self.GRADE, self.SECOND_GRADE]
        self.student_report_card.grades_by_subject[self.SECOND_SUBJECT] = [self.GRADE]
        expected = f"Name: {self.STUDENT_NAME}\n" \
                   f"Year: {self.SCHOOL_YEAR}\n" \
                   f"----------\n" \
                   f"{self.SUBJECT}: {sum([self.GRADE, self.SECOND_GRADE]) / len([self.GRADE, self.SECOND_GRADE]):.2f}\n" \
                   f"{self.SECOND_SUBJECT}: {self.GRADE:.2f}\n" \
                   f"----------\n" \
                   f"Average Grade: {sum([self.GRADE, self.SECOND_GRADE, self.GRADE]) / len([self.GRADE, self.SECOND_GRADE, self.GRADE]):.2f}"
        result = repr(self.student_report_card)
        self.assertEqual(expected, result)