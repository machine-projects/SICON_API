Generic single-database configuration.



#### Querys

``

INSERT INTO public.person
("name", surname, company_name, gender, birth_date, cpf, cnpj, creation_date, modification_date, "type")
VALUES('Felipe', 'Toffoli', null, 'Masculino', '19950315', '04784698108', null, '20120618 10:34:09 AM', '20120618 10:34:09 AM', 'Pessoa Fisica');


INSERT INTO public.address
(person_id, neighborhood, street, "number", complement, city, creation_date, modification_date)
VALUES(1, 'Monte Castelo', 'Julia Maksud', '117', 'bloco a 7, apartamento 14', 'Campo Grande', '20200602 10:34:09 AM', '20200602 10:34:09 AM');

INSERT INTO public.person_address
(address_id, person_id, creation_date, modification_date)
VALUES(1, 1, '20200602 10:34:09 AM', '20200602 10:34:09 AM');
``


