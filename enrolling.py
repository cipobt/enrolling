class Course:
    '''
    Parent or base class for whole course with name and contact_website as constants
    '''
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        '''
        Method that prints out message with hyperlink
        :return: Message inviting user to visit website
        '''
        print("Please contact us by visiting", self.contact_website)

    def head_office(self):
        '''
        Method that prints out location of head office
        :return: Message with head office's location
        '''
        print("The head office location is Cape Town")

class OOPCourse(Course):
    '''
    Derived class or subclass for specific course
    '''
    def __init__(self):
        '''
        Initialising OOPCourse subclass with two constant values
        '''
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        '''
        Method that displays course's name and instructor
        :return: Prints the specific details of this course given by the derived class attributes
        '''
        print(f"\nThis is the {self.description} course and your trainer is {self.trainer}")

    def show_course_id(self):
        '''
        Method that displays  course's ID number
        :return: Prints a message out with the number of the course
        '''
        print("\nThe ID number of the course is # 12345")

# main

course_1 = OOPCourse()
print(f"\nWelcome to the {course_1.name} program")
course_1.head_office()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
