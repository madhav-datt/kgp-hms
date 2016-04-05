#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

from __future__ import division
from fpdf import FPDF
import warnings
import time

def print_statement(Hall):
    """
    Print Hall Account statements for specified hall_ID
    """

    pdf = FPDF('P', 'mm', 'A4')
    pdf.set_font('Times', 'B', 14)

    pdf.multi_cell(0, 5, ('Hall Account Statement for Hall: %s', Hall.name))
    pdf.ln()
    pdf.multi_cell(0, 5, ('Mess Account: %s', Hall.mess_account))
    pdf.ln()
    pdf.multi_cell(0, 5, ('Salary Account: %s', Hall.salary_account))
    pdf.ln()
    pdf.multi_cell(0, 5, ('Repair Account: %s', Hall.repair_account))
    pdf.ln()
    pdf.multi_cell(0, 5, ('Rent Account: %s', Hall.rent_account))
    pdf.ln()
    pdf.multi_cell(0, 5, ('Others Account: %s', Hall.others_account))
    pdf.ln()

    # Write generated output file to PDF
    pdf.output(('hall_statement_%s', hall_ID), 'F')

def issue_cheque(name, amount):
    """
    Print salary and payment cheques with worker_ID
    Print hall payment cheques with hall_ID
    """

    pdf = FPDF('P', 'mm', 'A4')
    pdf.set_font('Times', 'B', 14)

    pdf.multi_cell(0, 5, 'Cheque Payment System')
    pdf.ln()
    pdf.multi_cell(0, 5, ('Pay: %s', name))
    pdf.ln()
    pdf.multi_cell(0, 5, ('The amount of: Rs. %s', amount))
    pdf.ln()
    pdf.multi_cell(0, 5, ('Issued on: %s', time.strftime("%d/%m/%Y")))
    pdf.ln()

    # Write generated output file to PDF
    pdf.output(('hall_statement_%s', hall_ID), 'F')

def generate_salary_list(Hall, worker_list):
    """
    Print list of all employees and respective salary details for specified hall
    Take dict of Worker objects as parameter
    """

    pdf = FPDF('P', 'mm', 'A4')
    pdf.set_font('Times', 'B', 14)

    pdf.multi_cell(0, 5, ('Hall Salary List: Hall %s', Hall.hall_ID))
    pdf.ln()

    for key in worker_list:
        if worker_list[key].hall_ID = Hall.hall_ID:
            if row[3] == "M":
                title = "Mess Manager"
                wage = worker_list[key].monthly_salary
            elif row[3] == "C":
                title = "Clerk"
                wage = worker_list[key].monthly_salary
            elif row[3] == "A":
                title = "Attendant"
                wage = worker_list[key].daily_wage

            pdf.multi_cell(0, 5, ('%s: %s (%s) - Rs. %s', worker_list[key].worker_ID,
            worker_list[key].name, title, wage))
            pdf.ln()

    # Write generated output file to PDF
    pdf.output(('hall_salary_%s', hall_ID), 'F')

def print_receipt(Student):
    """
    Print receipts related to specified Student
    Contain all three amounts paid - mess fees, room rent, amenities charge
    """

    pdf = FPDF('P', 'mm', 'A4')
    pdf.set_font('Times', 'B', 14)

    pdf.multi_cell(0, 5, 'Student Dues Payment Receipt')
    pdf.ln()
    pdf.multi_cell(0, 5, ('Student ID: %s', Student.student_ID))
    pdf.ln()
    pdf.multi_cell(0, 5, ('Name: %s', Student.name))
    pdf.ln()
    pdf.multi_cell(0, 5, ('Mess Fees: %s', Student.mess_charge))
    pdf.ln()

    if self.room_type = "S":
        room_rent = db.get("hall", hall_ID, "single_room_rent")
    elif self.room_type = "D":
        room_rent = db.get("hall", hall_ID, "double_room_rent")

    pdf.multi_cell(0, 5, ('Room Rent: %s', room_rent))
    pdf.ln()

    pdf.multi_cell(0, 5, ('Amenities Charge: %s', db.get("hall", self.hall_ID, "amenities_charge")))
    pdf.ln()

    pdf.multi_cell(0, 5, ('Total Amount Paid: %s', Student.total_dues()))
    pdf.ln()

    # Write generated output file to PDF
    pdf.output(('hall_statement_%s', hall_ID), 'F')

def issue_student_admission_letter(Student, body):
    """
    Print letter for Student at time of admission
    Contains details as provided by the Student
    """

    pdf = FPDF('P', 'mm', 'A4')
    pdf.set_font('Times', 'B', 14)

    pdf.multi_cell(0, 5, 'Student Admission Letter')
    pdf.ln()
    pdf.multi_cell(0, 5, ('Name: %s', Student.name))
    pdf.ln()
    pdf.multi_cell(0, 5, ('Address: %s', Student.address))
    pdf.ln()
    pdf.multi_cell(0, 5, ('Contact Number: %s', Student.contact_number))
    pdf.ln()
    pdf.multi_cell(0, 5, ('Hall Allotted: %s', db.get("hall", Student.hall_ID, "name")))
    pdf.ln()
    pdf.multi_cell(0, 5, ('Room Allotted: %s', Student.room_no))
    pdf.ln()
    pdf.ln()
    pdf.multi_cell(0, 5, ('%s', body)
    pdf.ln()

    # Write generated output file to PDF
    pdf.output(('admission_letter_%s', Student.student_ID), 'F')
