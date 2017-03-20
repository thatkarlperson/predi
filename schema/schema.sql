
create type market_state as enum ('open', 'closed', 'resolved');

create table markets (
	title text not null,
	state market_state not null default 'open',
	answer boolean default null,
	open_time timestamptz default now(),
	close_time timestamptz default now() + '1 day',
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

-- Resolved bids are those that are counted towards a player's score.
-- If a market resolves false, the bid value is inverted.
create view resolved_bids as 
	select bids.market, bids.player,
		(case when markets.answer
			then bids.value
			else 1 - bids.value
		end) as truth,
		bids.bid_time,
		bids.id
		from bids join markets
		     on bids.market = markets.id
		where markets.state = 'resolved';

-- align each current bid with the previous one
create view aligned_bids as
	select player, truth, 
	       lag(truth) over (partition by market order by bid_time) as previous, 
	       id
	from resolved_bids;

-- calculate centibits from each new bid
create view scored_bids as
	select player, 100 * (log(2, truth) - log(2, previous)) as score, id
	from aligned_bids;

-- total player scores
create view player_scores as
	select player, sum(score) from scored_bids
	group by player;

