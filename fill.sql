-- INSERT INTO roles(label, created_at, updated_at) VALUES
--     ('Backend', now(), now()),
--     ('Frontend', now(), now()),
--     ('Fullstack', now(), now()),
--     ('QA', now(), now()),
--     ('PM', now(), now());


-- INSERT INTO levels(label,created_at, updated_at) VALUES
--     ('Junior', now(), now()),
--     ('Middle', now(), now()),
--     ('Senior', now(), now());

INSERT INTO tickets (sprint_id, title, description, reporter_id, assignee_id, due_date, role_id, level_id, created_at, updated_at)
VALUES
    (NULL, 'Ticket 1 Title', 'Ticket 1 Description', 1, 2, '2022-01-01', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now()),
    (NULL, 'Ticket 2 Title', 'Ticket 2 Description', 2, 3, '2022-01-02', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now()),
    (NULL, 'Ticket 3 Title', 'Ticket 3 Description', 3, 4, '2022-01-03', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now()),
    (NULL, 'Ticket 4 Title', 'Ticket 4 Description', 4, 5, '2022-01-04', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now()),
    (NULL, 'Ticket 5 Title', 'Ticket 5 Description', 5, 6, '2022-01-05', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now()),
    (NULL, 'Ticket 6 Title', 'Ticket 6 Description', 6, 7, '2022-01-06', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now()),
    (NULL, 'Ticket 7 Title', 'Ticket 7 Description', 4, 5, '2022-01-07', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now()),
    (NULL, 'Ticket 8 Title', 'Ticket 8 Description', 4, 2, '2022-01-08', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now()),
    (NULL, 'Ticket 9 Title', 'Ticket 9 Description', 2, 2, '2022-01-09', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now()),
    (NULL, 'Ticket 10 Title', 'Ticket 10 Description', 4, 1, '2022-01-10', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now()),
    (NULL, 'Ticket 11 Title', 'Ticket 11 Description', 1, 2, '2022-01-11', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now()),
    (NULL, 'Ticket 12 Title', 'Ticket 12 Description', 2, 3, '2022-01-12', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now()),
    (NULL, 'Ticket 13 Title', 'Ticket 13 Description', 3, 4, '2022-01-13', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now()),
    (NULL, 'Ticket 14 Title', 'Ticket 14 Description', 4, 5, '2022-01-14', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now()),
    (NULL, 'Ticket 15 Title', 'Ticket 15 Description', 5, 6, '2022-01-15', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now()),
    (NULL, 'Ticket 16 Title', 'Ticket 16 Description', 6, 7, '2022-01-16', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now()),
    (NULL, 'Ticket 17 Title', 'Ticket 17 Description', 7, 2, '2022-01-17', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now()),
    (NULL, 'Ticket 18 Title', 'Ticket 18 Description', 1, 5, '2022-01-18', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now()),
    (NULL, 'Ticket 19 Title', 'Ticket 19 Description', 1, 3, '2022-01-19', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now()),
    (NULL, 'Ticket 20 Title', 'Ticket 20 Description', 4, 1, '2022-01-20', FLOOR(RANDOM()*(16-12+1)+12), FLOOR(RANDOM()*(9-7+1)+7), now(), now());