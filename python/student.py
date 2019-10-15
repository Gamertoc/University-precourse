class Srudent:
    def __init__(self, name, course=[], mail="", number="", ID=0):
        self.name = name
        self.course = course
        self.mail = mail
        self.number = number
        self.ID = ID
        print("Created student", self.name)
        return

    def details(self):
        print("Name: ", self.name)
        print("Course: ", self.course)
        print("Mail: ", self.mail)
        print("Number: ", self.number)
        print("ID: ", self.ID)
        return

    def attend(self, course):
        self.course.append(course)
        return
