class First:
    def __init__(self):
        print("This is first Class")
        self.bb=self.First_section_a()
        self.dd = self.First_section_b()

    class First_section_a:
        def __init__(self):
            print("This is First_section_a class")
            self.ccc=self.First_section_a_inside_class()

        class First_section_a_inside_class:
            def __init__(self):
                print("This is First_section_a_inside_class")

    class First_section_b:
        def __init__(self):
            print("This is First_section_b")
            self.eee=self.First_section_b_inside_class()

        class First_section_b_inside_class:
            def __init__(self):
                print("This is First_section_b_inside_class")


a = First()

