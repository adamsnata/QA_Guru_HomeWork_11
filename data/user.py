import dataclasses


@dataclasses.dataclass
class User():
    f_name: str
    l_name: str
    email: str
    gender: str
    mobile: str
    day_of_birth: int
    month_of_birth: str
    year_of_birth: int
    subject: str
    hobbie: str
    picture_name: str
    address: str
    state: str
    city: str
