from typing import List
from datetime import date
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import uvicorn
import crud, models, schemas
from database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# def get_all_Department():
#     session = Session()
#     employees = session.query(models.Department).all()
#     session.close()
#     return employees

@app.post("/viewdetails/", response_model=schemas.DepartmentSchema)
def create_user(user: schemas.DepartmentSchema, db: Session = Depends(get_db)):
   
    return crud.create_dept(db=db, user=user)


# @app.post("/postusers/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)

# @app.get('/getdepts')
# def read_employees():
#     employees = get_all_Department()
#     return employees

@app.get("/getusers/", response_model=List[schemas.User])
def read_users( db: Session = Depends(get_db)):
    users = crud.get_users(db)
    if users is None:
        raise HTTPException(status_code=404, detail="User not found")
    return users

@app.post("/appointmensats/", response_model=schemas.AppointmentSchema)
def create_appointment(user: schemas.AppointmentSchema,db: Session = Depends(SessionLocal)):
    db_appt = crud.create_appointment(db, user)
    return db_appt

@app.post("/testappointment/", response_model=schemas.AppointmentSchema)
def create_user(user: schemas.AppointmentSchema, db: Session = Depends(get_db)):
    db_user = crud.create_appointment(db, user)
    if db_user:
        raise HTTPException(status_code=400, detail="something went wrong ")
    return crud.create_appointment(db=db, user=user)


@app.get("/gettimesbydates/{doctorid}/{date}", response_model=List[schemas.Visits])
def get_time_by_date(doctorid:int, date:date,db: Session = Depends(get_db)):
    db_visit = crud.get_time_by_dates(db,doctorid=doctorid,date=date)
    if db_visit is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_visit


@app.get("/getdoctorsbyid/{doctorid}", response_model=List[schemas.Doctor2schema])
def get_time_by_date(doctorid:int, db: Session = Depends(get_db)):
    db_visit = crud.fetch_doctor2by_id(db,docid=doctorid)
    if db_visit is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_visit

# @app.get("/fetchdoctorsbyid/{Docid}", response_model=List[schemas.Doctor2schema])
# def fetchdoctorsbydid( docid :int ,db: Session = Depends(get_db)):
#     doc_data = crud.fetch_doctor2by_id(db,1)
#     if doc_data is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return doc_data

@app.get("/fetchalldoctorsbyspecialization/{specialty}", response_model=List[schemas.Doctor2schema])
def fetchalldoctorsbyspecs( specialty:str,db: Session = Depends(get_db)):
    doc_data = crud.fetch_alldoctors_byspecs(db,specialty)
    if doc_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    return doc_data



@app.get("/fetchpatientsinformation/{patientid}", response_model=schemas.Patient2schema)
def get_time_by_date(patientid:int, db: Session = Depends(get_db)):
    db_visit = crud.fetch_patientInformation(db,patinetid=patientid)
    if db_visit is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return db_visit

@app.put("/updatepatientsinformation/{patientid}", response_model=schemas.Patient2schema)
def update_patient_information(patientid: int, updated_patient_info: schemas.Patient2schema, db: Session = Depends(get_db)):
    # Update the patient information in the database
    db_patient = crud.update_patient_information(db, patientid=patientid, updated_patient_info=updated_patient_info)
    
    # Check if the patient information was found and updated
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient information not found")
    
    # Return the updated patient information
    return db_patient


@app.put("/updatetestinfostatus/{patientid}", response_model=schemas.patient111)
def update_patient_information(patientid: int, updated_status_info: schemas.patient111, db: Session = Depends(get_db)):
    # Update the patient information in the database
    db_patient = crud.update_status_information(db, patientid=patientid, updated_status_info=updated_status_info)
    
    # Check if the patient information was found and updated
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient information not found")
    
    # Return the updated patient information
    return db_patient

@app.put("/updateteststatus/{test_id}"  , response_model=schemas.patient111)
def update_test_status_endpoint(patientid: int, new_status: str, db: Session = Depends(get_db)):
   
    test = crud.update_test_status(db, patientid= patientid, new_status=new_status )
     
     
    if test is None:
        raise HTTPException(status_code=404, detail="Patient information not found")
        
        
        
        
        
