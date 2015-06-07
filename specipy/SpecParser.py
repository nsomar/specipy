__author__ = 'omarsubhiabdelhafith'

import re
from SpecElements import *


class SpecParser(object):

    def __init__(self, file, root_class=RootDecorator, describe_class=DescribeDecorator, context_class=ContextDecorator, it_class=ItDecorator):
        self.file = file
        self.bracket_count = 0
        self.root = None
        self.spec_name = None

        self.root_class = root_class
        self.describe_class = describe_class
        self.context_class = context_class
        self.it_class = it_class

        self.parse()

    def parse(self):
        self.root = TestElement("Root", self.root_class)
        self.bracket_count = 0
        stack = []
        line_number = 0

        start_ignoring_lines = False

        for line in self.file.splitlines():
            self.read_spec_name(line)
            self.parse_brackets(line)
            line_number += 1

            if self.multiline_comment_end(line): start_ignoring_lines = False
            if start_ignoring_lines: continue

            start_ignoring_lines = self.multiline_comment_start(line)

            if self.bracket_count <= 0 and self.has_closing_bracket(line) and len(stack) > 0:
                stack.pop()

            current_element = self.read_element(line)

            if not current_element: continue

            self.bracket_count = 0
            self.parse_brackets(line)

            if len(stack) == 0:
                self.root.add_child(current_element)

            top_element = stack[-1] if len(stack) > 0 else None
            if top_element:
                top_element.add_child(current_element)

            stack.append(current_element)

        self.root.name = self.spec_name
        return self.root

    def read_spec_name(self, line):
        m = re.match(r"SPEC_BEGIN\((.*)\)", line)

        if m:
            self.spec_name = m.group(1)

    def read_element(self, line):
        line = self.line_before_comments(line)

        m = re.match(r"describe\(@\"(.*)\"", line)
        if m:
            return TestElement(m.group(1), self.describe_class)

        m = re.match(r".*context\(@\"(.*)\"", line)
        if m:
            return TestElement(m.group(1), self.context_class)

        m = re.match(r".*it\(@\"(.*)\"", line)
        if m:
            return TestElement(m.group(1), self.it_class)

    def line_before_comments(self, line, only_single_line=False):
        if "/*" or "*/" in line:
            line = re.sub(r"(/\*.*\*/)", "", line)

        if "*/" in line:
            return ""

        if "/*" in line and not only_single_line:
            m = re.match(r"(.*?)/*", line)
            line = m.group(0)
        elif "//" in line:
            m = re.match(r"(.*?)//", line)
            line = m.group(0)

        return line

    def multiline_comment_start(self, line):
        line = self.line_before_comments(line, True)
        return "/*" in line

    def multiline_comment_end(self, line):
        return "*/" in line

    def parse_brackets(self, line):
        line = self.line_before_comments(line)

        openning_count = line.count("{")
        closing_count = line.count("}")

        self.bracket_count += openning_count
        self.bracket_count -= closing_count

    def has_closing_bracket(self, line):
        line = self.line_before_comments(line)

        return line.count("}") > 0
