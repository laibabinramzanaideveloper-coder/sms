from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import psycopg
from fastapi import status
import json
from dto import Student
from dto import Subject
from dto import Employees
from dto import Fees
from dto import Salary
from dto import UpdateStudent
from dto import UpdateEmployee
from dto import UpdateFees
from dto import UpdateSalary
from dto import UpdateSubject
from psycopg.rows import dict_row
import logging

app = FastAPI()
logging.basicConfig(
    level=logging.DEBUG)

logger = logging.getLogger(__name__)
# debug 0
# info 1
# error 2



      


@app.middleware("http")
async def my_middleware(request, call_next):
    print("I AM A MIDDLEWARE")
#    {"headers":{},"scope":[]}
    print("........................")
    req_headers=request.scope["headers"]
    # frutis=[]
    # frutis.append()
    for req_header in req_headers:
          header_name=req_header[0]
          header_value=req_header[1]
          print(f'{header_name}:{header_value}')
    print("........................")
    
    req_headers.append(
        (b"x-user-id", b"12345")
    )

    response = await call_next(request)
    response.headers["backend_server"] = "fast-api"

    return response



class RecordNotFound(Exception):
      def __init__(self,status_code, *args):
            super().__init__(*args)
            self.status_code=status_code


@app.exception_handler(RecordNotFound)
def record_not_found_handler(request:Request,exc: RecordNotFound):

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": str(exc)
        }
        )



@app.exception_handler(Exception)
def record_not_found_handler(request:Request,exc:Exception):
      print("............")
      print(exc)
      return JSONResponse( 
           status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
           content={
                "message":"Something went wrong on server. our engineers are working it. please try again latter"
           }
      )


@app.post("/students")
def create_student(student: Student):

    with psycopg.connect(
        "dbname=sms user=postgres password=12341234 host=localhost",
        row_factory=dict_row
    ) as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO students
                (student_name , phone_number)
                VALUES (%s, %s)
                RETURNING *
                """,
                (
                    student.name,
                    student.phone_number,
                    
                )   
            )

            new_student = cursor.fetchone()

            return {
                "message": "Student added successfully",
                "student": new_student
            }
    

@app.post("/subjects")
def create_subject(subject:Subject):
     
    with psycopg.connect(
        "dbname=sms user=postgres password=12341234 host=localhost",
        row_factory=dict_row
    ) as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO subject
                ( subject_name , teacher_name)
                VALUES (%s, %s)
                RETURNING *
                """,
                (
                    subject.name,
                    subject.teacher_name
                    
                )   
            )

            new_subject = cursor.fetchone()

            return {
                "message": "Subject added successfully",
                "student": new_subject
            }


@app.post("/fees")
def create_fees(fee:Fees):

     
    with psycopg.connect(
        "dbname=sms user=postgres password=12341234 host=localhost",
        row_factory=dict_row
    ) as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO fees
                ( student_id, amount)
                VALUES (%s, %s)
                RETURNING *
                """,
                (
                    fee.student_id,
                    fee.amount
                    
                )   
            )

            new_fee = cursor.fetchone()

            return {
                "message": "fees added successfully",
                "fee": new_fee
            }


@app.post("/salary")
def create_fees(salary:Salary):

     
    with psycopg.connect(
        "dbname=sms user=postgres password=12341234 host=localhost",
        row_factory=dict_row
    ) as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO salary
                ( employee_id, amount)
                VALUES (%s, %s)
                RETURNING *
                """,
                (
                    salary.employee_id,
                    salary.amount
                    
                )   
            )

            new_salary = cursor.fetchone()

            return {
                "message": "salary added successfully",
                "fee": new_salary
            }

@app.post("/employees")
def create_fees(employees:Employees):
      with psycopg.connect(
              "dbname=sms user=postgres password=12341234 host=localhost",
              row_factory=dict_row
          ) as connection:
      
              with connection.cursor() as cursor:
      
                  cursor.execute(
                      """
                      INSERT INTO employees
                      ( employee_name,phone_number,work,education,date_of_birth,father_name,year,role)
                      VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                      RETURNING *
                      """,
                      (
                          employees.name,
                          employees.phone_number,
                          employees.work,
                          employees.education,
                          employees.date_of_birth,
                          employees.father_name,
                          employees.year,
                          employees.role
                          
                      )   
                  )
      
                  new_employee = cursor.fetchone()
      
                  return {
                      "message": "employee added successfully",
                      "fee": new_employee
                  }
     
@app.get("/students/{id}")
def get_student(id:int):

    with psycopg.connect(
        "dbname=sms user=postgres password=12341234 host=localhost",
        row_factory=dict_row
    ) as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                "SELECT * FROM students WHERE id = %s",
                (id,)
            )

            student = cursor.fetchone()
            if not student:
                   raise RecordNotFound(404,"record not found")

            return student
        
