from .borrowers.registry import borrowers_registry
from .loan_information.registry import loan_informations_registry

borrowers_srv = borrowers_registry.service
linfo_srv = loan_informations_registry.service
