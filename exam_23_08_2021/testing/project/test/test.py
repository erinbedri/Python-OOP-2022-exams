import unittest

from project.library import Library


class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.library = Library("Test")

    def test_init(self):
        self.assertEqual("Test", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_setter__when_empty_string__expect_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.library.name = ""
        self.assertEqual("Name cannot be empty string!", str(context.exception))

    def test_name_setter__when_valid(self):
        self.library.name = "new name"
        self.assertEqual("new name", self.library.name)

    def test_add_book__when_author_not_in_dict__expect_empty_dict(self):
        self.library.add_book("Vazov", "Pod igoto")
        self.assertEqual({"Vazov": ["Pod igoto"]}, self.library.books_by_authors)

    def test_add_book__when_title_not_in_dict__expect_empty_dict(self):
        self.library.books_by_authors["Vazov"] = ["Pod igoto"]
        self.library.add_book("Vazov", "Pod igoto 2")
        self.assertEqual({"Vazov": ["Pod igoto", "Pod igoto 2"]}, self.library.books_by_authors)

    def test_add_reader__when_reader_not_in_dict(self):
        self.library.add_reader("Erin")
        self.assertEqual({"Erin": []}, self.library.readers)

    def test_add_reader__when_reader_in_dict(self):
        self.library.readers["Erin"] = []
        result = self.library.add_reader("Erin")
        self.assertEqual(f"Erin is already registered in the Test library.", result)

    def test_rent_book__when_reader_not_in_readers(self):
        result = self.library.rent_book("Bedri", "Botev", "Stihotvoreniq")
        self.assertEqual(f"Bedri is not registered in the Test Library.", result)

    def test_rent_book__when_author_not_in_authors(self):
        self.library.readers["Bedri"] = []
        result = self.library.rent_book("Bedri", "Botev", "Stihotvoreniq")
        self.assertEqual(f"Test Library does not have any Botev's books.", result)

    def test_rent_book__when_book_not_in_books(self):
        self.library.readers["Bedri"] = []
        self.library.books_by_authors["Botev"] = []
        result = self.library.rent_book("Bedri", "Botev", "Stihotvoreniq")
        self.assertEqual(f"""Test Library does not have Botev's "Stihotvoreniq".""", result)

    def test_rent_book__when_valid(self):
        self.library.readers["Bedri"] = []
        self.library.books_by_authors["Botev"] = ["Stihotvoreniq"]
        self.library.rent_book("Bedri", "Botev", "Stihotvoreniq")

        self.assertEqual({"Bedri": [{"Botev": "Stihotvoreniq"}]}, self.library.readers)
        self.assertEqual({"Botev": []}, self.library.books_by_authors)

