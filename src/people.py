# people.py

#from datetime import datetime
from flask import abort, make_response

from config import db
from models import People, people_schema, peoples_schema

# def get_timestamp():
#     return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# PEOPLE = {
#     "DE-JARGET_OSCAR": {
#         "unique_reference": "DE-JARGET_OSCAR",
#         "lname1": "De-Jarget",
#         "lname2": "Jarget",
#         "fname1": "Oscar",
#         "fname2": "",
#         "email1": "oscar@gmail.com",
#         "email2": "",
#         "address1": "MSF74, pnr",
#         "address2": "",
#         "phone1": "05 14 87 59 43",
#         "phone2": "",
#         "sex": "F",
#         "timestamp": get_timestamp(),
#     },
#     "KENT_CLARK": {
#         "unique_reference": "KENT_CLARK",
#         "lname1": "Kent",
#         "lname2": "",
#         "fname1": "Clark",
#         "fname2": "Balist",
#         "email1": "ckent@gmail.com",
#         "email2": "ckent2@gmail.com",
#         "address1": "MSFKENT, pnr",
#         "address2": "MSFKENT, paris",
#         "phone1": "05 14 87 59 47",
#         "phone2": "05 14 87 59 22",
#         "sex": "M",
#         "timestamp": get_timestamp(),
#     },
#     "LENNON_JOHN": {
#         "unique_reference": "LENNON_JOHN",
#         "lname1": "Lennon",
#         "lname2": "",
#         "fname1": "John",
#         "fname2": "Blinker",
#         "email1": "jleonon@gmail.com",
#         "email2": "",
#         "address1": "MSF LENNONG, pnr",
#         "address2": "",
#         "phone1": "05 14 87 59 77",
#         "phone2": "",
#         "sex": "M",
#         "timestamp": get_timestamp(),
#     },
#     "LENNON_MARTHA": {
#         "unique_reference": "LENNON_MARTHA",
#         "lname1": "Lennon",
#         "lname2": "",
#         "fname1": "Martha",
#         "fname2": "",
#         "email1": "mleonon@gmail.com",
#         "email2": "",
#         "address1": "MSF LENNONG, pnr",
#         "address2": "",
#         "phone1": "05 14 87 59 78",
#         "phone2": "",
#         "sex": "F",
#         "timestamp": get_timestamp(),
#     },
# }

def read_all():
    #return list(PEOPLE.values())
    peoples = People.query.all()
    return peoples_schema.dump(peoples)

def read_one_by_unique_reference(unique_reference):
    # unique_reference = unique_reference.upper()
    # if unique_reference in PEOPLE:
    #     return PEOPLE[unique_reference]
    # else:
    #     abort(
    #         404, f"Person with unique_reference {unique_reference} not found"
    #     )
    unique_reference = unique_reference.upper()
    people = People.query.filter(People.unique_reference == unique_reference).one_or_none()
    if people is not None:
        return people_schema.dump(people)
    else:
        abort(404, f"Person with unique_reference {unique_reference} not found")


def read_all_by_lname1(lname1):
    print("lname1",lname1)

    lname1 = lname1.upper()

    peoples = People.query.filter(People.lname1 == lname1).all()
    print("peoples",peoples)
    if peoples is not None:
        return peoples_schema.dump(peoples)
    else:
        abort(
            404, f"Person(s) with lname1 {lname1} not found"
        )

# def read_all_by_lname1(lname1):
#     #get each unique_reference in the PEOPLE data structure
#     # separe lname1 from fname1
#     #compare lname1 to the one given
#     # if same add it to another structure
#     ANSWER = {}
#     lname1 = lname1.upper()
#     for p in PEOPLE:
#         name = PEOPLE[p].get('lname1')
#         unique_reference = PEOPLE[p].get('unique_reference')
#         # if unique_reference.startswith(lname1):
#         #     ANSWER[unique_reference] = p
#         if name.upper() == lname1:
#             ANSWER[unique_reference] = PEOPLE[p]
#     if not ANSWER:
#         #le dictionnaire est toujours vide 
#         #(RAPPEL: a empty string/dict is evaluate to FALSE in python)
#         abort(
#             404, f"Person(s) with lname1 {lname1} not found"
#         )
#     else:
#         return list(ANSWER.values())

def construct_unique_reference(lname1, fname1):
    if not lname1 or not lname1.strip():
        abort(
            406,
            f"Person with last name empty cannot exists",
        )
    else:
        lname1=lname1.strip().replace(" ","_").upper()
        #lname1=lname1.replace(" ","_")
        #fname1 = people.get("fname1", "").upper()
        fname1 = fname1.strip().replace(" ","_").upper()
         
        return lname1 + '_' + fname1

def create(people):
    lname1 = people.get("lname1").upper()
    fname1 = people.get("fname1", "").upper()
    #si le nom est vide ou contient juste un espace
    # if not lname1 or not lname1.strip(): 
    #     abort(
    #         406,
    #         f"Person with last name empty cannot exists",
    #     )
    # else:
        # lname1=lname1.strip()
        # lname1=lname1.replace(" ","_")
        # fname1 = people.get("fname1", "").upper()
        # fname1 = fname1.strip().replace(" ","_")
        # unique_reference= lname1 + '_' + fname1
    unique_reference = construct_unique_reference(lname1,fname1)
    existing_people = People.query.filter(people.unique_reference == unique_reference).one_or_none()

    if existing_people is None:
        people.unique_reference = unique_reference
        people.lname1 = lname1
        people.fname1 = fname1
        
        new_people = people_schema.load(people, session=db.session)
        db.session.add(new_people)
        db.session.commit()
        return people_schema.dump(new_people), 201
    else:
        abort(
            406,
            f"Person with last name {lname1} (and first name {fname1}) already exists",
        )

    

