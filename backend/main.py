from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="ShieldRider API", description="Phase 2 API Contracts")

# --- Pydantic Models for Request Bodies ---
class RiderRegistration(BaseModel):
    rider_id: str
    name: str
    platform: str
    vehicle_type: str
    primary_zone_id: str

class ClaimCheck(BaseModel):
    rider_id: str
    current_lat: float
    current_lon: float
    active_delivery: bool

# --- API Endpoints ---

@app.post("/api/v1/rider/register")
async def register_rider(rider: RiderRegistration):
    """Mocks the Registration Process"""
    return {
        "status": "success",
        "message": f"Rider {rider.name} onboarded successfully.",
        "risk_profile_status": "pending_calculation"
    }

@app.get("/api/v1/policy/quote/{rider_id}")
async def get_policy_quote(rider_id: str):
    """Mocks the Insurance Policy Management & Dynamic Premium"""
    return {
        "policy_id": "POL_WEEK_12",
        "rider_id": rider_id,
        "validity": "7_days",
        "dynamic_weekly_premium_inr": 30.00,
        "base_premium_inr": 50.00,
        "ai_discount_applied": 20.00,
        "discount_reason": "Historically safe from waterlogging in primary zone",
        "coverage_status": "Ready for Purchase"
    }

@app.post("/api/v1/claims/check-trigger")
async def check_parametric_trigger(claim_data: ClaimCheck):
    """Mocks the Claims Management & Trigger Detection"""
    # For Sprint 1, we are just mocking a successful trigger detection
    return {
        "trigger_activated": True,
        "disruption_type": "Severe Waterlogging",
        "mock_api_source": "Simulated_Weather_Grid",
        "claim_status": "Auto-Approved",
        "payout_amount_inr": 350.00,
        "action_required": "None - Zero Touch Payout Initiated"
    }

# Run this locally using: uvicorn main:app --reload