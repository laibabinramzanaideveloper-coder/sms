from pydantic import BaseModel
from typing import Literal
from typing import Optional

class Student(BaseModel):
    name:str
    
    phone_number:str
    
# class UpdateStudent(BaseModel):
#       name:str | None = None
#       phone_number:str | None = None
# from pydantic import BaseModel

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None 
class UpdateEmployee(BaseModel):
      name:Optional[str]=None
      phone_number:Optional[str]=None
      work:Optional[str]=None
      education:Optional[str]=None
      date_of_birth:Optional[str]=None
      father_name:Optional[str]=None
      year:Optional[str]=None
      role:Optional[Literal["employee", "teacher", "principal"]] =None
    


class UpdateFees(BaseModel):
    amount: Optional[int] = None
    student_id: Optional[int] = None 

class UpdateSalary(BaseModel):
    amount: Optional[int] = None
    employee_id: Optional[int] = None


class UpdateSubject(BaseModel):
    name: Optional[str] = None
    teacher_name: Optional[str] = None
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
      year:str
      role: Literal["employee", "teacher", "principal"] 
       

class Fees(BaseModel):
      
      amount:int
      student_id:int
      

class Salary(BaseModel):
      amount:int
      employee_id:int

      

