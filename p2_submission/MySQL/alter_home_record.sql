SELECT * FROM home_record;

alter table home_record
add column h_r_id int not null comment 'home_record id';

update home_record
set h_r_id = 1
where home_id = '1000000011' and insurance_id = '1100000011';

update home_record
set h_r_id = 2
where home_id = '1000000021' and insurance_id = '1100000021';

update home_record
set h_r_id = 3
where home_id = '1000000031' and insurance_id = '1100000031';

update home_record
set h_r_id = 4
where home_id = '1000000031' and insurance_id = '1100000032';

update home_record
set h_r_id = 5
where home_id = '1000000041' and insurance_id = '1100000041';

update home_record
set h_r_id = 6
where home_id = '1000000041' and insurance_id = '1100000042';

update home_record
set h_r_id = 7
where home_id = '1000000042' and insurance_id = '1100000043';

update home_record
set h_r_id = 8
where home_id = '1000000051' and insurance_id = '1100000051';

update home_record
set h_r_id = 9
where home_id = '1000000052' and insurance_id = '1100000051';

update home_record
set h_r_id = 10
where home_id = '1000000053' and insurance_id = '1100000051';

update home_record
set h_r_id = 11
where home_id = '1000000061' and insurance_id = '1100000061';

update home_record
set h_r_id = 12
where home_id = '1000000062' and insurance_id = '1100000062';

update home_record
set h_r_id = 13
where home_id = '1000000071' and insurance_id = '1100000071';

update home_record
set h_r_id = 14
where home_id = '1000000072' and insurance_id = '1100000072';

update home_record
set h_r_id = 15
where home_id = '1000000081' and insurance_id = '1100000081';

update home_record
set h_r_id = 16
where home_id = '1000000082' and insurance_id = '1100000081';

update home_record
set h_r_id = 17
where home_id = '1000000083' and insurance_id = '1100000081';

update home_record
set h_r_id = 18
where home_id = '1000000084' and insurance_id = '1100000082';

update home_record
set h_r_id = 19
where home_id = '1000000091' and insurance_id = '1100000091';

update home_record
set h_r_id = 20
where home_id = '1000000092' and insurance_id = '1100000092';

update home_record
set h_r_id = 21
where home_id = '1000000101' and insurance_id = '1100000101';

update home_record
set h_r_id = 22
where home_id = '1000000102' and insurance_id = '1100000102';

update home_record
set h_r_id = 23
where home_id = '1000000151' and insurance_id = '1100000153';

update home_record
set h_r_id = 24
where home_id = '1000000152' and insurance_id = '1100000153';

alter table home_record
drop primary key,
add constraint home_record_pk primary key (home_id, insurance_id, h_r_id);

alter table home_record drop foreign key h_rcd_h_insur_fk;

alter table home_record drop foreign key h_rcd_insured_h_fk;

alter table home_record
drop primary key,
add constraint home_record_pk primary key (h_r_id);

ALTER TABLE home_record
    ADD CONSTRAINT h_rcd_h_insur_fk FOREIGN KEY ( insurance_id )
        REFERENCES home_insurance ( insurance_id );

ALTER TABLE home_record
    ADD CONSTRAINT h_rcd_insured_h_fk FOREIGN KEY ( home_id )
        REFERENCES insured_home ( home_id );