from pydantic import BaseModel, field_validator


class Post(BaseModel):
    """Class representing a post."""
    userId: int
    id: int
    title: str
    body: str

    @field_validator('title', 'body')
    def validate_length(cls, field: str):

        """Validate title and body according to the business requirements:
        - Title and Body should not be empty.
        - Title and Body should not exceed 2000 characters.
        - Title and Body should not be less than 2 characters"""

        if not field:
            raise ValueError(f'{field.name} should not be empty')
        elif len(field) <= 1:
            raise ValueError(f'{field.name} must be at least 2 characters long')
        elif len(field) > 2000:
            raise ValueError(f'{field.name} must not exceed 2000 characters')
        return field

    @field_validator('id')
    def validate_id_field(cls, field: int):

        """Validate id and userId according to the business requirements:
        - id and userId should not be 0 or empty.
        - userId should not be greater than 100."""

        if not field:
            raise ValueError(f'Id should not be 0')
        elif field > 100:
            raise ValueError(f'Id must not be greater than 100')
        return field

    @field_validator('userId')
    def validate_user_id_field(cls, field: int):
        """Validate userId according to the business requirements:
        - userId should not be 0 or empty.
        - userId should not be greater than 10."""
        if not field:
            raise ValueError(f'UserId should not be 0')
        elif field > 10:
            raise ValueError(f'UserId must be less than or equal to 10')
