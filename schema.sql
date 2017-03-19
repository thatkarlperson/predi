
create type market_state as enum ('open', 'closed', 'resolved');

create table markets (
	title text not null,
	state market_state not null,
	close_time timestamptz,
	resolve_time timestamptz,
	resolution boolean default null,
	open_time timestamptz default now(),
	id serial primary key
);

create table players (
	name text not null,
	auth_type text,  -- don't know what this will be yet
	secret text,     -- same here, but probably separate
	id serial primary key
);

create table bids (
	market integer references markets (id),
	player integer references players (id),
	value decimal(2,2) not null check (value > 0 and value < 1),
	bid_time timestamptz default now(),
	id serial primary key
);

