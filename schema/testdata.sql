-- test data
insert into markets (title, id) values ('The ponies will pwn', 1);
insert into players (name, id) values ('HOUSE', 0);
insert into players (name, id) values ('Amy', 1);
insert into players (name, id) values ('Bob', 2);
insert into players (name, id) values ('Cathy', 3);
insert into players (name, id) values ('Drew', 4);
insert into bids values (1, 0, 0.5);
insert into bids values (1, 1, 0.4);
insert into bids values (1, 2, 0.1);
insert into bids values (1, 1, 0.8);
insert into bids values (1, 3, 0.7);
insert into bids values (1, 2, 0.8);
insert into bids values (1, 4, 0.9);

update markets set state='resolved', answer=true where id = 1;


