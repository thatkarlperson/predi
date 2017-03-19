
create type market_state as enum ('open', 'closed', 'resolved');

create table markets (
	title text,
	close_time timestamptz,
	resolve_time timestamptz,
	open_time timestamptz default now,
	state market_state,
	id serial primary key
);

create table players (
	name text,
	auth_type text,
	secret text,
	id serial primary key
);

create table bids (
	market references markets.id,
	player references players.id,
	value decimal(2,2) constraint (value > 0 and value < 1),
	bid_time timestamptz default now,
	id serial
);

