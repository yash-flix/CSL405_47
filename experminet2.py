class Employee:
    def __init__ (
            self,
            designation : str = 'Developer',
            frontend : bool = False,
            backend : bool = False
    ):
        self.designation = designation
        self.frontend = frontend
        self.backend = backend

    def __repr__ (self):
        return '{}'.format(self.designation)

    def verifier(self):
        if self.frontend and self.backend:
            return "Fullstack"
        elif self.frontend:
            return "Frontend"
        elif self.backend:
            return "Backend"
        else:
            return "Not a Developer"

if __name__ == '__main__':
    firstEmployee = Employee(frontend=True, backend=True)
    print("Employee is " + firstEmployee.verifier()+ "developer")  
    secondEmployee = Employee(frontend=True, backend=False)
    print("Employee is" + secondEmployee.verifier()+ "developer")  
    thirdEmployee = Employee(frontend=False, backend=True)
    print("Employee is " +thirdEmployee.verifier()+ "developer")  
    fourthEmployee = Employee(frontend=False, backend=False)
    print("Employee is "+fourthEmployee.verifier()+ "developer") 
output:
Employee is Fullstackdeveloper
Employee is Frontenddeveloper
Employee is Backenddeveloper
Employee is Not a Developerdeveloper
