from services.general.base_service import BaseService
from services.orgs.helpers.orgs_helper import OrgsHelper
from services.orgs.models.org_response import OrgResponse
from services.orgs.models.credits_response import CreditsResponse
from services.orgs.models.purchase_request import PurchaseRequest
from services.orgs.models.purchase_response import PurchaseResponse
from services.orgs.models.plan_response import PlanResponse
from utils.api_utils import ApiUtils


class OrgsService(BaseService):
    SERVICE_URL = "https://kartochki.store/api"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)
        self.orgs_helper = OrgsHelper(self.api_utils)

    def get_me(self) -> OrgResponse:
        response = self.orgs_helper.get_me()
        response.raise_for_status()
        return OrgResponse(**response.json())

    def get_credits(self) -> CreditsResponse:
        response = self.orgs_helper.get_credits()
        response.raise_for_status()
        return CreditsResponse(**response.json())

    def get_plans(self) -> list[PlanResponse]:
        response = self.orgs_helper.get_plans()
        response.raise_for_status()
        return [PlanResponse(**plan) for plan in response.json()]

    def purchase_credits(self, credits: int, amount_rub_kopecks: int) -> PurchaseResponse:
        response = self.orgs_helper.post_purchase(
            json=PurchaseRequest(
                credits=credits,
                amountRubKopecks=amount_rub_kopecks
            ).model_dump()
        )
        response.raise_for_status()
        return PurchaseResponse(**response.json())