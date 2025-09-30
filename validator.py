from pydantic import BaseModel, Field, computed_field,field_validator
from typing import Literal, Annotated,Dict
from config.city import tier_1_cities,tier_2_cities


class user(BaseModel):
    age: Annotated[int,Field(...,gt=0,lt=120,description="Age of user")]
    weight: Annotated[int,Field(...,gt=0,description="weight of user")]
    height: Annotated[int,Field(...,gt=0,description="Height of user")]
    income_lpa:Annotated[float,Field(...,gt=0,description="Income of user in lpa")]
    city:Annotated[str,Field(...,description="Enter city")]
    smoker:Annotated[bool,Field(...,description="Use smokes or not")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the user')]
    @computed_field
    @property
    def bmi(self)->float:
        return (self.weight/(self.height)**2)
    
    @computed_field
    @property

    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
    
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
    @field_validator("city")
    def validate_city(cls, value):
        value=value.title()
        return value 


  ## Model to validate response  
class APIResponse(BaseModel):
    Predicted_classedicted_class: str = Field(
        ...,
        description="The predicted insurance premium category",
        example="High"
    )
    Confidence: float = Field(
        ...,
        description="Model's confidence score for the predicted class (range: 0 to 1)",
        example=0.8432
    )
    Probability: Dict[str, float] = Field(
        ...,
        description="Probability distribution across all possible classes",
        example={"Low": 0.01, "Medium": 0.15, "High": 0.84}
    )    