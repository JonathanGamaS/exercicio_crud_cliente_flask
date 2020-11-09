CREATE DATABASE clientes;
use clientes;

CREATE TABLE registro_cliente (
  id integer NOT NULL AUTO_INCREMENT,
  nome VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  senha VARCHAR(200) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO registro_cliente
  (nome, email, senha)
VALUES
  ('Lancelot', 'lancelot@email.com', 'qvjgt'),
  ('Galahad', 'galahad@email.com', 'qvjgt');
