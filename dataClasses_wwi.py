## creating classes for World Wide Importers
from dataclasses import dataclass
import datetime as dt

## CUSTOMERS
@dataclass
class Customer:
    customerID: int
    name: str
    billCustomerID: int
    customerCategoryID: int
    buyingGroupID: int
    primaryContactID: int
    alternateContactID: int
    deliveryMethodID: int
    deliveryCityID: str
    postalCityID: str
    creditLimit: float
    accountOpenDate: dt.date
    discountPercentage: float
    isStatementSent: bool
    onCreditHold: bool
    paymentDays: int
    phoneNum: str
    faxNum: str
    deliveryRun: str
    runPosition: str
    webURL: str
    deliveryAddress1: str
    deliveryAddress2: str
    deliveryPostalCode: str
    postalAddress1: str
    postalAddress2: str
    postalPostalCode: str
    lastEditBy: int
    validFrom: dt.datetime
    validTo: dt.datetime

## ORDERS
@dataclass
class Order:
    orderID: int
    customer: object
    salespersonID: int
    pickedByID: int
    contactPersonID: int
    backorderID: int
    orderDate: dt.date
    expectedDeliveryDate: dt.date
    customerPurchaseOrderNum: str
    isUnderSupply: bool
    comments: str
    deliveryInstructions: str
    internalComments: str
    pickingCompletedDate: dt.datetime
    lastEditBy: int
    lastEditWhen: dt.datetime

# magic methods: comparing order dates
    def __gt__(self,other):
        if self.orderDate > other.orderDate:
            print("__gt__ called\nTrue\nOrder #%i > Order #%i" % (self.orderID,other.orderID))
        else:
            print("__gt__ called\nFalse")

    def __ge__(self,other):
        if (self.orderDate > other.orderDate) or (self.orderDate == other.orderDate):
            print("__ge__ called\nTrue\nOrder #%i >= Order #%i" % (self.orderID,other.orderID))
        else:
            print("__ge__ called\nFalse")

    def __eq__(self,other):
        if self.orderDate == other.orderDate:
            print("__eq__ called\nTrue\nOrder #%i = Order #%i" % (self.orderID,other.orderID))
        else:
            print("__eq__ called\nFalse")

## INVOICES
@dataclass
class Invoice:
    invoiceID: int
    customer: object
    order: object
    accountPersonID: int
    packedByPersonID: int
    invoiceDate: dt.date
    isCreditNote: bool
    creditNoteReason: str
    dryItems: int
    chillerItems: int
    returnedDeliveryData: str
    confirmedDeliveryTime: dt.datetime
    confirmedReceivedBy: str

# magic methods: comparing total items (dry + chiller)
    def __gt__(self,other):
        total1 = self.dryItems + self.chillerItems
        total2 = other.dryItems + other.chillerItems
        if total1 > total2:
            print("__gt__called\nTrue\nInvoice #%i > Invoice #%i" % (self.invoiceID,other.invoiceID))
        else:
            print("__gt__ called\nFalse")

    def __ge__(self,other):
        total1 = self.dryItems + self.chillerItems
        total2 = other.dryItems + other.chillerItems
        if (total1 > total2) or (total1 == total2):
            print("__ge__called\nTrue\nInvoice #%i >= Invoice #%i" % (self.invoiceID,other.invoiceID))
        else:
            print("__ge__ called\nFalse")

    def __eq__(self,other):
        total1 = self.dryItems + self.chillerItems
        total2 = other.dryItems + other.chillerItems
        if total1 == total2:
            print("__eq__called\nTrue\nInvoice #%i = Invoice #%i" % (self.invoiceID,other.invoiceID))
        else:
            print("__eq__ called\nFalse")

