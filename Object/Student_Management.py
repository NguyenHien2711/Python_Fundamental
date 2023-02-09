#Định nghiã lớp sinh viên Student gồm các thông tin: mã sinh viên,họ và tên, ngày sinh, quê quán.
#Phương thức info để in thông tin của sinh viên ra màn hình
#Định nghĩa lớp danh sách sinh viên ListStudent thuộc tính là một list Student vừa định nghĩa
#Các phương thức  thêm sinh viên, cập nhập thông tin sinh viên theo mã sinh viên, xóa sinh viên
#trong list, tìm kiếm thông tin theo mã, in toàn bộ danh sách sinh viên ra màn hình
#Viết phần mềm quản lý danh sách sinh viên:
#1. Xem danh mục sinh viên
#2. Thêm sinh viên vào danh sách
#3. Chỉnh sửa thông tin sinh viên
#4. Xóa thông tin sv
#5. Tìm kiếm thông tin sinh viên
#6. Sắp xếp theo các tiêu chí: Tên, Mã
class Student:
    def __init__(self, id, name, dob, address):
        self.id = id
        self.name = name
        self.dob = dob
        self.address = address
    def info(self):
        row = self.id.ljust(20, ' ') + self.name.ljust(25, ' ') + self.dob.ljust(20,' ') + self.address.ljust(25, ' ')
        print(row)
    def rowForWriting(self):
        row = f'{self.id}|{self.name}|{self.dob}|{self.address}+\n'
        return row 

class ListStudent:
    def __init__(self):
        self.liststudent = []
    def load(self):
        stud1 = Student('K194020140', 'Nguyen Thi Thuy Hien', '27/11/2001', 'Quang Ngai')
        stud2 = Student('K194020140', 'Nguyen Thi Thuy Hien', '27/11/2001', 'Quang Ngai')
        stud3 = Student('K194020140', 'Nguyen Thi Thuy Hien', '27/11/2001', 'Quang Ngai')
        self.liststudent = [stud1, stud2, stud3]
    def loadFromFile(self, path):
        f = open(path, 'r', encoding= 'utf8')
        for x in f:
            # if not x.__contains__('|'):
            #     continue
            info = x.split('|')
            st = Student(info[0], info[1], info[2], info[3])
            self.liststudent.append(st)
        f.close()
    def saveFromFile(self, path):
        f = open(path, 'w', encoding = 'utf8')
        for st in self.liststudent:
            f.write(st.rowForWriting())
            f.close()
    def info(self):
        '''Xem danh mục sinh viên'''
        header = 'ID'.ljust(20, ' ') + 'Full name'.ljust(25, ' ') + 'Date of birth'.ljust(20, ' ') + 'Address'.ljust(25, ' ')
        print(header)
        print(''.ljust(90, '='))
        for stud in self.liststudent:
            stud.info()
    def add(self,st):
        '''Thêm sinh viên vào danh sách'''
        self.liststudent.append(st)
    def adjust(self):
        '''Điều chỉnh thông tin sinh viên'''
        pass
    def delete(self, code):
        '''Xóa thông tin sinh viên'''
        for stud in self.liststudent:
            if stud.id == code:
                confirm = input('Enter yes if you want to delete {code}')
                if confirm == 'yes':
                    self.liststudent.remove(stud)
                    print('Delete completed')
                    break
            else:
                print('No ID was found')

    def findout(self, code):
        '''Tìm kiếm thông tin sinh viên'''
        for stud in self.liststudent:
            if stud.id == code:
                stud.info()
            else: 
                print('No ID was found')
        
    def sort(self):
        '''Sắp xếp theo tên mã sinh viên'''
        pass

class Program:
    def __init__(self):
        self.list = ListStudent()
        self.list.loadFromFile('D:\Python cơ bản\Python_Fundamental\Object\data_student.txt')
    def run(self):
        while 1:
            print('============ QUẢN LÝ SINH VIÊN ============')
            print('=== 1. Hiển thị danh sách               ===')
            print('=== 2. Thêm sinh viên                   ===')
            print('=== 3. Chỉnh sửa thông tin              ===')
            print('=== 4. Xoá thông tin sinh viên          ===')
            print('=== 5. Tìm kiếm thông tin               ===')
            print('=== 6. Sắp xếp theo tên                 ===')
            print('=== 7.                  ===')
            print('=== 8. Đóng chương trình                ===')
            print('===========================================')
            choice = input('Nhập lựa chọn: ')
            if choice =='1':
                self.list.info()
                option = int(input('Enter 0 if you want to continue: '))
                if option:
                    break #break khỏi chương trình không while nữa
            elif choice =='2':
                id = input('Enter new id: ')
                name = input('Enter new name: ')
                dob = input('Enter new Date of Birth: ')
                address = input('Enter new address: ')
                newstud = Student(id, name, dob, address)
                self.list.add(newstud)
                self.list.info()
            elif choice == '3':
                pass 
            elif choice == '4':
                pass 
            elif choice == '5':
                pass 
            elif choice == '6':
                pass 
            elif choice == '7':
                self.list.saveFromFile('D:\Python cơ bản\Python_Fundamental\Object\data_student.txt')
                print('Save sucessfull')
            else:
                confirmed = input('Enter True if you want to end: ')
                if confirmed:
                    break 
run = Program()
run.run()
