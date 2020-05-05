alter table CUSTOMER add constraint C_CUSTOMER_GENDER check 
((GENDER is NULL) or (GENDER='M') or (GENDER='F'));

alter table CUSTOMER add constraint C_CUSTOMER_MARITAL_STATUS check 
((MARITAL_STATUS='M') or (MARITAL_STATUS='S') or (MARITAL_STATUS='W'));
	
alter table CUSTOMER add constraint C_CUSTOMER_CUSTOMER_TYPE check 
((CUSTOMER_TYPE='A') or (CUSTOMER_TYPE='H') or (CUSTOMER_TYPE='B'));

alter table CUSTOMER drop check C_CUSTOMER_CUSTOMER_TYPE;
	
alter table CUSTOMER add constraint C_CUSTOMER_CUSTOMER_TYPE check 
((CUSTOMER_TYPE='A') or (CUSTOMER_TYPE='H') or (CUSTOMER_TYPE='B') or (CUSTOMER_TYPE='N'));
    
alter table HOME_INSURANCE add constraint C_HOME_INSURANCE_INSURANCE_STATUS check 
((INSURANCE_STATUS='C') or (INSURANCE_STATUS='P'));
	
alter table AUTO_INSURANCE add constraint C_AUTO_INSURANCE_INSURANCE_STATUS check 
((INSURANCE_STATUS='C') or (INSURANCE_STATUS='P'));
	
alter table INSURED_HOME add constraint C_INSURED_HOME_HOME_TYPE check 
((HOME_TYPE='S') or (HOME_TYPE='M') or (HOME_TYPE='C') or (HOME_TYPE='T'));
	
alter table INSURED_HOME add constraint C_INSURED_HOME_AUTO_FIRE_NOTIFICATION check 
((AUTO_FIRE_NOTIFICATION=1) or (AUTO_FIRE_NOTIFICATION=0));
	
alter table INSURED_HOME add constraint C_INSURED_HOME_HOME_SECURITY_SYSTEM check 
((HOME_SECURITY_SYSTEM=1) or (HOME_SECURITY_SYSTEM=0));
	
alter table INSURED_HOME add constraint C_INSURED_HOME_BASEMENT check 
((BASEMENT=1) or (BASEMENT=0));
	
alter table INSURED_HOME add constraint C_INSURED_HOME_SWIMMING_POOL check 
((SWIMMING_POOL='U') or (SWIMMING_POOL='O') or (SWIMMING_POOL='I') or (SWIMMING_POOL='M') or (SWIMMING_POOL is NULL));

alter table PAYMENT_HOME add constraint C_PAYMENT_HOME_PAYMENT_METHOD check 
((PAYMENT_METHOD='PayPal') or (PAYMENT_METHOD='Credit') or (PAYMENT_METHOD='Debit') or (PAYMENT_METHOD='Check'));

alter table PAYMENT_AUTO add constraint C_PAYMENT_AUTO_PAYMENT_METHOD check 
((PAYMENT_METHOD='PayPal') or (PAYMENT_METHOD='Credit') or (PAYMENT_METHOD='Debit') or (PAYMENT_METHOD='Check'));

alter table INSURED_VEHICLE add constraint C_INSURED_VEHICLE_VEHICLE_STATUS check 
((VEHICLE_STATUS='L') or (VEHICLE_STATUS='F') or (VEHICLE_STATUS='O'));

alter table CUSTOMER add constraint C_CUSTOMER_FIRST_NAME check 
(FIRST_NAME=upper(FIRST_NAME));

alter table CUSTOMER add constraint C_CUSTOMER_LAST_NAME check 
(LAST_NAME=upper(LAST_NAME));

alter table CUSTOMER add constraint C_CUSTOMER_CITY check 
(CITY=upper(CITY));

alter table CUSTOMER add constraint C_CUSTOMER_STATE check 
(STATE=upper(STATE));

alter table CUSTOMER add constraint C_CUSTOMER_STREET check 
(STREET=upper(STREET));

alter table DRIVER add constraint C_DRIVER_F_NAME check 
(F_NAME=upper(F_NAME));

alter table DRIVER add constraint C_DRIVER_L_NAME check 
(L_NAME=upper(L_NAME));