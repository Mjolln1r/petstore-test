from pydantic import BaseModel, validator, field_validator


class Pet(BaseModel):
    id: int
    category: dict
    mail: str


@field_validator('mail')
def check_mail(cls, mail):
    if '@' in mail:
        return mail
    else:
        print('not @ in mail')
