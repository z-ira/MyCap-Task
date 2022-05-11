#Program to accept file name and print the extention

Fname=input("Enter file name with extention: ");
Fext=Fname.split(".")

if Fext[-1]=="py":
    Fext[-1]="python"
elif Fext[-1]=="cpp":
    Fext[-1]="C++"
elif Fext[-1]=="c":
    Fext[-1]="C"
print(" Extention of file is: ",(Fext[-1]));
