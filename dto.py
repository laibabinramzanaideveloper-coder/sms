from pydantic import BaseModel
from typing import Literal

class Student(BaseModel):
    name:str
    father_name:str
    phone_number:str
    fees:str

class Subject(BaseModel):
     name:str
     teacher_name:str




class Employees(BaseModel):
      name:str
      phone_number:str
      work:str
      education:str
      date_of_birth:str
      father_name:str
      year:int
      role: Literal["employee", "teacher", "principal"] 
        

class Fees(BaseModel):
      
      amount:int
      student_id:int
      

class Salary(BaseModel):
      amount:int
      employee_id:int

      

