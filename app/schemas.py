from pydantic import BaseModel

class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str = None
    address: str = None
    city: str = None
    state: str = None
    zip_code: str = None
    country: str = None

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class Customer(CustomerBase):
    customer_id: int

    class Config:
        orm_mode = True

