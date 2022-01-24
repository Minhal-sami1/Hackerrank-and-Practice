class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    def __init__(self, firstName, lastName, idNumber, scores = []):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here

    #   Function Name: calculate
    def calculate(self):
        average = 0
        for i in self.scores:
            average += i
        average = average / len(self.scores)
        if (average >= 90.0 and average <= 100.0):
            return "O"
        if (average >= 80.0 and average < 90.0):
            return "E"
        if (average >= 70.0 and average < 80.0):
            return "A"
        if (average >= 55.0 and average < 70.0):
            return "P"
        if (average >= 40.0 and average < 55.0):
            return "D"
        if (average < 40):
            return "T"
        

    #   Return: A character denoting the grade.
    #
    # Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())