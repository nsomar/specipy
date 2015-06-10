

class TestElement:

    def __init__(self, content, decorator_class):
        self.name = content
        self.children = []
        self.decorator = decorator_class()

    def add_child(self, child):
        self.children.append(child)

    def elements_description(self):
        return "\n".join(self.elements_description_r(-1, []))

    def elements_description_r(self, level, acc):
        prefix = [" "] * (level * 4)
        prefix = "".join(prefix)

        string = (self.decorator.before_decoration()) +\
            prefix + self.decorator.name_decoration(self.name) +\
            self.decorator.after_decoration()

        acc.append(string)

        if self.children:
            for child in self.children:
                child.elements_description_r(level+1, acc)

        return acc


class BaseDecorator(object):

    def after_decoration(self):
        return ""

    def name_decoration(self, element_name):
        return ""

    def before_decoration(self):
        return ""


class RootDecorator(BaseDecorator):

    def name_decoration(self, element_name):
        return "Spec: %s" % element_name


class DescribeDecorator(BaseDecorator):

    def name_decoration(self, element_name):
        return "Describe: %s" % element_name

    def before_decoration(self):
        return "\n" + "".join(["-"] * 50) + "\n"

    def after_decoration(self):
        return "\n" + "".join(["-"] * 50)


class ContextDecorator(BaseDecorator):

    def name_decoration(self, element_name):
        return "When: %s" % element_name

    def before_decoration(self):
        return "\n"


class ItDecorator(BaseDecorator):

    def name_decoration(self, element_name):
        return "It: %s" % element_name
