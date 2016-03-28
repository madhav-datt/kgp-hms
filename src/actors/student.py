class Student(object):
    """Contains details of Student

    Attributes:
        student_ID: An integer to uniquely identify student
        password: A string hashed after adding salt
        name: string
        gender: string
        address: string
        contact_number: string
        photograph: image
        hall_ID: An integer to identify hall of residence
        room_no: string
        room_type: Either an "S" for single, or a "D" for double room
        total_dues: A float to calculate total amount due by student
    """

    def __init__(self, student_ID, password, name, gender, address,
                contact_number, photograph, hall_ID, room_no, room_type):
        """
        Init Student with details from Admission Letter
        """

        self.student_ID = student_ID
        self.password = password
        self.name = name
        self.gender = gender
        self.address = address
        self.contact_number = contact_number
        self.photograph = photograph
        self.hall_ID = hall_ID
        self.room_no = room_no
        self.room_type = room_type

        # Total dues payable by student
        # total_dues = room_rent + mess_charges + amenities_charges
        self.total_dues = 0.