@app.get("/fees")
def get_fees():
      with psycopg.connect("dbname=sms user=postgres password=12341234 host=localhost", row_factory=dict_row) as connection:
      
          with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM fees WHERE is_deleted = false")
            fees = cursor.fetchall()
            if not fees:
                  raise RecordNotFound(404,"record not found")
            return fees    
        


@app.get("/students")
def get_student():
      
      with psycopg.connect("dbname=sms user=postgres password=12341234 host=localhost", row_factory=dict_row) as connection:
      
          with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM students WHERE is_deleted = false ")
            fees = cursor.fetchall()
            if not fees:
                  raise RecordNotFound(404,"record not found")
            return fees   
          
@app.patch("/students/{student_id}")
def update_student(student_id:int,student_updated_data:UpdateStudent):

    #   logger.debug("debug++++++++++++++")
    #   logger.info("Update data: %s", update_data)
    #   logger.error("error+++++++++++++")
    #   print(update_data)
    #   logger.info(f"{student_updated_data.phone_number} namber")
    #   logger.info(f"{student_updated_data.name} name")
      with psycopg.connect("dbname=sms user=postgres password=12341234 host=localhost", row_factory=dict_row) as connection:
            with connection.cursor() as cursor:
                 cursor.execute("""select * from students WHERE id = %s and is_deleted = false""",(student_id,))
                 student=cursor.fetchone()
                 if not student:
                       raise RecordNotFound(404,"record not found")
                 cursor.execute("""
                 update students
                 set phone_number = COALESCE(%s, phone_number),
                  student_name =COALESCE(%s, student_name)
                 where id = %s
                 RETURNING *""",
                 (
                    student_updated_data.phone_number,
                    student_updated_data.name,
                    student_id
                 )
                 
                 )
             
            connection.commit()
            return {"message":"student update successfully"}
@app.patch("/employees/{employee_id}")
def update_student(employee_id:int,employee_updated_data:UpdateEmployee):

    #   logger.debug("debug++++++++++++++")
    #   logger.info("Update data: %s", update_data)
    #   logger.error("error+++++++++++++")
    #   print(update_data)
    #   logger.info(f"{student_updated_data.phone_number} namber")
    #   logger.info(f"{student_updated_data.name} name")
      with psycopg.connect("dbname=sms user=postgres password=12341234 host=localhost", row_factory=dict_row) as connection:
            with connection.cursor() as cursor:
                 cursor.execute("""select * from employees WHERE id = %s and is_deleted = false""",(employee_id,))
                 employee=cursor.fetchone()
                 if not employee:
                       raise RecordNotFound(404,"record not found")
                 cursor.execute("""
                 update employees
                 set phone_number = COALESCE(%s, phone_number),
                  employee_name =COALESCE(%s, employee_name),
                  work=COALESCE(%s,work),
                  education=COALESCE(%s,education),
                  date_of_birth=COALESCE(%s,date_of_birth),
                  father_name=COALESCE(%s,father_name),
                  year=COALESCE(%s,year),
                  role=COALESCE(%s,role)
                 where id = %s
                 RETURNING *""",
                 (
                    employee_updated_data.phone_number,
                    employee_updated_data.name,
                    employee_updated_data.work,
                    employee_updated_data.education,
                    employee_updated_data.date_of_birth,
                    employee_updated_data.father_name,
                    employee_updated_data.year,
                    employee_updated_data.role,

                    employee_id
                 )
                 
                 )
                 
            connection.commit()
            return {"message":"employee update successfully"}


@app.patch("/fees/{student_id}")
def update_student(student_id:int,fees_updated_data:UpdateFees):

    #   logger.debug("debug++++++++++++++")
    #   logger.info("Update data: %s", update_data)
    #   logger.error("error+++++++++++++")
    #   print(update_data)
    #   logger.info(f"{student_updated_data.phone_number} namber")
    #   logger.info(f"{student_updated_data.name} name")
      with psycopg.connect("dbname=sms user=postgres password=12341234 host=localhost", row_factory=dict_row) as connection:
            with connection.cursor() as cursor:
                 cursor.execute("""select * from fees WHERE id = %s and is_deleted = false""",(student_id,))
                 fees=cursor.fetchone()
                 if not fees:
                       raise RecordNotFound(404,"record not found")
                 cursor.execute("""
                 update fees
                 set amount = COALESCE(%s, amount),
                  student_id =COALESCE(%s, student_id)
                 where id = %s
                 RETURNING *""",
                 (
                    fees_updated_data.amount,
                    fees_updated_data.student_id,
                    student_id
                 )
                 
                 )
             
            connection.commit()
            return {"message":"fees update successfully"}
