def analyze_result(name,roll,marks):
    total=sum(marks)
    average=total/len(marks)
    
    if(average>=90):
        grade="A"
    elif(average>=75):
        grade="B"
    elif(average>=60):
        grade="C"
    elif(average>=40):
        grade="D"
    else:
        grade="Fail"
    
    print(f"Student:{name}(Roll:{roll})")
    print(f"Tolat:{total},Average:{average}")
    print("Grade:",grade)
    print("Subjects below 40:")
    
    found=False
    for i in range(len(marks)):
        if(marks[i]<40):
            print("Subject",i+1,":",marks[i])
            found=True
    if not found:
        print("none")

name=input("Enter your name:") 
roll=int(input("Enter your roll no:"))
marks=list(map(int,input("Enter marks:").split()))
analyze_result(name,roll,marks)  