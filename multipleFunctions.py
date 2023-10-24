class multipleFunction():
    def Subfields():
        x=["Machine learning","Neural Network","Vision","Robotics","Speech Processing","Natural language processing"]
        print("sub-fields in AI are:")
        print(*x, sep="\n")

    def OddEven():
        number=int(input("Enter a number:"))
        if number % 2 == 0:
            print(f"{number} is an even number.")
            msg="even"
        else:
            print(f"{number} is an odd number.")
            msg="odd"
        return msg

    def Elegible():
        Gender=input("Your Gender:")
        maleAge=int(input("Your Age:"))
        if(maleAge>=21):
            print("ELEGIBLE")
        else:
            print("NOT ELEGIBLE")

    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        total=sub1+sub2+sub3+sub4+sub5
        print("Total:",total)
        percentage=(total/500)*100
        print("Percentage:",percentage,)

    def triangle():
        Height=float(input("Height: "))
        Breadth=float(input("Breadth: "))
        Area=(Height*Breadth)/2
        print("Area Formula: (Height*Breadth)/2")
        print("Area of Triangle:",Area)
        Height1 = float(input("Height1: "))
        Height2 = float(input("Height2: "))
        Breadth = float(input("Breadth: ")) 
        Perimeter = Height1+Height2+Breadth
        print("Perimeter Formula: Height1+Height2+Breadth")
        print("Perimeter of a Triangle: ",Perimeter)
