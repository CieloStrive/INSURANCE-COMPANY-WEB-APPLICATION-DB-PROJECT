--total number of records populated for CUSTOMER:
select COUNT(*) 
from CUSTOMER;

--total number of records populated for HOME_INSURANCE:
select COUNT(*) 
from HOME_INSURANCE;

--total number of records populated for HOME_RECORD:
select COUNT(*) 
from HOME_RECORD;

--total number of records populated for INSURED_HOME:
select COUNT(*) 
from INSURED_HOME;

--total number of records populated for INVOICE_HOME:
select COUNT(*) 
from INVOICE_HOME;

--total number of records populated for PAYMENT_HOME:
select COUNT(*) 
from PAYMENT_HOME;

--total number of records populated for AUTO_INSURANCE:
select COUNT(*) 
from AUTO_INSURANCE;

--total number of records populated for AUTO_RECORD:
select COUNT(*) 
from AUTO_RECORD;

--total number of records populated for INSURED_VEHICLE:
select COUNT(*) 
from INSURED_VEHICLE;

--total number of records populated for VEHICLE_DRIVER:
select COUNT(*) 
from VEHICLE_DRIVER;

--total number of records populated for DRIVER:
select COUNT(*) 
from DRIVER;

--total number of records populated for INVOICE_AUTO:
select COUNT(*) 
from INVOICE_AUTO;

--total number of records populated for PAYMENT_AUTO:
select COUNT(*) 
from PAYMENT_AUTO;

--g
select a.table_name, a.column_name, a.data_type, a.data_length, a.data_precision, a.data_scale, a.nullable, b.comments
from user_tab_columns a, user_col_comments b
where a.table_name=b.table_name and a.column_name=b.column_name
order by a.table_name;

--g
select table_name, constraint_name, constraint_type, search_condition, index_name, r_owner, r_constraint_name, delete_rule
from user_constraints
order by table_name;

--h
--Q1
SELECT CUSTOMER_ID, FIRST_NAME, LAST_NAME, INSURANCE_ID, PREMIUM_AMOUNT, INSURANCE_STATUS, HOME_ID, HOME_PURCHASE_VALUE, HOME_TYPE 
FROM CUSTOMER  NATURAL JOIN HOME_INSURANCE  NATURAL JOIN HOME_RECORD  NATURAL JOIN INSURED_HOME 
ORDER BY CUSTOMER_ID;


--Q2
SELECT CUSTOMER_ID, PREMIUM_AMOUNT 
FROM HOME_INSURANCE
WHERE PREMIUM_AMOUNT >= ALL (SELECT AVG(PREMIUM_AMOUNT) FROM HOME_INSURANCE GROUP BY CUSTOMER_ID);


--Q3
SELECT a.CUSTOMER_ID, a.PREMIUM_AMOUNT
FROM HOME_INSURANCE a
WHERE a.PREMIUM_AMOUNT > (SELECT AVG(b.PREMIUM_AMOUNT) PERSONALAVG FROM HOME_INSURANCE b WHERE a.CUSTOMER_ID = b.CUSTOMER_ID);


--Q4
select CUSTOMER_ID, PREMIUM_AMOUNT 
from AUTO_INSURANCE 
where PREMIUM_AMOUNT > (select AVG(PREMIUM_AMOUNT) from AUTO_INSURANCE)
INTERSECT
select CUSTOMER_ID, PREMIUM_AMOUNT 
from AUTO_INSURANCE 
where PREMIUM_AMOUNT < (select MAX(PREMIUM_AMOUNT) from AUTO_INSURANCE)
order by PREMIUM_AMOUNT desc;


--Q5
WITH TOTAL AS 
(select CUSTOMER_ID, INSURANCE_ID, PREMIUM_AMOUNT
from AUTO_INSURANCE
where INSURANCE_STATUS='C'
UNION
select CUSTOMER_ID, INSURANCE_ID, PREMIUM_AMOUNT
from HOME_INSURANCE
where INSURANCE_STATUS='C')
select a.FIRST_NAME, a.LAST_NAME, b.PREMIUM_AMOUNT
from CUSTOMER a, TOTAL b
where a.CUSTOMER_ID=b.CUSTOMER_ID and b.PREMIUM_AMOUNT=(select MAX(PREMIUM_AMOUNT) from TOTAL);