from services.general.base_service import BaseService
from services.orgs.helpers.orgs_helper import OrgsHelper
from services.orgs.models.org_response import OrgResponse
from services.orgs.models.credits_response import CreditsResponse
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