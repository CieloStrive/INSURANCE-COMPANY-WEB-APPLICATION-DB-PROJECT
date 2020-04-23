SELECT * FROM vehicle_driver;

alter table vehicle_driver
add column v_d_id int not null comment 'vehicle_driver id';

update vehicle_driver
set v_d_id = 1
where license_num = '016446449'and vin = '1B6MF36C6SS164013';

update vehicle_driver
set v_d_id = 2
where license_num = '016446449'and vin = '5N1AL0MM4DC301508';

update vehicle_driver
set v_d_id = 3
where license_num = '016446449'and vin = 'JH4DA9440PS002537';

update vehicle_driver
set v_d_id = 4
where license_num = '259774698'and vin = 'JH4KA3161HC006800';

update vehicle_driver
set v_d_id = 5
where license_num = '445174650'and vin = 'SCBBR53W36C034889';

update vehicle_driver
set v_d_id = 6
where license_num = '516354818'and vin = '1N4AB41DXWC732852';

update vehicle_driver
set v_d_id = 7
where license_num = '516354818'and vin = '3G4AG54N9NS614902';

update vehicle_driver
set v_d_id = 8
where license_num = '516354818'and vin = '5NPEC4AC5BH041176';

update vehicle_driver
set v_d_id = 9
where license_num = '904479134'and vin = '1FVACWCT67HY22127';

update vehicle_driver
set v_d_id = 10
where license_num = '9419543'and vin = '1N4AB41DXWC732852';

update vehicle_driver
set v_d_id = 11
where license_num = '9419543'and vin = 'JH4DA9350LS003644';

update vehicle_driver
set v_d_id = 12
where license_num = '9419543'and vin = 'JN8AS1MU0CM120061';

update vehicle_driver
set v_d_id = 13
where license_num = 'C14791382'and vin = '1FAFP58S11A177991';

update vehicle_driver
set v_d_id = 14
where license_num = 'G7997872'and vin = '1B7HF13ZX1J572139';

update vehicle_driver
set v_d_id = 15
where license_num = 'Q93086387024583'and vin = 'JH4DA3360JS015375';

update vehicle_driver
set v_d_id = 16
where license_num = 'Q93086387024583'and vin = 'WBACD432XWAV64423';

update vehicle_driver
set v_d_id = 17
where license_num = 'S5304609913000'and vin = '3G4AG55M8RS622999';

update vehicle_driver
set v_d_id = 18
where license_num = 'S5304609913000'and vin = 'JH4CC2640NC004693';

update vehicle_driver
set v_d_id = 19
where license_num = 'S5304609913000'and vin = 'JH4DA9440PS002537';

alter table vehicle_driver
drop primary key,
add constraint vehicle_driver_pk primary key (license_num, vin, v_d_id);

alter table vehicle_driver drop foreign key vhcl_drv_drv_fk;

alter table vehicle_driver drop foreign key vhcl_drv_vhcl_fk;

alter table vehicle_driver
drop primary key,
add constraint vehicle_driver_pk primary key (v_d_id);

ALTER TABLE vehicle_driver
    ADD CONSTRAINT vhcl_drv_drv_fk FOREIGN KEY ( license_num )
        REFERENCES driver ( license_num );

ALTER TABLE vehicle_driver
    ADD CONSTRAINT vhcl_drv_vhcl_fk FOREIGN KEY ( vin )
        REFERENCES insured_vehicle ( vin );


