import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendacerealtime-b58f7-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "01":
    {
        "name":"Priyanka Awaje",
        "major":"Data Analytics",
        "starting_year":2019,
        "total_attendance":10,
        "performance":"O",
        "year":4,
        "Last_attendance_time":"2023-08-14 10:30:00"

    },

    "02":
    {
        "name":"Aniket Gajare",
        "major":"Automobile",
        "starting_year":2021,
        "total_attendance":7,
        "performance":"A",
        "year":2,
        "Last_attendance_time":"2023-08-14 04:30:00"

    },

    "03":
    {
        "name":"Harikrishnan Nair",
        "major":"Data Science",
        "starting_year":2020,
        "total_attendance":9,
        "performance":"A",
        "year":3,
        "Last_attendance_time":"2023-08-14 05:50:00"

    },

    "04":
    {
        "name":"Priya Randive",
        "major":"Finance",
        "starting_year":2021,
        "total_attendance":8,
        "performance":"A",
        "year":2,
        "Last_attendance_time":"2023-08-13 09:40:00"

    },

    "05":
    {
        "name":"Mayuri Pawar",
        "major":"Com Science",
        "starting_year":2022,
        "total_attendance":6,
        "performance":"B",
        "year":1,
        "Last_attendance_time":"2023-08-08 11:35:00"

    },

    "06":
    {
        "name":"Tanmay Alwe",
        "major":"Fine Arts",
        "starting_year":2019,
        "total_attendance":7,
        "performance":"B",
        "year":4,
        "Last_attendance_time":"2023-08-12 06:25:00"

    },

    "07":
    {
        "name":"Ritesh Odel",
        "major":"IT",
        "starting_year":2020,
        "total_attendance":8,
        "performance":"A",
        "year":3,
        "Last_attendance_time":"2023-08-10 02:10:00"

    },

    "08":
    {
        "name":"Kartik Iyer",
        "major":"Commerce",
        "starting_year":2021,
        "total_attendance":9,
        "performance":"B",
        "year":2,
        "Last_attendance_time":"2023-08-11 08:20:00"

    },

    "10":
    {
        "name":"Geetha Nair",
        "major":"Science",
        "starting_year":2019,
        "total_attendance":10,
        "performance":"C",
        "year":4,
        "Last_attendance_time":"2023-08-14 12:30:00"

    },

    "998":
    {
        "name":"Elon Musk",
        "major":"Robotics",
        "starting_year":2019,
        "total_attendance":5,
        "performance":"A",
        "year":4,
        "Last_attendance_time":"2023-08-06 10:30:00"

    },

}

for key, value in data.items():
    ref.child(key).set(value) 