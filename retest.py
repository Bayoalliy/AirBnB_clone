#!/usr/bin/python3
import os
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage


bm_init = BaseModel()
bm_init.save()


try:
    bm = BaseModel(**bm_init.to_dict())
except:
    bm = None

if bm is None or bm.id != bm_init.id:
    try:
        bm = BaseModel(bm_init.to_dict())
    except:
        bm = None
print(bm.id == bm_init.id)
print(type(bm.created_at))
print(bm_init)
try:
    print(type(bm.updated_at))
except:
    print("<class 'datetime.datetime'>")
print(bm_init)

print(bm.created_at.year == bm_init.created_at.year)
print(bm.created_at.month == bm_init.created_at.month)
print(bm.created_at.day == bm_init.created_at.day)
print(bm.created_at.hour == bm_init.created_at.hour)
print(bm.created_at.minute == bm_init.created_at.minute)

try:
    print(bm.updated_at.year == bm_init.updated_at.year)
    print(bm.updated_at.month == bm_init.updated_at.month)
    print(bm.updated_at.day == bm_init.updated_at.day)
    print(bm.updated_at.hour == bm_init.updated_at.hour)
    print(bm.updated_at.minute == bm_init.updated_at.minute)
except:
    print("True")
    print("True")
    print("True")
    print("True")
    print("True")


fs = FileStorage()
file_path = "file.json"
try:
    file_path = FileStorage._FileStorage__file_path
except:
    pass
try:
    os.remove(file_path)
except:
    pass
try:
    fs._FileStorage__objects.clear()
except:
    pass
ids = []

# First create
for i in range(1):
    bm = BaseModel()
    bm.updated_at = datetime.utcnow()
    fs.new(bm)
    ids.append(bm.id)

try:
    os.remove(file_path)
except:
    pass
fs.save()
try:
    fs._FileStorage__objects.clear()
except:
    pass
fs.reload()

all_reloaded = fs.all()

if len(all_reloaded.keys()) != len(ids):
    print("Missing after reload 1")

for id in ids:
    if all_reloaded.get(id) is None and all_reloaded.get("{}.{}".format("BaseModel", id)) is None:
        print("Missing 1 {}".format(id))

from models import storage
storage.reload()

# Second create
for i in range(2):
    bm = BaseModel()
    bm.save()
    ids.append(bm.id)
try:
    os.remove(file_path)
except:
    pass
storage.save()
try:
    fs._FileStorage__objects.clear()
except:
    pass
storage.reload()

all_reloaded = storage.all()

if len(all_reloaded.keys()) != len(ids):
    print("Missing after reload 2")

for id in ids:
    if all_reloaded.get(id) is None and all_reloaded.get("{}.{}".format("BaseModel", id)) is None:
        print("Missing 2 {}".format(id))

try:
    os.remove(file_path)
except Exception as e:
    pass
