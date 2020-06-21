CREATE TABLE auto_insurance (
    insurance_id      VARCHAR(10) NOT NULL COMMENT 'Insurance ID of auto-mobile  insurance, starts with "A", followed by 9 digits number',
    customer_id       INT,
    start_date        DATETIME NOT NULL COMMENT 'start date of auto insurance policy',
    end_date          DATETIME NOT NULL COMMENT 'end date of auto insurance policy',
    premium_amount    DECIMAL(10, 2) NOT NULL COMMENT 'auto insurance premium amount',
    insurance_status  VARCHAR(1) NOT NULL COMMENT 'auto policy insurance status'
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN auto_insurance.insurance_id IS
    'Insurance ID of auto-mobile  insurance, starts with "A", followed by 9 digits number'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN auto_insurance.start_date IS
    'start date of auto insurance policy'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN auto_insurance.end_date IS
    'end date of auto insurance policy'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN auto_insurance.premium_amount IS
    'auto insurance premium amount'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN auto_insurance.insurance_status IS
    'auto policy insurance status'; */

ALTER TABLE auto_insurance ADD CONSTRAINT auto_insurance_pk PRIMARY KEY ( insurance_id );

CREATE TABLE auto_record (
    vin           VARCHAR(17) NOT NULL,
    insurance_id  VARCHAR(10) NOT NULL
);

ALTER TABLE auto_record ADD CONSTRAINT auto_record_pk PRIMARY KEY ( vin );
alter table auto_record drop primary key, add constraint auto_record_pk primary key(vin,insurance_id);



CREATE TABLE customer (
    customer_id     INT NOT NULL COMMENT 'customer''s id',
    first_name      VARCHAR(30) NOT NULL COMMENT 'customer''s first name',
    last_name       VARCHAR(30) NOT NULL COMMENT 'customer''s last name',
    gender          VARCHAR(1) COMMENT 'customer''s gender, must be either “M”, or “F” representing “Male” or “Female”.If it is NULL,means not provided',
    marital_status  VARCHAR(1) NOT NULL COMMENT 'customer''s marital status, the possible data value of marital status must be either “M”, “S”, or “W”, representing “Married”, “Single”, and “Widow/Widower” respectively.',
    customer_type   VARCHAR(2) NOT NULL COMMENT 'customer type, can be auto or home or both. “A” represents Automobile Insurance customer and “H” represents Home insurance customer, "B" represents both.',
    city            VARCHAR(30) NOT NULL COMMENT 'customer''s living city',
    state           VARCHAR(2) NOT NULL COMMENT 'customers'' state',
    street          VARCHAR(30) NOT NULL COMMENT 'customers'' street',
    zip             VARCHAR(5) NOT NULL COMMENT 'Zip code'
);

ALTER TABLE customer COMMENT
    'customer information';

/* Moved to CREATE TABLE
COMMENT ON COLUMN customer.customer_id IS
    'customer''s id'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN customer.first_name IS
    'customer''s first name'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN customer.last_name IS
    'customer''s last name'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN customer.gender IS
    'customer''s gender, must be either “M”, or “F” representing “Male” or “Female”.If it is NULL,means not provided'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN customer.marital_status IS
    'customer''s marital status, the possible data value of marital status must be either “M”, “S”, or “W”, representing “Married”, “Single”, and “Widow/Widower” respectively.'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN customer.customer_type IS
    'customer type, can be auto or home or both. “A” represents Automobile Insurance customer and “H” represents Home insurance customer, "B" represents both.'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN customer.city IS
    'customer''s living city'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN customer.state IS
    'customers'' state'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN customer.street IS
    'customers'' street'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN customer.zip IS
    'Zip code'; */

ALTER TABLE customer ADD CONSTRAINT customer_pk PRIMARY KEY ( customer_id );

CREATE TABLE driver (
    license_num  VARCHAR(16) NOT NULL COMMENT 'driver''s license number',
    f_name       VARCHAR(30) NOT NULL COMMENT 'driver''s first name',
    l_name       VARCHAR(30) NOT NULL COMMENT 'driver''s last  name',
    birthdate    DATETIME NOT NULL COMMENT 'driver''s birthdate'
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN driver.license_num IS
    'driver''s license number'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN driver.f_name IS
    'driver''s first name'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN driver.l_name IS
    'driver''s last  name'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN driver.birthdate IS
    'driver''s birthdate'; */

ALTER TABLE driver ADD CONSTRAINT driver_pk PRIMARY KEY ( license_num );

CREATE TABLE home_insurance (
    insurance_id      VARCHAR(10) NOT NULL COMMENT 'Insurance ID of home  insurance, starts with "H", followed by 9 digits number',
    customer_id       INT,
    start_date        DATETIME NOT NULL COMMENT 'start date of home insurance policy',
    end_date          DATETIME NOT NULL COMMENT 'end date of home insurance policy',
    premium_amount    DECIMAL(10, 2) NOT NULL COMMENT 'home insurance premium amount',
    insurance_status  VARCHAR(1) NOT NULL COMMENT 'home policy insurance status. "C" for current, "P" for expired'
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN home_insurance.insurance_id IS
    'Insurance ID of home  insurance, starts with "H", followed by 9 digits number'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN home_insurance.start_date IS
    'start date of home insurance policy'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN home_insurance.end_date IS
    'end date of home insurance policy'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN home_insurance.premium_amount IS
    'home insurance premium amount'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN home_insurance.insurance_status IS
    'home policy insurance status. "C" for current, "P" for expired'; */

ALTER TABLE home_insurance ADD CONSTRAINT home_insurance_pk PRIMARY KEY ( insurance_id );

CREATE TABLE home_record (
    home_id       BIGINT NOT NULL,
    insurance_id  VARCHAR(10) NOT NULL
);

ALTER TABLE home_record ADD CONSTRAINT home_record_pk PRIMARY KEY ( home_id );
alter table home_record drop primary key, add constraint home_record_pk primary key(home_id,insurance_id);

CREATE TABLE insured_home (
    home_id                 BIGINT NOT NULL COMMENT 'home ID',
    home_purchase_date      DATETIME NOT NULL COMMENT 'home purchase date',
    home_purchase_value     DECIMAL(10, 2) NOT NULL COMMENT 'home purchase value',
    home_area               INT NOT NULL COMMENT 'home area in square feet',
    home_type               VARCHAR(1) NOT NULL COMMENT 'type of home, S,M,C,T representing Single family, Multi Family, Condominium, Town house respectively',
    auto_fire_notification  TINYINT NOT NULL COMMENT 'whether home has auto fire notification or not, 1 stands for yes, 0 stands for no',
    home_security_system    TINYINT NOT NULL COMMENT 'whether home has security system or not, 1 stands for yes, 0 stands for no',
    swimming_pool           VARCHAR(1) COMMENT 'whether home has swimming pool or not and which kind of pool: "I" represents Indoor, "U" represents Underground, "O" represents Overground, "M" represents Multiple',
    basement                TINYINT NOT NULL COMMENT 'whether home has basement or not, 1 shands for yes, 0 stands for no'
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN insured_home.home_id IS
    'home ID'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN insured_home.home_purchase_date IS
    'home purchase date'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN insured_home.home_purchase_value IS
    'home purchase value'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN insured_home.home_area IS
    'home area in square feet'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN insured_home.home_type IS
    'type of home, S,M,C,T representing Single family, Multi Family, Condominium, Town house respectively'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN insured_home.auto_fire_notification IS
    'whether home has auto fire notification or not, 1 stands for yes, 0 stands for no'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN insured_home.home_security_system IS
    'whether home has security system or not, 1 stands for yes, 0 stands for no'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN insured_home.swimming_pool IS
    'whether home has swimming pool or not and which kind of pool: "I" represents Indoor, "U" represents Underground, "O" represents Overground, "M" represents Multiple'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN insured_home.basement IS
    'whether home has basement or not, 1 shands for yes, 0 stands for no'; */

ALTER TABLE insured_home ADD CONSTRAINT insured_home_pk PRIMARY KEY ( home_id );

CREATE TABLE insured_vehicle (
    vin              VARCHAR(17) NOT NULL COMMENT 'vehicle identification number',
    make_model_year  SMALLINT NOT NULL COMMENT 'vehicle make model year',
    vehicle_status   VARCHAR(1) NOT NULL COMMENT 'status of the vehicle, can be one of “L”, “F”, or “O” representing “Leased”, Financed”, “and Owned’.'
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN insured_vehicle.vin IS
    'vehicle identification number'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN insured_vehicle.make_model_year IS
    'vehicle make model year'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN insured_vehicle.vehicle_status IS
    'status of the vehicle, can be one of “L”, “F”, or “O” representing “Leased”, Financed”, “and Owned’.'; */

ALTER TABLE insured_vehicle ADD CONSTRAINT insured_vehicle_pk PRIMARY KEY ( vin );

CREATE TABLE invoice_auto (
    invoice_id        INT NOT NULL COMMENT 'invoice id',
    insurance_id      VARCHAR(10) NOT NULL,
    invoice_date      DATETIME NOT NULL COMMENT 'date of invoice',
    payment_due_date  DATETIME NOT NULL COMMENT 'payment due date',
    invoice_amount    DECIMAL(10, 2) NOT NULL COMMENT 'invoice amount in usd'
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN invoice_auto.invoice_id IS
    'invoice id'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN invoice_auto.invoice_date IS
    'date of invoice'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN invoice_auto.payment_due_date IS
    'payment due date'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN invoice_auto.invoice_amount IS
    'invoice amount in usd'; */

ALTER TABLE invoice_auto ADD CONSTRAINT invoice_auto_pk PRIMARY KEY ( invoice_id );

CREATE TABLE invoice_home (
    invoice_id        INT NOT NULL COMMENT 'invoice id',
    insurance_id      VARCHAR(10) NOT NULL,
    invoice_date      DATETIME NOT NULL COMMENT 'date of invoice',
    payment_due_date  DATETIME NOT NULL COMMENT 'payment due date',
    invoice_amount    DECIMAL(10, 2) NOT NULL COMMENT 'invoice amount in usd'
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN invoice_home.invoice_id IS
    'invoice id'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN invoice_home.invoice_date IS
    'date of invoice'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN invoice_home.payment_due_date IS
    'payment due date'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN invoice_home.invoice_amount IS
    'invoice amount in usd'; */

ALTER TABLE invoice_home ADD CONSTRAINT invoice_home_pk PRIMARY KEY ( invoice_id );

CREATE TABLE payment_auto (
    payment_id      INT NOT NULL COMMENT 'payment''s ID',
    payment_date    DATETIME NOT NULL COMMENT 'date of payment',
    payment_method  VARCHAR(6) NOT NULL COMMENT 'payment method: "PayPal", "Credit", "Debit", "Check"',
    invoice_id      INT
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN payment_auto.payment_id IS
    'payment''s ID'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN payment_auto.payment_date IS
    'date of payment'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN payment_auto.payment_method IS
    'payment method: "PayPal", "Credit", "Debit", "Check"'; */

CREATE UNIQUE INDEX payment_auto__idx ON
    payment_auto (
        invoice_id
    ASC );

ALTER TABLE payment_auto ADD CONSTRAINT payment_auto_pk PRIMARY KEY ( payment_id );

CREATE TABLE payment_home (
    payment_id      INT NOT NULL COMMENT 'payment''s ID',
    invoice_id      INT,
    payment_date    DATETIME NOT NULL COMMENT 'date of payment',
    payment_method  VARCHAR(6) NOT NULL COMMENT 'payment method: "PayPal", "Credit", "Debit", "Check"'
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN payment_home.payment_id IS
    'payment''s ID'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN payment_home.payment_date IS
    'date of payment'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN payment_home.payment_method IS
    'payment method: "PayPal", "Credit", "Debit", "Check"'; */

CREATE UNIQUE INDEX payment_home__idx ON
    payment_home (
        invoice_id
    ASC );

ALTER TABLE payment_home ADD CONSTRAINT payment_home_pk PRIMARY KEY ( payment_id );

CREATE TABLE vehicle_driver (
    license_num  VARCHAR(16) NOT NULL,
    vin          VARCHAR(17) NOT NULL
);

ALTER TABLE vehicle_driver ADD CONSTRAINT vehicle_driver_pk PRIMARY KEY ( license_num,
                                                                          vin );

ALTER TABLE auto_insurance
    ADD CONSTRAINT a_insur_cust_fk FOREIGN KEY ( customer_id )
        REFERENCES customer ( customer_id );

ALTER TABLE auto_record
    ADD CONSTRAINT a_rcd_a_insur_fk FOREIGN KEY ( insurance_id )
        REFERENCES auto_insurance ( insurance_id );

ALTER TABLE auto_record
    ADD CONSTRAINT a_rcd_insured_vhcl_fk FOREIGN KEY ( vin )
        REFERENCES insured_vehicle ( vin );

ALTER TABLE home_insurance
    ADD CONSTRAINT h_insur_cust_fk FOREIGN KEY ( customer_id )
        REFERENCES customer ( customer_id );

ALTER TABLE home_record
    ADD CONSTRAINT h_rcd_h_insur_fk FOREIGN KEY ( insurance_id )
        REFERENCES home_insurance ( insurance_id );

ALTER TABLE home_record
    ADD CONSTRAINT h_rcd_insured_h_fk FOREIGN KEY ( home_id )
        REFERENCES insured_home ( home_id );

ALTER TABLE invoice_auto
    ADD CONSTRAINT inv_a_a_insur_fk FOREIGN KEY ( insurance_id )
        REFERENCES auto_insurance ( insurance_id );

ALTER TABLE invoice_home
    ADD CONSTRAINT inv_h_h_insur_fk FOREIGN KEY ( insurance_id )
        REFERENCES home_insurance ( insurance_id );

ALTER TABLE payment_auto
    ADD CONSTRAINT pay_a_inv_a_fk FOREIGN KEY ( invoice_id )
        REFERENCES invoice_auto ( invoice_id );

ALTER TABLE payment_home
    ADD CONSTRAINT pay_h_inv_h_fk FOREIGN KEY ( invoice_id )
        REFERENCES invoice_home ( invoice_id );

ALTER TABLE vehicle_driver
    ADD CONSTRAINT vhcl_drv_drv_fk FOREIGN KEY ( license_num )
        REFERENCES driver ( license_num );

ALTER TABLE vehicle_driver
    ADD CONSTRAINT vhcl_drv_vhcl_fk FOREIGN KEY ( vin )
        REFERENCES insured_vehicle ( vin );