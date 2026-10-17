-- Datos iniciales para PostgreSQL (se ejecuta automáticamente al crear el contenedor)

CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL
);

INSERT INTO students (first_name, surname) VALUES
    ('John', 'Andersen'),
    ('Emma', 'Smith'),
    ('Lot', 'Lotso');
