create table if not exists clima_detalhado (
    id bigint not null auto_increment,
    temperatura_atual float not null,
    temperatura_minima float not null,
    temperatura_maxima float not null,
    data_hora datetime,
    clima int not null, /* 1 - ensolarado | 2 - nublado | 3 - garoando | 4 - chuvoso | 5 - tempestade */
    periodo varchar(100), /* manha, tarde, noite, madru */
    primary key(id)
);

create table if not exists clima_resumo_diario (
    id bigint not null auto_increment,
    dia date,
    temperatura_media_geral float not null,
    clima_geral_manha int not null,
    clima_geral_tarde int not null,
    clima_geral_noite int not null,
    clima_geral_madru int not null,
    primary key(id)
);