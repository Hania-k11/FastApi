from typing import List, Optional
from pydantic import BaseModel
from datetime import date, time


# class ItemBase(BaseModel):
#     title: str
#     description: Optional[str] = None

# class ItemCreate(ItemBase):
#     pass

# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


class UserCreate(BaseModel):
    DEPTNO: int
    DNAME: str
    Locid: int

class User(BaseModel):
    email: str
    hashed_password: str

    class Config:
        orm_mode = True


class DepartmentSchema(BaseModel):
    DEPTNO: int
    DNAME: str
    Locid: int

    class Config:
        orm_mode = True
        
class AppointmentSchema(BaseModel):
    appointment_id: Optional[int] = None
    appointment_date: date
    appointment_time: time
    patient_name: str
    patient_age: int
    additional_information: str

    class Config:
       orm_mode = True


class Doctor(BaseModel):
    id: Optional[int] = None
    name: str
    specialization: str

class Patient(BaseModel):
    patient_id: Optional[int] = None
    name: str
    email: str
    gender: str
    age: int
    address: str
    phone: str
    region: str
    date_of_birth: date

class Visits(BaseModel):
    visitid: int
    doctorid: int
    patientid:int
    dateofvisit: date
    timeofvisit: time

    class Config:
        orm_mode = True

class Doctor2schema(BaseModel):
    DoctorID: int
    DoctorAge: int
    DoctorName: str
    Descriptions: str
    ExperienceInYears: float
    PatientDealt: int
    ShiftStart: time
    ShiftEnd: time
    Specialty: str
    Designation: str
    Rating: str

    class Config:
        orm_mode = True

        



class Patient2schema(BaseModel):
    PatientID: int
    FullName: str
    Age: str
    Gender: str
    HomeAdress: str
    ContactInformation: str
    EmergencyContact: str

    class Config:
        orm_mode = True
        
class HospitalSchema(BaseModel):
    hospital_ID: int
    name: str
    address: str
    location:str
    city: str
    
    class Config:
        orm_mode = True
        

class Department(BaseModel):
    deptID: int
    deptName: str
    hospital_id: int
   
    class Config:
        orm_mode = True
        
 #mydatabase final       

class hania(BaseModel):
    ID: int
    
    class Config:
        orm_mode = True
        

   
        
class patient00(BaseModel):
    patientid: int
    patientname: str
    patientage: int 
    patientgender: str
    patientcontact: str
    testdate: str
    testtime: str
    testname: str
     
    class Config:
        orm_mode = True        
        

class Loginn(BaseModel):
    logID: int
    email: str
    password: str
    name : str
    
    class Config:
        orm_mode = True        
        

class Laboratorist(BaseModel):
    laboratorist_ID: int
    EmpID: int
    email: str
    password: str
    laboratistname: str
    Laboratory_License_Number: str
    Equipment_Proefficeincy: str
    Qualifications: str
    Experience: int
    Hospital_Privileges: str
    HR_ID: int
    gender: str
    age: int
    shifttiming: str
    workingdays: str

    class Config:
        orm_mode = True
        
class Laboratoristt(BaseModel):
    laboratorist_ID: int
    email: str
    password: str
    laboratistname: str
    Equipment_Proefficeincy: str
    Qualifications: str
    Experience: int
    Hospital_Privileges: str
    gender: str
    age: int
    shifttiming: str
    workingdays: str

    class Config:
        orm_mode = True        


class patient111(BaseModel):
    patientid: int
    patientname: str
    patientage: str
    patientgender: str
    patientcontact: str
    testname: str
    testdate: str
    testtime: str
    component1: str
    component2: str
    component3: str
    result1: str
    result2: str
    result3: str
    unit1: str
    unit2: str
    unit3: str
    adult1: str
    adult2: str
    adult3: str
    child1: str
    child2: str
    child3: str
    reportid: str
    reportdate: str
    refby: str
    teststatus: str
    laboratoristID: int
      

    class Config:
        orm_mode = True        



  