@app.patch("/salary/{employee_id}")
def update_student(employee_id:int,employee_updated_data:UpdateSalary):

    #   logger.debug("debug++++++++++++++")
    #   logger.info("Update data: %s", update_data)
    #   logger.error("error+++++++++++++")
    #   print(update_data)
    #   logger.info(f"{student_updated_data.phone_number} namber")
    #   logger.info(f"{student_updated_data.name} name")
      with psycopg.connect("dbname=sms user=postgres password=12341234 host=localhost", row_factory=dict_row) as connection:
            with connection.cursor() as cursor:
                 cursor.execute("""select * from salary WHERE id = %s and is_deleted = false""",(employee_id,))
                 salary=cursor.fetchone()
                 if not salary:
                       raise RecordNotFound(404,"record not found")
                 cursor.execute("""
                 update salary
                 set amount = COALESCE(%s, amount),
                  employee_id =COALESCE(%s, employee_id)
                 where id = %s
                 RETURNING *""",
                 (
                    employee_updated_data.amount,
                    employee_updated_data.employee_id,
                    employee_id
                 )
                 
                 )
             
            connection.commit()
            return {"message":"salary update successfully"}


@app.patch("/subjects/{subject_id}")
def update_student(subject_id:int,subject_updated_data:UpdateSubject):

    #   logger.debug("debug++++++++++++++")
    #   logger.info("Update data: %s", update_data)
    #   logger.error("error+++++++++++++")
    #   print(update_data)
    #   logger.info(f"{student_updated_data.phone_number} namber")
    #   logger.info(f"{student_updated_data.name} name")
      with psycopg.connect("dbname=sms user=postgres password=12341234 host=localhost", row_factory=dict_row) as connection:
            with connection.cursor() as cursor:
                 cursor.execute("""select * from subject WHERE id = %s and is_deleted = false""",(subject_id,))
                 subject=cursor.fetchone()
                 if not subject:
                       raise RecordNotFound(404,"record not found")
                 cursor.execute("""
                 update subject
                 set teacher_name = COALESCE(%s, teacher_name),
                  subject_name =COALESCE(%s, subject_name)
                 where id = %s
                 RETURNING *""",
                 (
                    subject_updated_data.name,
                    subject_updated_data.teacher_name,
                    subject_id
                 )
                 
                 )
             
            connection.commit()
            return {"message":"subject update successfully"}
@app.get("/subjects")
def get_subject():
    with psycopg.connect("dbname=sms user=postgres password=12341234 host=localhost", row_factory=dict_row) as connection:
    
          with connection.cursor() as cursor:
             cursor.execute("SELECT * FROM subject WHERE is_deleted = false")
             subject = cursor.fetchall()
             if not subject:
                 raise RecordNotFound(404,"record not found")      
             return subject

@app.get("/employees")
def get_employee():
      with psycopg.connect("dbname=sms user=postgres password=12341234 host=localhost", row_factory=dict_row) as connection:
      
          with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM employees WHERE is_deleted = false")
            employees = cursor.fetchall()
            if not employees:
                  raise RecordNotFound(404,"record not found")
            return employees 

@app.get("/salary")
def get_fees():
      with psycopg.connect("dbname=sms user=postgres password=12341234 host=localhost", row_factory=dict_row) as connection:
      
          with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM salary WHERE is_deleted = false")
            fees = cursor.fetchall()
            if not fees:
                  raise RecordNotFound(404,"record not found")
            return fees        


     
@app.get("/employees/{id}")
def get_employee(id:int):

    with psycopg.connect(
        "dbname=sms user=postgres password=12341234 host=localhost",
        row_factory=dict_row
    ) as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                "SELECT * FROM employees WHERE id = %s and is_deleted =false",
                (id,)
            )

            employees = cursor.fetchone()
            if not employees:
                   raise RecordNotFound(404,"record not found")

            return employees

@app.get("/salary/{id}")
def get_salary(id:int):

    with psycopg.connect(
        "dbname=sms user=postgres password=12341234 host=localhost",
        row_factory=dict_row
    ) as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                "SELECT * FROM salary WHERE id = %s and is_deleted = false",
                (id,)
            )

            salary = cursor.fetchone()
            if not salary:
                   raise RecordNotFound(404,"record not found")

            return salary       


@app.get("/subjects/{id}")
def get_subject(id:int):

    with psycopg.connect(
        "dbname=sms user=postgres password=12341234 host=localhost",
        row_factory=dict_row
    ) as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                "SELECT * FROM subject WHERE id = %s and is_deleted = false",
                (id,)
            )

            subject = cursor.fetchone()
            if not subject:
                   raise RecordNotFound(404,"record not found")

            return subject    
