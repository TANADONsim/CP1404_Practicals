class ProgrammingLanguage:

    def __init__(self, field="", typing="", reflection="", year=""):

        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.field = field

    def is_dynamic(self):
        if self.typing.lower() == "dynamic":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {} typing, Reflection = {}, First appeared in {}".format(self.field, str(self.typing), str(self.reflection), str(self.year))

