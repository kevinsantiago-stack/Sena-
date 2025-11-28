EJERCICIO INTEGRAL MYSQL

-- Crear BD
CREATE DATABASE ventas_db;
USE ventas_db;

-- Tablas
CREATE TABLE clientes(
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50),
  email VARCHAR(80)
);

CREATE TABLE productos(
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50),
  precio DECIMAL(10,2)
);

CREATE TABLE ventas(
  id INT PRIMARY KEY AUTO_INCREMENT,
  cliente_id INT,
  producto_id INT,
  fecha DATE,
  cantidad INT,
  FOREIGN KEY (cliente_id) REFERENCES clientes(id),
  FOREIGN KEY (producto_id) REFERENCES productos(id)
);

-- Inserts
INSERT INTO clientes(nombre,email) VALUES
('Ana Pérez','ana@gmail.com'),
('David Torres','david@gmail.com'),
('Laura Soto','laura@gmail.com');

INSERT INTO productos(nombre,precio) VALUES
('Laptop',3200.00),
('Mouse',25.50),
('Teclado',70.00);

INSERT INTO ventas(cliente_id,producto_id,fecha,cantidad) VALUES
(1,1,'2024-03-01',1),
(1,2,'2024-03-01',2),
(2,3,'2024-03-05',1),
(3,1,'2024-03-06',1);

-- Consultas
SELECT * FROM ventas;

SELECT c.nombre, p.nombre, v.cantidad, p.precio, (v.cantidad*p.precio) AS total
FROM ventas v
JOIN clientes c ON v.cliente_id=c.id
JOIN productos p ON v.producto_id=p.id;

SELECT c.nombre, SUM(v.cantidad*p.precio) AS total_gastado
FROM ventas v
JOIN clientes c ON v.cliente_id=c.id
JOIN productos p ON v.producto_id=p.id
GROUP BY c.id
ORDER BY total_gastado DESC;

UPDATE productos SET precio=3000.00 WHERE id=1;

DELETE FROM ventas WHERE id=2;
