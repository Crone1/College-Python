
def make_map():
   import sys
   student_map = {}
   list_to_sort = []
   for student in sys.stdin.readlines():
      student = student.strip().split()
      
      if student:
         list_to_sort.append(student[0])
         student_map[student[0]] = student[1]
   return student_map