@app.get("/fees/{id}")
def get_salary(id:int):

    with psycopg.connect(
        "dbname=sms user=postgres password=12341234 host=localhost",
        row_factory=dict_row
    ) as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                "SELECT * FROM fees WHERE id = %s and is_deleted = false",
                (id,)
            )
            # if cursor.rowcount == 0:
            #   raise RecordNotFound(404, f"Invalid student_id {student_id}")

            fees = cursor.fetchone()
            if not fees:
                   raise RecordNotFound(404,"record not found")

            return fees


# @app.delete("/students/{student_id}")
# def delete_student(student_id: int):
#     with psycopg.connect(
#         "dbname=sms user=postgres password=12341234 host=localhost",
#         row_factory=dict_row
#     ) as connection:

    
#           with connection.cursor() as cursor:

#               cursor.execute(
#                 "DELETE FROM fees WHERE student_id = %s",
#               (student_id,)
#               )

#               cursor.execute(
#               "DELETE FROM students WHERE id = %s",
#               (student_id,)
#               )

#               if cursor.rowcount == 0:
#                   raise RecordNotFound(404, f"Invalid student_id {student_id}")

#           connection.commit()

#           return {"message": "Student is deleted"}




@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    with psycopg.connect(
        "dbname=sms user=postgres password=12341234 host=localhost",
        row_factory=dict_row
    ) as connection:

    
          with connection.cursor() as cursor:
              cursor.execute("""
              select * from students where id =%s and is_deleted = false""",
              (student_id,) 
              )
              student=cursor.fetchone()
              if student is None:
                  raise RecordNotFound(404, "record not found")
            #   elif student["is_deleted"]: dead code
            #         raise RecordNotFound(404,"student already deleted")
                   
            #   else:
              cursor.execute(
                 """UPDATE students
                  SET is_deleted = True
                  WHERE id= %s""",
                 (student_id,)
                 ) 

              cursor.execute(
                """UPDATE fees
                 SET is_deleted = True
                 WHERE id= %s""",
                 (student_id,)
                 )          

            

          connection.commit()

          return {"message": "Student is deleted"}



# @app.delete("/employees/{employee_id}")
# def delete_student(employee_id: int):
#     with psycopg.connect(
#         "dbname=sms user=postgres password=12341234 host=localhost",
#         row_factory=dict_row
#     ) as connection:

    
#           with connection.cursor() as cursor:

#               cursor.execute(
#               "DELETE FROM salary WHERE employee_id = %s",
#               (employee_id,)
#               )

#               cursor.execute(
#               "DELETE FROM employees WHERE id = %s",
#               (employee_id,)
#               ) 

#               if cursor.rowcount == 0:
#                   raise RecordNotFound(404, f"Invalid employee_id {employee_id}")

#           connection.commit()

#           return {"message": "employee is deleted"}



@app.delete("/employees/{employee_id}")
def delete_student(employee_id: int):
    with psycopg.connect(
        "dbname=sms user=postgres password=12341234 host=localhost",
        row_factory=dict_row
    ) as connection:

    
          with connection.cursor() as cursor:
            cursor.execute("""
            select * from employees where id =%s and is_deleted = false""",
            (employee_id,)               
            )
            employee=cursor.fetchone
            if employee is None:
                  raise RecordNotFound(404,"record not found")
            # elif employee["is deleted"]: dead cod
            #       raise RecordNotFound(404, "employee already deleted")
            
                 
            cursor.execute(
                  """UPDATE employees
                   SET is_deleted = True
                   WHERE id= %s""",
                   (employee_id,)
                   ) 
            cursor.execute(
                  """UPDATE salary
                  SET is_deleted = True
                  WHERE id= %s""",
                  (employee_id,)
                  ) 

          connection.commit()

          return {"message": "employee is deleted"}


@app.delete("/subjects/{id}")
def delete_subject(id: int):
    with psycopg.connect(
        "dbname=sms user=postgres password=12341234 host=localhost",
        row_factory=dict_row
    ) as connection:

    
          with connection.cursor() as cursor:
              cursor.execute("""
            select * from subject where id =%s""",
            (id,)               
            )
              subject=cursor.fetchone()
              if subject is None:
                 raise RecordNotFound(404,"record not found")
              elif subject["is_deleted"]:
                 raise RecordNotFound(404, "subject already deleted")
              
              else:
                  cursor.execute(
                  """UPDATE subject
                  SET is_deleted = True
                  WHERE id= %s""",
                  (id,)
                  ) 
                 

              


          connection.commit()

          return {"message": "subject is deleted"}

    






