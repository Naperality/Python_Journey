# This is a Mini project involving soem basic functionalities of python 
students = []
src = 'C:/Users/Hp/Desktop/Python_Journey/Beginner/mini_project/students.txt'
def show_menu():
    print('\n--- Student Manager ---')
    print('1. Add Student')
    print('2. View All Students')
    print('3. Remove Student')
    print('4. Search Student')
    print('5. Save to File (txt)')
    print('6. Load to File (txt)')
    print('7. Exit')

def add_students(students):
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    course = input('Enter Course: ')
    
    students.append({'name':name, 'age':age, 'course':course})
    print(f'Student: {name} Course: {course}, is added successfully!')

def view_students(students):
    print('\n --- List of Students ---')
    for student in students:
        print('Name:',student['name'], 'Course:', student['course'], 'Age:', student['age'])

def search_student(students):
    key = ''
    studs = []
    print('\n--- Filter Search ---')
    print('1. By name')
    print('2. By Age')
    print('3. By Course')
    choice = input('Enter number choice: ')
    
    match(choice):
        case '1':
            key = input('Enter Name to be searched: ') 
        case '2':
            key = int(input('Enter age to be searched: '))
        case '3':
            key = input('Enter course to be searched: ')
        case _:
            print('Wrong choice!')
            key = ''
    if key != '':
        for student in students:
            if key in student.values():
                studs.append(student)
        
        view_students(studs)

def remove_student(students):
    while True:
        print('\n--- Remove Student ---')
        print('Note: Enter "exit/Exit" to stop')
        name = input('Enter student name to remove: ')
        
        if name.lower() == 'exit':
            break
        else:
            for student in students:
                if name == student['name']:
                    students.remove(student)
                    print(f'Successfully removed student: {name}')
            print(f'There is no student name: {name}')
            break

def save_to_file(students, filename="students.txt"):
    with open(filename, "w") as file:
        for s in students:
            file.write(f"{s['name']},{s['age']},{s['course']}\n")
    print("Saved successfully!")

def load_from_file(filename="students.txt"):
    students = []
    try:
        with open(filename, "r") as file:
            for line in file:
                name, age, course = line.strip().split(",")
                students.append({"name": name, "age": int(age), "course": course})
    except FileNotFoundError:
        print("No saved file found.")
    return students

def main():
    while True:
        show_menu()
        choice = input('Enter number choice: ')
        
        match(choice):
            case '1':
                add_students(students)
            case '2':
                view_students(students)
            case '3':
                remove_student(students)
            case '4':
                search_student(students)
            case '5':
                save_to_file(students,src)
            case '6':
                students = load_from_file(src)
            case '7':
                print('Exiting program...')
                break
            case _:
                print('Wrong choice!, Try again...')
main()