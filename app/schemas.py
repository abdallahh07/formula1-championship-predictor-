from pydantic import BaseModel

class FormulaInput(BaseModel):
  season: int
  operating_budget_usd_m: float
  sponsorship_revenue_usd_m: float
  prize_money_usd_m: float
  in_cost_cap_era: int
  cost_cap_limit_usd_m: float
  is_constructors_champion: int
  team_name_encoded: int 
  country_iso3_encoded: int
    
class FormulaOutput(BaseModel):
  total_revenue_usd_m: float