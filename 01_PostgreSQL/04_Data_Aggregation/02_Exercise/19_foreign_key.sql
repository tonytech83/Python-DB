-- 19. Foreign Key
-- url: https://judge.softuni.org/Contests/Compete/Index/4107#18

CREATE TABLE employees_projects
(
    id          SERIAL PRIMARY KEY,
    employee_id int,
    project_id  int,

    CONSTRAINT fk_employees_projects__employees
        FOREIGN KEY (employee_id)
            REFERENCES employees (id),
    CONSTRAINT fk_employees_projects__projects
        FOREIGN KEY (project_id)
            REFERENCES projects (id)
);
