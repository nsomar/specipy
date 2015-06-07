__author__ = 'omarsubhiabdelhafith'

import unittest
import os
from specipy.SpecParser import SpecParser
from specipy.SpecElements import BaseDecorator


class SpecipyTests(unittest.TestCase):

    def test_it_parses_simple_specs(self):
        with open(os.path.dirname(__file__) + "/test_data/Test1.m", "r") as file:
            self.file = file.read()
        pass

        parser = SpecParser(self.file)

        self.assertEqual(parser.spec_name, "SomeTest1Spec")
        self.assertEqual(parser.root.name, "SomeTest1Spec")
        self.assertEqual(len(parser.root.children), 1)

    def test_it_parses_a_context_in_a_describe(self):
        with open(os.path.dirname(__file__) + "/test_data/Test2.m", "r") as file:
            self.file = file.read()
        pass

        parser = SpecParser(self.file)

        self.assertEqual(parser.root.elements_description(), "Spec: SomeTest1Spec\n\n--------------------------------------------------\nDescribe: The first describe\n--------------------------------------------------\n\n    When: first context")
        self.assertEqual(parser.root.name, "SomeTest1Spec")
        self.assertEqual(len(parser.root.children), 1)

    def test_it_parses_a_context_with_2_it(self):
        with open(os.path.dirname(__file__) + "/test_data/Test3.m", "r") as file:
            self.file = file.read()
        pass

        parser = SpecParser(self.file)

        self.assertEqual(parser.spec_name, "SomeTest1Spec")
        self.assertEqual(parser.root.elements_description(), "Spec: SomeTest1Spec\n\nWhen: first context\n    It: has this test\n    It: and a second test")
        self.assertEqual(parser.root.name, "SomeTest1Spec")
        self.assertEqual(len(parser.root.children), 1)

    def test_it_parses_a_describe_with_a_context_with_2_it(self):
        with open(os.path.dirname(__file__) + "/test_data/Test4.m", "r") as file:
            self.file = file.read()
        pass

        parser = SpecParser(self.file)

        self.assertEqual(parser.spec_name, "SomeTest1Spec")
        self.assertEqual(parser.root.elements_description(), "Spec: SomeTest1Spec\n\n--------------------------------------------------\nDescribe: The first describe\n--------------------------------------------------\n\n    When: first context\n        It: has this test\n        It: and a second test")
        self.assertEqual(parser.root.name, "SomeTest1Spec")
        self.assertEqual(len(parser.root.children), 1)

    def test_it_parses_a_describe_with_2_context_with_2_it(self):
        with open(os.path.dirname(__file__) + "/test_data/Test5.m", "r") as file:
            self.file = file.read()
        pass

        parser = SpecParser(self.file)

        self.assertEqual(parser.spec_name, "SomeTest1Spec")
        self.assertEqual(parser.root.elements_description(), "Spec: SomeTest1Spec\n\n--------------------------------------------------\nDescribe: The first describe\n--------------------------------------------------\n\n    When: first context\n        It: has this test\n        It: and a second test\n\n    When: second context\n        It: has this othertest")
        self.assertEqual(parser.root.name, "SomeTest1Spec")
        self.assertEqual(len(parser.root.children), 1)

    def test_it_parses_complex_test(self):
        with open(os.path.dirname(__file__) + "/test_data/Test6.m", "r") as file:
            self.file = file.read()
        pass

        parser = SpecParser(self.file)

        self.assertEqual(parser.spec_name, "SomeTest1Spec")
        self.assertEqual(parser.root.elements_description(), "Spec: SomeTest1Spec\n\n--------------------------------------------------\nDescribe: The first describe\n--------------------------------------------------\n\n    When: first context\n        It: has this test\n        It: and a second test\n\n        When: inner context\n            It: has this an inner test\n            It: and a second inner test\n\n    When: second context\n        It: has this othertest\n\n--------------------------------------------------\nDescribe: The second describe\n--------------------------------------------------\n\n    When: second descibe context\n        It: has this other test\n        It: and another test")
        self.assertEqual(parser.root.name, "SomeTest1Spec")
        self.assertEqual(len(parser.root.children), 2)

    def test_it_can_change_element_decorations(self):
        with open(os.path.dirname(__file__) + "/test_data/Test1.m", "r") as file:
            self.file = file.read()
        pass

        class TestRootClass(BaseDecorator):

            def name_decoration(self, element_name):
                return "TEST:::: %s ::::" % element_name

        parser = SpecParser(self.file, root_class=TestRootClass)
        self.assertEqual(parser.parse().elements_description(), "TEST:::: SomeTest1Spec ::::\nIt: has this test")

    def test_it_ignores_single_line_comments(self):
        with open(os.path.dirname(__file__) + "/test_data/Test7.m", "r") as file:
            self.file = file.read()
        pass

        parser = SpecParser(self.file)
        self.assertEqual(parser.parse().elements_description(), "Spec: SomeTest1Spec\n\nWhen: first context\n    It: has this test")

    def test_it_ignores_multiline_comments(self):
        with open(os.path.dirname(__file__) + "/test_data/Test8.m", "r") as file:
            self.file = file.read()
        pass

        parser = SpecParser(self.file)
        self.assertEqual(parser.root.elements_description(), "Spec: SomeTest1Spec\n\nWhen: first context\n    It: has this test")

if __name__ == '__main__':
    unittest.main()
