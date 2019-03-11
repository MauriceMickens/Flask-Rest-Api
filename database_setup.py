import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    password_hash = Column(String(64))
    name = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False)
    picture = Column(String(100))

    def hash_password(self, password):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'picture': self.picture
        }

# class Contact(Base):
#     __tablename__ = 'contact'
#
#     id = Column(Integer, primary_key=True)
#     contact_title = Column(String(20))
#     contact_first = Column(String(75))
#     contact_middle = Column(String(50))
#     contact_last = Column(String(75))
#     lead_referral_source = Column(String(75))
#     date_of_initial_contact = Column(String(50))
#     title = Column(String(20))
#     company = Column(String(75))
#     industry = Column(String(75))
#     address = Column(String(50))
#     address_street_1 = Column(String(75))
#     address_street_2 = Column(String(75))
#     address_city = Column(String(75))
#     address_state = Column(String(75))
#     address_zip = Column(String(50))
#     address_country = Column(String(75))
#     phone = Column(String(20))
#     email = Column(String(75))
#     status = Column(String(50))
#     website = Column(String(75))
#     linkedIn_profile = Column(String(75))
#     background_info = Column(String(250))
#     sales_rep = Column(String(75))
#     rating = Column(String(50))
#     project_type = Column(String(50))
#     project_description = Column(String(250))
#     budget = Column(String(75))
#     deliverables = Column(String(75))
#
#     @property
#     def serialize(self):
#         """Return object data in easily serializeable format"""
#         return {
#             'id': self.id,
#             'contact_title': self.contact_title,
#             'contact_first': self.contact_first,
#             'contact_middle': self.contact_middle,
#             'contact_last': self.contact_last,
#             'lead_referral_source': self.lead_referral_source,
#             'date_of_initial_contact': self.date_of_initial_contact,
#             'title': self.title,
#             'company': self.company,
#             'industry': self.industry,
#             'address': self.address,
#             'address_street_1': self.address_street_1,
#             'address_street_2': self.address_street_2,
#             'address_city': self.address_city,
#             'address_state': self.address_state,
#             'address_zip': self.address_zip,
#             'address_country': self.address_country,
#             'phone': self.phone,
#             'email': self.email,
#             'status': self.status,
#             'website': self.website,
#             'linkedIn_profile': self.linkedIn_profile,
#             'background_info': self.background_info,
#             'sales_rep': self.sales_rep,
#             'rating': self.rating,
#             'project_type': self.project_type,
#             'project_description': self.project_description,
#             'budget': self.budget,
#             'deliverables': self.deliverables
#         }
#
# class ContactStatus(Base):
#     __tablename__ = 'contact_status'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#
#     @property
#     def serialize(self):
#         """Return object data in easily serializeable format"""
#         return {
#             'name': self.name,
#             'id': self.id
#         }
#
# class Notes(Base):
#     __tablename__ = 'notes'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#
#     @property
#     def serialize(self):
#         """Return object data in easily serializeable format"""
#         return {
#             'name': self.name,
#             'id': self.id
#         }
#
# class Roles(Base):
#     __tablename__ = 'roles'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#
#     @property
#     def serialize(self):
#         """Return object data in easily serializeable format"""
#         return {
#             'name': self.name,
#             'id': self.id
#         }
#
# class TaskStatus(Base):
#     __tablename__ = 'task_status'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#
#     @property
#     def serialize(self):
#         """Return object data in easily serializeable format"""
#         return {
#             'name': self.name,
#             'id': self.id
#         }
#
# class TodoDesc(Base):
#     __tablename__ = 'todo_desc'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#
#     @property
#     def serialize(self):
#         """Return object data in easily serializeable format"""
#         return {
#             'name': self.name,
#             'id': self.id
#         }
#
#
# class TodoType(Base):
#     __tablename__ = 'todo_type'
#
#     name = Column(String(80), nullable=False)
#     id = Column(Integer, primary_key=True)
#     description = Column(String(250))
#     price = Column(String(8))
#     course = Column(String(250))
#     restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
#     restaurant = relationship(Restaurant)
#
#     @property
#     def serialize(self):
#         """Return object dfata in easily serializeable format"""
#         return {
#             'name': self.name,
#             'description': self.description,
#             'id': self.id,
#             'price': self.price,
#             'course': self.course,
#         }
#
# class UserStatus(Base):
#     __tablename__ = 'user_status'
#
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     user = relationship(User)
#
#     @property
#     def serialize(self):
#         """Return object dfata in easily serializeable format"""
#         return {
#             'id': self.id
#         }

engine = create_engine('sqlite:///custom_crm.db')

Base.metadata.create_all(engine)
