from sqlalchemy import Boolean, CheckConstraint, Column, Date, Float, ForeignKey, Integer, String, Time, UniqueConstraint
from sqlalchemy.orm import relationship

from database import Base

class Location(Base):
    __tablename__ = 'Dloc'

    Locid = Column(Integer, primary_key=True)
    locname = Column(String)

class Department(Base):
    __tablename__ = 'department'

    DEPTNO = Column(Integer, primary_key=True)
    DNAME = Column(String)
    Locid = Column(Integer, ForeignKey('Dloc.Locid'))
    
    location = relationship('Location', backref='departments')


class Appointment(Base):
    __tablename__ = "appointment"

    appointment_id = Column(Integer, primary_key=True, index=True)
    appointment_date = Column(Date)
    appointment_time = Column(Time)
    patient_name = Column(String(100), index=True)
    patient_age = Column(Integer, default=0)
    additional_information = Column(String(255), index=True)

    __table_args__ = (
        CheckConstraint('patient_age >= 0', name='chk_patient_age'),
    )

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
    
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(255), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class Doctor(Base):
    __tablename__ = "doctor"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    specialization = Column(String(255), index=True)

    # visits = relationship('Visits', backref='doctor')

class Patient(Base):
    __tablename__ = "patient"

    patientid = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    email = Column(String(255), index=True)
    gender = Column(String(50), index=True)
    age = Column(Integer, index=True)
    address = Column(String(255), index=True)
    phone = Column(String(50), index=True)
    region = Column(String(255), index=True)
    dateofbirth = Column(Date, index=True)

    Visits = relationship('Visits', backref='patient')
    
class Visits(Base):
    __tablename__ = "visits"

    visitid = Column(Integer, primary_key=True, index=True)
    patientid = Column(Integer, ForeignKey("patient.patientid"))
    doctorid = Column(Integer, ForeignKey("doctor.id"))
    dateofvisit = Column(Date, index=True)
    timeofvisit = Column(Time, index=True)

    Patient = relationship("Patient", back_populates="Visits")
    Doctor = relationship('Doctor', backref='Visits')



class Doctor2model(Base):
    __tablename__ = "DOCTOR2"

    DoctorID = Column(Integer, primary_key=True)
    DoctorAge = Column(Integer)
    DoctorName = Column(String(100))
    Descriptions = Column(String(100))
    ExperienceInYears = Column(Float)
    PatientDealt = Column(Integer)
    ShiftStart = Column(Time)
    ShiftEnd = Column(Time)
    Specialty = Column(String(100))
    Designation = Column(String(100))
    Rating = Column(String(100))

class LoginModels(Base):
    __tablename__ = "LoginInfo"
    EmailAddress = Column(String(500),  primary_key=True)
    Passwords = Column(String(500))
    


class Patient2Model(Base):
    __tablename__ = "Patient2"
    PatientID = Column(Integer, primary_key=True)
    FullName = Column(String(255))
    Age = Column(String(50))
    Gender = Column(String(10))
    HomeAdress= Column(String(255))
    ContactInformation = Column(String(255))
    EmergencyContact = Column(String(255))

    class Config:
        orm_mode = True
        
class PatientNewForUpdate(Base):
    __tablename__ = "patient11"
    patientid = Column(Integer, primary_key=True)
    teststatus = Column(String(255))
    

    class Config:
        orm_mode = True
          

class Hospital(Base):
    __tablename__ = "Hospital"
    hospital_ID = Column(Integer, primary_key=True)
    name = Column(String(255))
    address = Column(String(255))
    location = Column(String(255))
    city = Column(String(255))
   
    Department23 = relationship("Department23", back_populates="Hospital")
    
    class Config:
        orm_mode = True
        

class Department23(Base):
    __tablename__ = "Departments"
    deptID = Column(Integer, primary_key=True)
    deptName = Column(String(255))
    hospital_id = Column(Integer, ForeignKey("Hospital.hospital_ID"))
    
    Hospital = relationship("Hospital", back_populates="Department23")

   
    class Config:
        orm_mode = True

class hania(Base):
    __tablename__ = "hania"
    ID = Column(Integer, primary_key=True)
    
    class Config:
        orm_mode = True




class Laboratorist(Base):
    __tablename__ = "Laboratorist"
    laboratorist_ID = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255))
    password = Column(String(255))
    laboratistname = Column(String(255))
    Equipment_Proefficeincy = Column(String(255))
    Qualifications = Column(String(255))
    Experience = Column(Integer)
    Hospital_Privileges = Column(String(255))
    gender = Column(String(255))
    age = Column(Integer)
    shifttiming = Column(String(255))
    workingdays = Column(String(255))
    
    class Config:
        orm_mode = True





class Laboratoristt(Base):
    __tablename__ = "Laboratoristtt"
    laboratorist_ID = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255))
    password = Column(String(255))
    laboratistname = Column(String(255))
    Equipment_Proefficeincy = Column(String(255))
    Qualifications = Column(String(255))
    Experience = Column(Integer)
    Hospital_Privileges = Column(String(255))
    gender = Column(String(255))
    age = Column(Integer)
    shifttiming = Column(String(255))
    workingdays = Column(String(255))
   
    
 
    
#laboratist login no more
class Loginn(Base):
    __tablename__ = "Loginn"
    logID = Column(Integer, primary_key=True)
    email = Column(String(255))
    password = Column(String(255)) 
    name = Column(String(255)) 
    
    class Config:
        orm_mode = True
        
class patient00(Base):
    __tablename__ = "patient00"
    patientid = Column(Integer, primary_key=True)
    patientname = Column(String(255))
    patientage = Column(Integer)
    patientgender = Column(String(255))
    patientcontact = Column(String(255))
    testdate = Column(String(255))
    testtime = Column(String(255))
    testname = Column(String(255))
      

    class Config:
        orm_mode = True
    


    
class patient111(Base):
    __tablename__ = "patient111"  
    patientid = Column(Integer, primary_key=True)
    patientname = Column(String(255))
    patientage = Column(String(255))
    patientgender = Column(String(255))
    patientcontact = Column(String(255))
    testname = Column(String(255))
    testdate = Column(String(255))
    testtime = Column(String(255))
    component1 = Column(String(255))
    component2 = Column(String(255))
    component3 = Column(String(255))
    result1 = Column(String(255))
    result2 = Column(String(255))
    result3 = Column(String(255))
    unit1 = Column(String(255))
    unit2 = Column(String(255))
    unit3 = Column(String(255))
    adult1 = Column(String(255))
    adult2 = Column(String(255))
    adult3 = Column(String(255))
    child1 = Column(String(255))
    child2 = Column(String(255))
    child3 = Column(String(255))
    reportid = Column(String(255))
    reportdate = Column(String(255))
    refby = Column(String(255))
    teststatus = Column(String(255)) 
    laboratoristID = Column(Integer)
      
      
    class Config:
        orm_mode = True
        