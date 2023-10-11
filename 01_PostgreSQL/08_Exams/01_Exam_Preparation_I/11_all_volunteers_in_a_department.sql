-- 4.11. All Volunteers in a Department
-- url: https://judge.softuni.org/Contests/Practice/Index/4296#10

CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(
    IN searched_volunteers_department VARCHAR(30),
    OUT count_of_volunteers INT
)
AS
$$
BEGIN
    SELECT count(*) INTO count_of_volunteers
    from volunteers
    WHERE department_id =
          (SELECT id FROM volunteers_departments WHERE department_name = searched_volunteers_department);
END;
$$
    LANGUAGE plpgsql;

-- Test examples:
SELECT fn_get_volunteers_count_from_department('Education program assistant');
SELECT fn_get_volunteers_count_from_department('Guest engagement');
SELECT fn_get_volunteers_count_from_department('Zoo events');