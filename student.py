import csv

def write_in_csv(info_list):
    with open('student_info_csv','a',newline='') as csv_file:
        writer=csv.writer (csv_file)
        if csv_file.tell()==0:
            writer.writerow(["name", "age","contact number", "email" ])
        writer.writerow(info_list)

if __name__=='__main__':      
    condition=True
    student_num=1
    
    while(condition):
        student_info=input("enter student info in format for stuent {}(name,age,Contact,email): ".format(student_num))
       
        #split
        stud_info_list= student_info.split(' ')

        print("\n The entered info is: \n name: {}\n age: {}\n contact: {}\n email: {}".format(stud_info_list[0],stud_info_list[1],stud_info_list[2],stud_info_list[3]))

        choice_check=input("is entered info correct? (y/n): ")
        
        if choice_check=="yes":
            write_in_csv(stud_info_list)
            
            condition_check=input("enter y/n if you want to enter more:")
            if condition_check=="yes":
                condition=True
                student_num= student_num+1
            elif condition_check=="no":
                condition= False
                
        elif choice_check=="no":
            print("\n re-enter the values")
