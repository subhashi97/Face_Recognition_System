import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "database_Link"
})

ref = db.reference('Members')

data = {
    "321856":
        {
            "name": "Subhashini Lakshani",
            "major": "S_Officer",
            "starting_year": 2017,
            "total_attendance": 2,
            "standing": "G",
            "year": 6,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "540153":
        {
            "name": "Vishmi Taniya",
            "major": "C_Attacker",
            "starting_year": 2019,
            "total_attendance": 5,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "845108":
        {
            "name": "Gayan Pradeepa",
            "major": "S_Maintainer",
            "starting_year": 2020,
            "total_attendance": 5,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "326748":
        {
            "name": "Piyumi Nilmini",
            "major": "S_Engineer",
            "starting_year": 2016,
            "total_attendance": 8,
            "standing": "G",
            "year": 7,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "430547":
        {
            "name": "Lakindu Dilshan ",
            "major": "O_Engineer",
            "starting_year": 2016,
            "total_attendance": 5,
            "standing": "G",
            "year": 7,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "328972":
        {
            "name": "Pramila Nuwan",
            "major": "S_Engineer",
            "starting_year": 2017,
            "total_attendance": 8,
            "standing": "G",
            "year": 6,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "276328":
        {
            "name": "Umesh Gayashan",
            "major": "O_Engineer",
            "starting_year": 2017,
            "total_attendance": 5,
            "standing": "G",
            "year": 6,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)


