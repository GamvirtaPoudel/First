from abc import ABC , abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calclate_perimeter(self):
        pass


class Triangle(Shape):
    def __init__(self,length,breadth,height):
        self.length=length
        self.breadth=breadth
        self.height=height

    def calculate_area(self):
        area=((1/2)*(self.breadth*self.height))
        print(f"\t \tThe area of triangle with breadth {self.breadth} cm  and height {self.height} is ", area, "sq.cm.\n")

    def calclate_perimeter(self):
        perimeter=3*self.length
        print(f"\n \t \tThe perimeter of triangle with length {self.length} cm is ",perimeter,"cm.")


class Rectangle(Shape):
    def __init__(self,length_rectangle,breadth_rectangle):
        self.length_rectangle=length_rectangle
        self.breathd_rectangle=breadth_rectangle

    def calculate_area(self):
        area1=self.length_rectangle*self.breathd_rectangle
        print(f"\t \tThe area of rectangle with length {self.length_rectangle} cm  and breadth {self.breathd_rectangle} is ", area1, "sq.cm.\n")

    def calclate_perimeter(self):
        perimeter1=2*(self.breathd_rectangle+self.length_rectangle)
        print(f"\n \t \tThe perimeter of rectangle with length {self.length_rectangle} and breadth {self.breathd_rectangle} cm is ", perimeter1, "cm.")


class Sphere(Shape):
    def __init__(self,radius):
        self.radius=radius

    def calculate_area(self):
        area2 = (22/7) * (self.radius*2)
        print(f"\t \tThe area of sphere with radius {self.radius} cm is ",area2, "sq.cm.\n")

    def calclate_perimeter(self):
        perimeter2=2*(22/7) * (self.radius)
        print(f"\n \t \tThe perimeter of circle with radius {self.radius} cm is ", perimeter2, "cm.")


class Cuboid(Shape):
    def __init__(self,length_cuboid,breadth_cuboid,height_cuboid):
        self.length_cuboid=length_cuboid
        self.breadth_cuboid=breadth_cuboid
        self.height_cuboid=height_cuboid

    def calculate_area(self):
        area3=(2*((self.length_cuboid*self.breadth_cuboid)+(self.breadth_cuboid*self.height_cuboid)+(self.height_cuboid*self.length_cuboid)))
        print(f"\t \tThe area of cuboid with length {self.length_cuboid} cm breadth {self.breadth_cuboid} and height {self.height_cuboid} is ", area3, "sq.cm.\n")

    def calclate_perimeter(self):
        perimeter3=4*(self.breadth_cuboid*self.length_cuboid*self.height_cuboid)
        print(f"\n \t \tThe perimeter of cuboid with length {self.length_cuboid} breadth {self.breadth_cuboid} and height {self.height_cuboid} cm is ", perimeter3,"cm.")

