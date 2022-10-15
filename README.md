Loan Management System 
==
A simple graphQL Loan Management System built in python

## Collections [WIP]
```python
class Gender(Enum):
  MALE = 0
  FEMALE = 1
  
class Borrowers:
    created_at: datetime.datetime
    name: str
    phone_number: str
    age: int
    address: str,
    gender: Gender
```

```python
class PaymentRange(Enum):
  DAILY = 0
  WEEKLY = 1
  BIWEEKLY = 2
  MONTHLY = 3
  BIMONTHLY = 4
  QUARTERLY = 5
  SEMIANNUALLY = 6
  ANNUALLY = 7

class LoansInformation:
  borrower_id: ObjectId
  loan_date: datetime.datetime
  loan_due: float
  payment_range: PaymentRange 
```

## Services [WIP]
- [x] Create a borrower
- [x] Get all borrowers
- [x] get a borrower information
- [x] Create a LoansInformation
- [x] Get all borrowers
- [ ] Get a LoansInformation



