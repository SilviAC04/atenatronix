select * from users;
insert into users (first_name, last_name, email, cedula_ruc, user_type_id, empresa_id, direccion_id) 
values ('Silvana', 'Arevalo', 'silvi.arevalo@udla.edu.ec', '0401314561', 2, 1,1),
('Lenin', 'Falconi', 'lenin.g.falconi@gmail.com', '1719676239', 2,1,2),
('Alejandro', 'Ayala', 'ayala@inaselecuador.com', '1719666666', 3,2,3); 

delete  from users where users.id=2; 

insert into users_types (description) values ('Administrador'), ('Cliente'), ('Vendedor');
select * from users_types;

insert into empresas (name, ruc, direccion_id) values ('INDEPENDIENTE', '9999999999001', 1), 
('INASEL', '1791826140001', 2),
('SEBATELEC', '1791886933001', 3),
('INGELCOM', '1791852567001', 4);
select * from empresas;
insert into direcciones (direccion, latitud, longitud) 
values ('DIRECCION GENERICA', -0.22985, -78.52495),
('Jorge juan N',-0.187227,-78.492864),
('Juan Barrezueta 170310',-0.092269,-78.473837),
('Av. 6 de Diciembre N47-203 y, Quito 170138',-0.15148,-78.47652);
select * from direcciones;

insert into paises_fabricantes (nombre_pais) values ('ALEMANIA'), ('FRANCIA'), ('ESTADOS UNIDOS'), ('ECUADOR');
select * from paises_fabricantes;

select * from product_types;
insert into product_types (descripcion) values ('CONTROL INDUSTRIAL - MANIOBRA'), ('ACCIONAMIENTOS DE VELOCIDAD VARIABLE'), ('AUTOMATIZACION'), ('ELECTRICIDAD BAJO VOLTAJE');

select * from fabricantes;
insert into fabricantes (nombre, pais_fabricante_id) values ('SIEMENS', 1), ('SCHNEIDER', 1), ('ABB', 3);

select * from products limit 10;
select product_type_id, count(*) from products group by products.product_type_id;
select count(*) from products;

delete from products where id=423;

select products.id, product_types.descripcion as categoria, products.descripcion, products.precio from products 
left join product_types on products.product_type_id=product_types.id
limit 10;
insert into products (codigo_fabricante, descripcion, precio, stock, product_type_id, fabricante_id, empresa_id) 
values ('6SL3210-5BB13-7UV1', 'SINAMICS V20, 1AC 23', 311.00, 10, 2, 1, 2),
('6SL3210-5BB13-7UV1', 'CPU 1511-1PN, 150KB', 1942.00, 2, 3, 1, 2),
('6AV2123-2DB03-0AX0', 'SIMATIC HMI KTP400 B', 877.00, 5, 3, 1, 2),
('6ES7822-1AE07-0YA5', 'SIMATIC STEP 7 PROFESIONAL', 5091.00, 2, 3, 1, 3),
('6ED1055-1MB00-0BA2', 'LOGO! DM8 12/24R Exp', 127.00, 8, 3, 1, 4);

select * from servicios;
insert into servicios (descripcion, precio, empresa_id) 
values ('Programación de PLC', 1500, 1),
('Programación de PLC', 2000, 2),
('Programación de HMI', 5000, 1),
('Programación de HMI', 7000, 3),
('Configuración de Accionamientos de velocidad variable', 3000, 2),
('Instalación eléctrica industrial de bajo voltaje', 3000, 2);

# como realizo una compra?????
# 1 generar un id de compra
select * from compras;
insert into compras (descripcion) values ('compra1'), ('compra2'), ('compra3');
select * from users_has_products;
insert into users_has_products (user_id, product_id, cantidad, compra_id) 
values (2, 1, 2, 1),(2,2,1,1), (1,3,10,2);

select * from users
left join users_has_products on users.id = users_has_products.user_id
left join  products on products.id = user_has_products.product_id;

select * from products
left join users_has_products on users_has_products.product_id = products.id
left join  users on users.id = users_has_products.user_id
where user_id = 2;


 