def calculation():
    print("\t\t===== Geometry Simplified =====")
    print("\t\t=== Welcome to the program. ===\n")

    try:
        print("Choose the polygon to calculate its Area and its Perimeter? \n 1.) Triangle \n 2.) Rectangle \n 3.) Circle \n 4.) Cuboid")
        choice=int(input("\n\tEnter your choice?"))
    except:
        print("\n\tThe program seeks for input in numeric form.\n\tPlease enter a valid number.")
        choice = int(input("\n\tEnter your choice?"))

    if choice==1:
        try:
            value_length=int(input("\t1.Enter the length of the triangle?"))
        except ValueError:
            print("\tThe program seeks for integeral input.\tProvide value in numerical form.")
            value_length = int(input("\t1.Enter the length of the triangle?"))
        try:
            value_breadth=int(input("\t2.Enter the breadth of the triangle?"))
        except ValueError:
            print("\tThe program seeks for integeral input.\tProvide value in numerical form.")
            value_breadth = int(input("\t2.Enter the breadth of the triangle?"))
        try:
            value_height=int(input("\t3.Enter the height of the triangle?"))
        except ValueError:
            print("\tThe program seeks for integeral input.\tProvide value in numerical form.")
            value_height=int(input("\t3.Enter the height of the triangle?"))
        print("\n The calculated result :")
        calculating_obj=Triangle(value_length,value_breadth,value_height)
        calculating_obj.calclate_perimeter()
        calculating_obj.calculate_area()

        try:
            continue_choice = str(input("Do you wish to continue? ( Y / N)"))
        except ValueError:
            print("Please provide value in strings.\n\t Y.) For Yes. \n\t N.) For No.")
            continue_choice = str(input("Do you wish to continue? ( Y / N)"))
        if continue_choice.upper() == "Y":
            calculation()
        elif continue_choice.upper() == "N":
            print("\n\t\t===  Program Terminated  ===")
        elif continue_choice.upper() != "Y" and continue_choice.upper() != "N":
            print("\n\t\tInvalid selection")
            print("\n\t\t===  Program Terminated  ===")
            exit()

    elif choice==2:
        try:
            value_length_1=int(input("\t1.Enter the length of the Rectangle?"))
        except ValueError:
            print("\tThe program seeks for integeral input.\tProvide value in numerical form.")
            value_length_1=int(input("\t1.Enter the length of the Rectangle?"))
        try:
            value_breadth_1=int(input("\t1.Enter the breadth of the Rectangle?"))
        except ValueError:
            print("\tThe program seeks for integeral input.\tProvide value in numerical form.")
            value_breadth_1=int(input("\t1.Enter the breadth of the Rectangle?"))
        print("\n The calculated result :")
        calculationg_obj_1=Rectangle(value_length_1,value_breadth_1)
        calculationg_obj_1.calclate_perimeter()
        calculationg_obj_1.calculate_area()

        try:
            continue_choice0=str(input("Do you wish to continue? ( Y / N)"))
        except ValueError:
            print("Please provide value in strings.\n\t Y.) For Yes. \n\t N.) For No.")
            continue_choice0 = str(input("Do you wish to continue? ( Y / N)"))
        if continue_choice0.upper()=="Y":
            calculation()
        elif continue_choice0.upper() == "N":
            print("\n\t\t===  Program Terminated  ===")
        elif continue_choice0.upper() != "Y" and continue_choice0.upper() != "N":
            print("\n\t\tInvalid selection")
            print("\n\t\t===  Program Terminated  ===")
            exit()

    elif choice==3:
        try:
            value_radius=int(input("\t1.Enter the radius of the Circle?"))
        except ValueError:
            print("\tThe program seeks for integeral input.\tProvide value in numerical form.")
            value_radius=int(input("\t1.Enter the radius of the Circle?"))
        print("\n The calculated result :")
        calculating_obj_2=Sphere(value_radius)
        calculating_obj_2.calclate_perimeter()
        calculating_obj_2.calculate_area()

        try:
            continue_choice1=str(input("Do you wish to continue? ( Y / N)"))
        except ValueError:
            print("Please provide value in strings.\n\t Y.) For Yes. \n\t N.) For No.")
            continue_choice1 = str(input("Do you wish to continue? ( Y / N)"))
        if continue_choice1.upper()=="Y":
            calculation()
        elif continue_choice1.upper()=="N":
            print("\n\t\t===  Program Terminated  ===")
        elif continue_choice1.upper() != "Y" and continue_choice1.upper() != "N":
            print("\n\t\tInvalid selection")
            print("\n\t\t===  Program Terminated  ===" )
            exit()


    elif choice==4:
        try:
            value_length_2=int(input("\t1.Enter the length of the Cuboid?"))
        except ValueError:
            print("\tThe program seeks for integeral input.\tProvide value in numerical form.")
            value_length_2=int(input("\t1.Enter the length of the Cuboid?"))
        try:
            value_breadth_2=int(input("\t1.Enter the breadth of the Cuboid?"))
        except ValueError:
            print("\tThe program seeks for integeral input.\tProvide value in numerical form.")
            value_breadth_2=int(input("\t1.Enter the breadth of the Cuboid?"))
        try:
            value_height_2=int(input("\t1.Enter the height of the Cuboid?"))
        except ValueError:
            print("\tThe program seeks for integeral input.\tProvide value in numerical form.")
            value_height_2=int(input("\t1.Enter the height of the Cuboid?"))
        print("\n The calculated result :")
        calculationg_obj_3=Cuboid(value_length_2,value_breadth_2,value_height_2)
        calculationg_obj_3.calclate_perimeter()
        calculationg_obj_3.calculate_area()

        try:
            continue_choice0=str(input("Do you wish to continue? ( Y / N)"))
        except ValueError:
            print("Please provide value in strings.\n\t Y.) For Yes. \n\t N.) For No.")
            continue_choice0 = str(input("Do you wish to continue? ( Y / N)"))
        if continue_choice0.upper()=="Y":
            calculation()
        elif continue_choice0.upper() == "N":
            print("\n\t\t===  Program Terminated  ===")
        elif continue_choice0.upper() != "Y" and continue_choice0.upper() != "N":
            print("\n\t\tInvalid selection")
            print("\n\t\t===  Program Terminated  ===")


    elif choice==0 or choice > 4:
        print("\n\t\tInvalid selection.")
        print("\n\t\t===  Program Terminated  ===")
        exit()


calculation()


# gaurav