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
from psycopg.rows import dict_row

app = FastAPI()



      


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
                ( student_name , father_name , phone_number, fees)
                VALUES (%s, %s, %s, %s)
                RETURNING *
                """,
                (
                    student.name,
                    student.father_name,
                    student.phone_number,
                    student.fees
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
                "message": "Subject added successfully",
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
                      ( employee_name,phone_number,work,education,date_of_birth,father_name,year,role,uu_id)
                      VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)
                      RETURNING *
                      """,
                      (
                          employees.employee_name,
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
            cursor.execute("SELECT * FROM fees ")
            fees = cursor.fetchall()
            if not fees:
                  raise RecordNotFound(404,"record not found")
            return fees    



@app.get("/students")
def get_student():
      with psycopg.connect("dbname=sms user=postgres password=12341234 host=localhost", row_factory=dict_row) as connection:
      
          with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM students ")
            fees = cursor.fetchall()
            if not fees:
                  raise RecordNotFound(404,"record not found")
            return fees   
          


@app.get("/subjects")
def get_subject():
    with psycopg.connect("dbname=sms user=postgres password=12341234 host=localhost", row_factory=dict_row) as connection:
    
          with connection.cursor() as cursor:
             cursor.execute("SELECT * FROM subject")
             subject = cursor.fetchall()
             if not subject:
                 raise RecordNotFound(404,"record not found")      
             return subject

@app.get("/employees")
def get_employee():
      with psycopg.connect("dbname=sms user=postgres password=12341234 host=localhost", row_factory=dict_row) as connection:
      
          with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM employees")
            employees = cursor.fetchall()
            if not employees:
                  raise RecordNotFound(404,"record not found")
            return employees 

@app.get("/salary")
def get_fees():
      with psycopg.connect("dbname=sms user=postgres password=12341234 host=localhost", row_factory=dict_row) as connection:
      
          with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM salary")
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
                "SELECT * FROM employees WHERE id = %s",
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
                "SELECT * FROM salary WHERE id = %s",
                (id,)
            )

            salary = cursor.fetchone()
            if not salary:
                   raise RecordNotFound(404,"record not found")

            return salary       


@app.get("/subject/{id}")
def get_salary(id:int):

    with psycopg.connect(
        "dbname=sms user=postgres password=12341234 host=localhost",
        row_factory=dict_row
    ) as connection:

        with connection.cursor() as cursor:

            cursor.execute(
                "SELECT * FROM subject WHERE id = %s",
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
                "SELECT * FROM fees WHERE id = %s",
                (id,)
            )

            fees = cursor.fetchone()
            if not fees:
                   raise RecordNotFound(404,"record not found")

            return fees


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    with psycopg.connect(
        "dbname=sms user=postgres password=12341234 host=localhost",
        row_factory=dict_row
    ) as connection:

    
          with connection.cursor() as cursor:

              cursor.execute(
                "DELETE FROM fees WHERE student_id = %s",
              (student_id,)
              )

              cursor.execute(
              "DELETE FROM students WHERE id = %s",
              (student_id,)
              )

              if cursor.rowcount == 0:
                  raise RecordNotFound(404, f"Invalid student_id {student_id}")

          connection.commit()

          return {"message": "Student is deleted"}

    



@app.delete("/employees/{employee_id}")
def delete_student(employee_id: int):
    with psycopg.connect(
        "dbname=sms user=postgres password=12341234 host=localhost",
        row_factory=dict_row
    ) as connection:

    
          with connection.cursor() as cursor:

              cursor.execute(
              "DELETE FROM salary WHERE employee_id = %s",
              (employee_id,)
              )

              cursor.execute(
              "DELETE FROM employees WHERE id = %s",
              (employee_id,)
              ) 

              if cursor.rowcount == 0:
                  raise RecordNotFound(404, f"Invalid employee_id {employee_id}")

          connection.commit()

          return {"message": "employee is deleted"}




@app.delete("/subjects/{id}")
def delete_student(id: int):
    with psycopg.connect(
        "dbname=sms user=postgres password=12341234 host=localhost",
        row_factory=dict_row
    ) as connection:

    
          with connection.cursor() as cursor:

              cursor.execute(
              "DELETE FROM subjects WHERE id = %s",
              (id,)
              )

              

              if cursor.rowcount == 0:
                  raise RecordNotFound(404, f"Invalid employee_id {id}")

          connection.commit()

          return {"message": "subject is deleted"}

    