# def create(person):
#     lname1 = person.get("lname1").upper()

#     #si le nom est vide ou contient juste un espace
#     if not lname1 or not lname1.strip(): 
#         abort(
#             406,
#             f"Person with last name empty cannot exists",
#         )
#     else:
#         lname1=lname1.strip()
#         lname1=lname1.replace(" ","_")
#         fname1 = person.get("fname1", "").upper()
#         fname1 = fname1.strip().replace(" ","_")
#         unique_reference= lname1 + '_' + fname1
#         #unique_reference = unique_reference.upper()

#         if unique_reference and unique_reference not in PEOPLE:
#             PEOPLE[unique_reference] = {
#                 "unique_reference": unique_reference,
#                 "lname1": lname1,
#                 "lname2": person.get("lname2", ""),
#                 "fname1": fname1,
#                 "fname2": person.get("fname2", ""),
#                 "email1": person.get("email1", ""),
#                 "email2": person.get("email2", ""),
#                 "address1": person.get("address1", ""),
#                 "address2": person.get("address2", ""),
#                 "phone1": person.get("phone1", ""),
#                 "phone2": person.get("phone2", ""),
#                 "sex": person.get("sex", ""),
#                 "timestamp": get_timestamp(),
#             }
#             return PEOPLE[unique_reference], 201
#         else:
#             abort(
#                 406,
#                 f"Person with last name {lname1} (and first name {fname1}) already exists",
#             )

def update(unique_reference, people):
    unique_reference = unique_reference.upper()
    existing_people = People.query.filter(people.unique_reference == unique_reference).one_or_none()

    if existing_people:
        update_people = people_schema.load(people, session=db.session)
        new_reference = construct_unique_reference(update_people.lname1, update_people.fname1)
        if existing_people.unique_reference != new_reference : 
            existing_people.unique_reference = new_reference
            existing_people.lname1 = update_people.lname1.upper()
            existing_people.fname1 = update_people.fname1.upper()
        if update_people.lname2: existing_people.lname2 = update_people.lname2
        if update_people.fname2: existing_people.fname2 = update_people.fname2
        if update_people.email1: existing_people.email1 = update_people.email1
        if update_people.email2: existing_people.email2 = update_people.email2
        if update_people.addres1: existing_people.addres1 = update_people.addres1
        if update_people.addres2: existing_people.addres2 = update_people.addres2
        if update_people.phone1: existing_people.phone1 = update_people.phone1
        if update_people.phone2: existing_people.phone2 = update_people.phone2
        if update_people.sex: existing_people.sex = update_people.sex
        db.session.merge(existing_people)
        db.session.commit()
        return people_schema.dump(existing_people), 201
    else:
        abort(
            404,
            f"Person with unique_reference {unique_reference} not found"
        )

# def update(unique_reference, person):
#     unique_reference = unique_reference.upper()
#     if unique_reference in PEOPLE:
#         PEOPLE[unique_reference]["lname1"] = person.get("lname1", PEOPLE[unique_reference]["lname1"])
#         PEOPLE[unique_reference]["lname2"] = person.get("lname2", PEOPLE[unique_reference]["lname2"])
#         PEOPLE[unique_reference]["fname1"] = person.get("fname1", PEOPLE[unique_reference]["fname1"])
#         PEOPLE[unique_reference]["fname2"] = person.get("fname2", PEOPLE[unique_reference]["fname2"])
#         PEOPLE[unique_reference]["email1"] = person.get("email1", PEOPLE[unique_reference]["email1"])
#         PEOPLE[unique_reference]["email2"] = person.get("email2", PEOPLE[unique_reference]["email2"])
#         PEOPLE[unique_reference]["address1"] = person.get("address1", PEOPLE[unique_reference]["address1"])
#         PEOPLE[unique_reference]["address2"] = person.get("address2", PEOPLE[unique_reference]["address2"])
#         PEOPLE[unique_reference]["phone1"] = person.get("phone1", PEOPLE[unique_reference]["phone1"])
#         PEOPLE[unique_reference]["phone2"] = person.get("phone2", PEOPLE[unique_reference]["phone2"])
#         PEOPLE[unique_reference]["sex"] = person.get("sex", PEOPLE[unique_reference]["sex"])
#         PEOPLE[unique_reference]["timestamp"] = get_timestamp()
#         return PEOPLE[unique_reference]
#     else:
#         abort(
#             404,
#             f"Person with unique_reference {unique_reference} not found"
#         )

def delete(unique_reference):
    unique_reference = unique_reference.upper()
    existing_people = People.query.filter(People.unique_reference == unique_reference).one_or_none()

    if existing_people:
        db.session.delete(existing_people)
        db.session.commit()
        return make_response(
            f"{unique_reference} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with unique reference {unique_reference} not found"
        )

# def delete(unique_reference):
#     unique_reference = unique_reference.upper()
#     if unique_reference in PEOPLE:
#         del PEOPLE[unique_reference]
#         return make_response(
#             f"{unique_reference} successfully deleted", 200
#         )
#     else:
#         abort(
#             404,
#             f"Person with unique reference {unique_reference} not found"
#         )