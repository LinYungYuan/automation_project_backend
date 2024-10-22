from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, services
from app.api import deps

router = APIRouter()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(deps.get_db)):
    user = services.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/messages/", response_model=schemas.Message)
def create_message(message: schemas.MessageCreate, db: Session = Depends(deps.get_db), current_user: User = Depends(deps.get_current_user)):
    return services.create_message(db, message, current_user)