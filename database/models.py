from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True, nullable=False)
    description = Column(String(255), index=True, nullable=False)
    
    users = relationship("User", back_populates="role")
    
class MemberShip(Base):
    __tablename__ = "memberships"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True, nullable=False)
    description = Column(String(255), index=True, nullable=False)
    
    users = relationship("User", back_populates="membership")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    fullname = Column(String(100), index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False, index=True)
    membership_id = Column(Integer, ForeignKey("memberships.id"), nullable=False, index=True)
    
    role = relationship("Role", back_populates="users")
    membership = relationship("MemberShip", back_populates="users")
    pets = relationship("Pet", back_populates="user")

class PetType(Base):
    __tablename__ = "petstype"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True, nullable=False)
    description = Column(String(255), index=True, nullable=False)
    
    pets = relationship("Pet", back_populates="pet_type")

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True, nullable=False)
    age = Column(String(50), index=True, nullable=False)
    pet_type_id = Column(Integer, ForeignKey("petstype.id"), nullable=False)
    avaliability = Column(Integer, index=True, default=1, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    
    user = relationship("User", back_populates="pets")
    pet_type = relationship("PetType", back_populates="pets")
    first_matchs = relationship("Match", foreign_keys='Match.first_pet_id', back_populates="first_pet")
    second_matchs = relationship("Match", foreign_keys='Match.second_pet_id', back_populates="second_pet")

class Match(Base):
    __tablename__ = "matchs"

    first_pet_id = Column(Integer, ForeignKey("pets.id"), primary_key=True, nullable=False)
    second_pet_id = Column(Integer, ForeignKey("pets.id"), primary_key=True, nullable=False)
    
    first_pet = relationship("Pet", foreign_keys=[first_pet_id], back_populates="first_matchs")
    second_pet = relationship("Pet", foreign_keys=[second_pet_id], back_populates="second_matchs")

    __table_args__ = (PrimaryKeyConstraint('first_pet_id', 'second_pet_id', name='match_pk'),)