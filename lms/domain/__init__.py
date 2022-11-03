from .borrowers.registry import borrowers_registry
from .loan_information.registry import loans_information_registry
from .loan_offer.registry import loan_offer_registry
from .payments.registry import payments_registry
from .reports.registry import reports_registry
from .users.registry import users_registry

borrowers_srv = borrowers_registry.service
linfo_srv = loans_information_registry.service
loan_offer_srv = loan_offer_registry.service
payments_srv = payments_registry.service
reports_srv = reports_registry.service
users_srv = users_registry.service
