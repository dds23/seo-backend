from typing import List, Optional, Union
from app.utils.common import CustomModel


class MozDataInterface(CustomModel):
    page: str
    subdomain: str
    root_domain: str
    title: str
    last_crawled: str
    http_code: int
    pages_to_page: int
    nofollow_pages_to_page: int
    redirect_pages_to_page: int
    external_pages_to_page: int
    external_nofollow_pages_to_page: int
    external_redirect_pages_to_page: int
    deleted_pages_to_page: int
    root_domains_to_page: int
    indirect_root_domains_to_page: int
    deleted_root_domains_to_page: int
    nofollow_root_domains_to_page: int
    pages_to_subdomain: int
    nofollow_pages_to_subdomain: int
    redirect_pages_to_subdomain: int
    external_pages_to_subdomain: int
    external_nofollow_pages_to_subdomain: int
    external_redirect_pages_to_subdomain: int
    deleted_pages_to_subdomain: int
    root_domains_to_subdomain: int
    deleted_root_domains_to_subdomain: int
    nofollow_root_domains_to_subdomain: int
    pages_to_root_domain: int
    nofollow_pages_to_root_domain: int
    redirect_pages_to_root_domain: int
    external_pages_to_root_domain: int
    external_indirect_pages_to_root_domain: int
    external_nofollow_pages_to_root_domain: int
    external_redirect_pages_to_root_domain: int
    deleted_pages_to_root_domain: int
    root_domains_to_root_domain: int
    indirect_root_domains_to_root_domain: int
    deleted_root_domains_to_root_domain: int
    nofollow_root_domains_to_root_domain: int
    page_authority: int
    domain_authority: Union[int, str]
    link_propensity: int
    spam_score: int
    root_domains_from_page: int
    nofollow_root_domains_from_page: int
    pages_from_page: int
    nofollow_pages_from_page: int
    root_domains_from_root_domain: int
    nofollow_root_domains_from_root_domain: int
    pages_from_root_domain: int
    nofollow_pages_from_root_domain: int
    pages_crawled_from_root_domain: int


class IMozResponse(CustomModel):
    results: List[MozDataInterface]


class MozRequest(CustomModel):
    targets: List[str]
    daily_history_deltas: Optional[List[str]] = []
    daily_history_values: Optional[List[str]] = []
    monthly_history_deltas: Optional[List[str]] = []
    monthly_history_values: Optional[List[str]] = []
    distributions: Optional[bool] = False
