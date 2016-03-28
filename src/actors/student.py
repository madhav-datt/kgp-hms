class Student(object):
    """Contains details of Student

    Attributes:
        student_ID: An integer to uniquely identify student
        password: A string hashed after adding salt
        name: string
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
        self.address = address
        self.contact_number = contact_number
        self.photograph = photograph
        self.hall_ID = hall_ID
        self.room_no = room_no
        self.room_type = room_type

        # Total dues payable by student
        # total_dues = room_rent + mess_charges + amenities_charges
        self.total_dues = 0.

    # student_ID getter and setter functions
    @property
    def student_ID(self):
        return self._student_ID

    @student_ID.setter
    def student_ID(self, student_ID):
        self._student_ID = student_ID

    # password getter and setter functions
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    # name getter and setter functions
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    # address getter and setter functions
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    # contact_number getter and setter functions
    @property
    def contact_number(self):
        return self._contact_number

    @contact_number.setter
    def contact_number(self, contact_number):
        self._contact_number = contact_number

    # photograph getter and setter functions
    @property
    def photograph(self):
        return self._photograph

    @photograph.setter
    def photograph(self, photograph):
        self._photograph = photograph

    # hall_ID getter and setter functions
    @property
    def hall_ID(self):
        return self._hall_ID

    @hall_ID.setter
    def hall_ID(self, hall_ID):
        self._hall_ID = hall_ID

    # room_no getter and setter functions
    @property
    def room_no(self):
        return self._room_no

    @room_no.setter
    def room_no(self, room_no):
        self._room_no = room_no

    # room_type getter and setter functions
    @property
    def room_type(self):
        return self._room_type

    @room_type.setter
    def room_type(self, room_type):
        self._room_type = room_type

    # total_dues getter function
    @property
    def total_dues(self):
        return self._total_dues

    def calculate_total_dues (self):
        """
        Calculate total dues payable by student
        total_dues = room_rent + mess_charges + amenities_charges
        """

        #TODO: Add based on DB querying functionalities
