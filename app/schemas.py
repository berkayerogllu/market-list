from pydantic import BaseModel

# --- KULLANICI ŞEMALARI ---
class UserCreate(BaseModel):
    email: str
    password: str 

class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True

# --- ÜRÜN ŞEMALARI ---
class ProductCreate(BaseModel):
    name: str
    quantity: int
    price: float
    is_bought: bool = False
    # Kullanıcının listesine eklemek için ID'sini istiyoruz
    user_id: int 

class ProductResponse(BaseModel):
    id: int
    name: str
    quantity: int
    price: float
    is_bought: bool
    user_id: int

    class Config:
        from_attributes = True