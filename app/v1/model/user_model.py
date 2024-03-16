import peewee
import datetime

from app.v1.utils.db import db

class User(peewee.Model):
    id = peewee.IntegerField(column_name='id', primary_key=True, null=False)
    username = peewee.CharField(column_name='username', unique=True, index=True, max_length=50, null=False)
    email = peewee.CharField(column_name='email',unique=True, index=True, max_length=150, null=False)
    password = peewee.CharField(column_name='password', max_length=1000, null=True)
    activo = peewee.BooleanField(column_name='activo', null=False, default=True)
    address = peewee.CharField(column_name='address', max_length=250, null=True)
    phone = peewee.CharField(column_name='phone', max_length=9, null=True)
    name = peewee.CharField(column_name='name', max_length=50, null=True)
    lastname = peewee.CharField(column_name='lastname', max_length=50, null=True)
    createAt = peewee.DateTimeField(column_name='createat', default=datetime.datetime.now)


    class Meta:
        database = db
        db_table='user'