@app.get("/getallhospitals/", response_model=List[schemas.HospitalSchema])
def read_users( db: Session = Depends(get_db)):
    users = crud.get_hospitals(db)
    if users is None:
        raise HTTPException(status_code=404, detail="User not found")
    return users





@app.get("/getallLoginn/", response_model=List[schemas.Loginn])
def fetch_login( db: Session = Depends(get_db)):
    db_log = crud.get_Loginn(db)
    if db_log is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_log

@app.get("/getallLaboratorist/", response_model=List[schemas.Laboratorist])
def get_laboratorsit( db: Session = Depends(get_db)):
    db_laboratorist = crud.get_Laboratorist(db)
    if db_laboratorist is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_laboratorist

@app.get("/gethania/", response_model=List[schemas.hania])
def get_haniaaa( db: Session = Depends(get_db)):
    db_hania = crud.get_hania(db)
    if db_hania is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_hania

@app.get("/getallLaboratoristt/", response_model=List[schemas.Laboratoristt])
def fetch_laboratoristt( db: Session = Depends(get_db)):
    db_laboratoristt = crud.get_Laboratoristt(db)
    if db_laboratoristt is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_laboratoristt

@app.get("/getallpatient00/", response_model=List[schemas.patient00])
def fetch_patient00( db: Session = Depends(get_db)):
    db_patient00 = crud.get_patient00(db)
    if db_patient00 is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_patient00

@app.get("/getallpatient11/", response_model=List[schemas.patient111])
def fetch_patient11( db: Session = Depends(get_db)):
    db_patient11 = crud.get_patient11(db)
    if db_patient11 is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_patient11

#correctttt
@app.get("/logininfo/{email}", response_model=schemas.Laboratoristt)
def fetch_laboratoristt( email:str,db: Session = Depends(get_db)):
    db_laboratoristt = crud.getlogininfo(db,email=email)
    if db_laboratoristt is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_laboratoristt

#showing corect laboid, #allpatients #correct fetching all test
@app.get("/fetchpatientreportinfo/{laboratoristID}", response_model=list[schemas.patient111])
def fetch_ppp(laboratoristID:str,db: Session = Depends(get_db)):
    db_laboratoristttt = crud.getppppinfo(db,laboratoristID=laboratoristID)
    if db_laboratoristttt is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_laboratoristttt

#patientreport
@app.get("/fetchpatientreport/{reportid}", response_model=schemas.patient111)
def fetch_report( reportid:str,db: Session = Depends(get_db)):
    db_report = crud.getpatientreport(db,reportid=reportid)
    if db_report is None:
        raise HTTPException(status_code=404, detail="Report is not available")
    return db_report

@app.get("/completed-tests/", response_model=list[schemas.patient111])
def fetch_completed_tests(db: Session = Depends(get_db)):
    completed_tests = crud.get_completed_tests(db)
    if completed_tests is None:
        raise HTTPException(status_code=404, detail="No completed tests found")
    return completed_tests

#correct fetching of completed tests
@app.get("/completed-tests-patientrepot/{laboratoristID}", response_model=list[schemas.patient111])
def fetch_completed_test_patient(laboratoristID:str,db: Session = Depends(get_db)):
    db_comp = crud.getcompletedpatientreport(db,laboratoristID=laboratoristID)
    if db_comp is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_comp
#correct fething of remaining test
@app.get("/remaining-tests-patientrepot/{laboratoristID}", response_model=list[schemas.patient111])
def fetch_remaining_test_patient(laboratoristID:str,db: Session = Depends(get_db)):
    db_comp = crud.getremainingpatientreport(db,laboratoristID=laboratoristID)
    if db_comp is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_comp

@app.get("/remaining-tests/", response_model=list[schemas.patient111])
def fetch_remaining_tests(db: Session = Depends(get_db)):
    remaining_tests = crud.get_remaining_tests(db)
    if remaining_tests is None:
        raise HTTPException(status_code=404, detail="No remaining tests found")
    return remaining_tests

# @app.get("/getusersbyid/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items

#if __name__ == "__main__":
 #    uvicorn.run(app, host="0.0.0.0", port=8000)
 
 
 
 