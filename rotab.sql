
/*==============================================================*/
/* Table: cadet                                                 */
/*==============================================================*/
create table cadet
(
   id_cadet             int not null  comment '',
   rang_cadet           varchar(128)  comment '',
   name_cadet           varchar(128)  comment '',
   zbroya               int  comment '',
   primary key (id_cadet)
);

/*==============================================================*/
/* Table: commandor                                             */
/*==============================================================*/
create table commandor
(
   id_commandor         int not null  comment '',
   rang_c               varchar(128)  comment '',
   name_c               varchar(128)  comment '',
   primary key (id_commandor)
);

/*==============================================================*/
/* Table: rota                                                  */
/*==============================================================*/
create table rota
(
   id_rota              int not null  comment '',
   name_rota            varchar(128)  comment '',
   commandor            int  comment '',
   primary key (id_rota)
);

/*==============================================================*/
/* Table: vzvod                                                 */
/*==============================================================*/
create table vzvod
(
   id_vzvod             int not null  comment '',
   rota                 int  comment '',
   vzvod_name           varchar(128)  comment '',
   cadet                int  comment '',
   primary key (id_vzvod)
);

/*==============================================================*/
/* Table: zbroya                                                */
/*==============================================================*/
create table zbroya
(
   id_zbroya            int not null  comment '',
   type_z               varchar(128)  comment '',
   name_z               varchar(128)  comment '',
   calibr               varchar(128)  comment '',
   primary key (id_zbroya)
);

alter table cadet add constraint FK_CADET_RELATIONS_ZBROYA foreign key (zbroya)
      references zbroya (id_zbroya) on delete set default on update cascade;

alter table rota add constraint FK_ROTA_RELATIONS_COMMANDO foreign key (commandor)
      references commandor (id_commandor) on delete set default on update cascade;

alter table vzvod add constraint FK_VZVOD_RELATIONS_CADET foreign key (cadet)
      references cadet (id_cadet) on delete set default on update cascade;

alter table vzvod add constraint FK_VZVOD_RELATIONS_ROTA foreign key (rota)
      references rota (id_rota) on delete set default on update cascade;

/* ========================== œ–Œ÷≈ƒ”–¿ ¬»¬≈ƒ≈ÕÕﬂ —œ»— ”  ”–—¿Õ“≤¬ “¿ «¿ –≤œÀ≈ÕŒØ «¡–ŒØ ============================*/
CREATE PROCEDURE chat () SELECT id_cadet, rang_cadet, name_cadet, type_z, name_z, id_zbroya FROM cadet INNER JOIN zbroya ON zbroya = zbroya.id_zbroya;

/* ==== œ–Œ÷≈ƒ”–¿ ¬»¬≈ƒ≈ÕÕﬂ —œ»— ”  ”–—¿Õ“≤¬ « ¿¬“ŒÃ¿“¿Ã», œ≤—“ŒÀ≈“¿Ã», √–¿Õ¿“ŒÃ≈“¿Ã»,  ”À≈Ã≈“¿Ã» ==================*/
CREATE PROCEDURE chat_automat () SELECT id_cadet, rang_cadet, name_cadet, type_z, name_z FROM cadet INNER JOIN zbroya ON zbroya = zbroya.id_zbroya WHERE type_Z = 'automat';
CREATE PROCEDURE chat_pistolet () SELECT id_cadet, rang_cadet, name_cadet, type_z, name_z FROM cadet INNER JOIN zbroya ON zbroya = zbroya.id_zbroya WHERE type_Z = 'pistolet';
CREATE PROCEDURE chat_granatomet () SELECT id_cadet, rang_cadet, name_cadet, type_z, name_z FROM cadet INNER JOIN zbroya ON zbroya = zbroya.id_zbroya WHERE type_Z = 'granatomet';
CREATE PROCEDURE chat_kulemet () SELECT id_cadet, rang_cadet, name_cadet, type_z, name_z FROM cadet INNER JOIN zbroya ON zbroya = zbroya.id_zbroya WHERE type_Z = 'kulemet';



DELIMITER //
CREATE TRIGGER before_succses BEFORE INSERT ON cadet
FOR EACH ROW BEGIN IF NEW.zbroya = zbroya THEN INSERT INTO zbroya values (NEW.id_cadet, NEW.rang_cadet, NEW.name_cadet, NULL);
END IF;
END//
DELIMITER ;