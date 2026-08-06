import os

from flask import Flask
from flask import jsonify
from flask import request

from flask_cors import CORS

from db import get_connection
from db import initialize_database

app = Flask(__name__)

CORS(app)


@app.route("/")

def home():

    return jsonify({
        "message":"Docker Workshop Backend Running"
    })


@app.route("/health")

def health():

    return jsonify({
        "status":"UP"
    })


@app.route("/students",methods=["GET"])

def get_students():

    conn=get_connection()

    cursor=conn.cursor(dictionary=True)

    cursor.execute("select * from students")

    students=cursor.fetchall()

    cursor.close()

    conn.close()

    return jsonify(students)


@app.route("/students",methods=["POST"])

def add_student():

    data=request.json

    conn=get_connection()

    cursor=conn.cursor()

    cursor.execute(

        """

        INSERT INTO students(name,email,course)

        VALUES(%s,%s,%s)

        """,

        (

            data["name"],

            data["email"],

            data["course"]

        )

    )

    conn.commit()

    cursor.close()

    conn.close()

    return jsonify({

        "message":"Student Added Successfully"

    })


@app.route("/students/<int:id>",methods=["PUT"])

def update_student(id):

    data=request.json

    conn=get_connection()

    cursor=conn.cursor()

    cursor.execute(

        """

        UPDATE students

        SET

        name=%s,

        email=%s,

        course=%s

        WHERE id=%s

        """,

        (

            data["name"],

            data["email"],

            data["course"],

            id

        )

    )

    conn.commit()

    cursor.close()

    conn.close()

    return jsonify({

        "message":"Student Updated"

    })


@app.route("/students/<int:id>",methods=["DELETE"])

def delete_student(id):

    conn=get_connection()

    cursor=conn.cursor()

    cursor.execute(

        "DELETE FROM students WHERE id=%s",

        (id,)

    )

    conn.commit()

    cursor.close()

    conn.close()

    return jsonify({

        "message":"Student Deleted"

    })


if __name__=="__main__":

    initialize_database()

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )