class Student:
    """Represents a student with their information and grades"""
    
    def __init__(self, name, student_id):
        """Initialize student with name and ID"""
        # Store student's basic information
        self.name = name
        self.student_id = student_id
        # Initialize empty list for grades
        self.grades = []
    
    def add_grade(self, grade):
        """Add a grade to the student's record"""
        # Validate grade is between 0 and 100
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return True
        return False
    
    def calculate_average(self):
        """Calculate the average of all grades"""
        # Check if student has any grades
        if not self.grades:
            return 0
        
        # Calculate and return average
        return sum(self.grades) / len(self.grades)
    
    def get_letter_grade(self):
        """Convert average to letter grade"""
        # Get numerical average
        avg = self.calculate_average()
        
        # Determine letter grade based on average
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
    
    def display_info(self):
        """Display student information"""
        avg = self.calculate_average()
        letter = self.get_letter_grade()
        print(f"Student: {self.name} (ID: {self.student_id})")
        print(f"Grades: {self.grades}")
        print(f"Average: {avg:.2f} (Letter Grade: {letter})")

# Main execution
if __name__ == "__main__":
    # Create a student object
    student = Student("John Doe", "S001")
    
    # Add some grades
    student.add_grade(85)
    student.add_grade(92)
    student.add_grade(78)
    student.add_grade(88)
    
    # Display student information
    student.display_info()
