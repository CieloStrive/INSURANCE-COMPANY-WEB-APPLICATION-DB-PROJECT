SELECT * FROM auto_record;

alter table auto_record
add column a_r_id int not null comment 'auto_record id';

update auto_record
set a_r_id = 1
where vin = '1B6MF36C6SS164013' and insurance_id = '1100000111';

update auto_record
set a_r_id = 2
where vin = '1B7HF13ZX1J572139' and insurance_id = '1100000083';

update auto_record
set a_r_id = 3
where vin = '1FAFP58S11A177991' and insurance_id = '1100000131';

update auto_record
set a_r_id = 4
where vin = '1FVACWCT67HY22127' and insurance_id = '1100000103';

update auto_record
set a_r_id = 5
where vin = '1N4AB41DXWC732852' and insurance_id = '1100000141';

update auto_record
set a_r_id = 6
where vin = '3G4AG54N9NS614902' and insurance_id = '1100000064';

update auto_record
set a_r_id = 7
where vin = '3G4AG55M8RS622999' and insurance_id = '1100000073';

update auto_record
set a_r_id = 8
where vin = '5N1AL0MM4DC301508' and insurance_id = '1100000113';

update auto_record
set a_r_id = 9
where vin = '5NPEC4AC5BH041176' and insurance_id = '1100000033';

update auto_record
set a_r_id = 10
where vin = 'JH4CC2640NC004693' and insurance_id = '1100000093';

update auto_record
set a_r_id = 11
where vin = 'JH4DA3360JS015375' and insurance_id = '1100000094';

update auto_record
set a_r_id = 12
where vin = 'JH4DA9350LS003644' and insurance_id = '1100000083';

update auto_record
set a_r_id = 13
where vin = 'JH4DA9440PS002537' and insurance_id = '1100000112';

update auto_record
set a_r_id = 14
where vin = 'JH4KA3161HC006800' and insurance_id = '1100000063';

update auto_record
set a_r_id = 15
where vin = 'JN8AS1MU0CM120061' and insurance_id = '1100000142';

update auto_record
set a_r_id = 16
where vin = 'SCBBR53W36C034889' and insurance_id = '1100000151';

update auto_record
set a_r_id = 17
where vin = 'WBACD432XWAV64423' and insurance_id = '1100000121';

alter table auto_record
drop primary key,
add constraint auto_record_pk primary key (vin, insurance_id, a_r_id);

alter table auto_record drop foreign key a_rcd_a_insur_fk;

alter table auto_record drop foreign key a_rcd_insured_vhcl_fk;

alter table auto_record
drop primary key,
add constraint auto_record_pk primary key (a_r_id);

ALTER TABLE auto_record
    ADD CONSTRAINT a_rcd_a_insur_fk FOREIGN KEY ( insurance_id )
        REFERENCES auto_insurance ( insurance_id );

ALTER TABLE auto_record
    ADD CONSTRAINT a_rcd_insured_vhcl_fk FOREIGN KEY ( vin )
        REFERENCES insured_vehicle ( vin );
