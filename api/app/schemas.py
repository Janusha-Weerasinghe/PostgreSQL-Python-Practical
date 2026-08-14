from pydantic import BaseModel, ConfigDict, Field


class StudentBase(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    age: int | None = Field(
        default=None,
        ge=0,
        le=150
    )

    email: str

    score: float | None = Field(
        default=None,
        ge=0,
        le=100
    )


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100
    )

    age: int | None = Field(
        default=None,
        ge=0,
        le=150
    )

    email: str | None = None

    score: float | None = Field(
        default=None,
        ge=0,
        le=100
    )


class StudentResponse(StudentBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )