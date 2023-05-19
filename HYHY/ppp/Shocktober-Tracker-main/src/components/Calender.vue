<template>
	<section v-if="listToDisplay != undefined && listToDisplay.size > 0" id="calender">
		<component 
			v-for="calVal in calender"
			:is="calVal.isPadding ? 'div' : 'a'" 
			:key="calVal.date"
			:class="{
				'today': isToday(calVal.date),
				'padding': calVal.isPadding,
				'date': true,
			}"
			v-tippy="{
				content: filmExist(calVal.date) ? listToDisplay.get(calVal.date)!.name : '',
				followCursor: true,
			}"
			:href="(filmExist(calVal.date)) ? `https://letterboxd.com${listToDisplay.get(calVal.date)!.slug}` : ''"
			target="_blank"
		>
			<template v-if="!calVal.isPadding">
				<h3>
					{{ calVal.date + 1 }}
				</h3>
				<p
					v-for="[username, filmList] in userFilmList.entries()"
					:class="filmList.get(listToDisplay.get(calVal.date)?.name ?? '')?.toLowerCase() ?? ''"
					class="user"
				>
					{{ username }}
				</p>
				</template>
		</component>
	</section>
</template>

<script setup lang="ts">
	import type { Film, WatchStatus } from '@/types';
	import { getDaysInMonth, firstDayInMonthIndex } from '@/utils'
	
	type CalenderItem = {
		isPadding: boolean
		date: number
	}

	type CalenderProps = {
		year: number,
		month: number
		listToDisplay: Map<number, Film>
		userFilmList: Map<string, Map<string, WatchStatus>>
	}

	const props = defineProps<CalenderProps>()

	const filmExist = (date: number)=> {
		return props.listToDisplay.has(date)
	}

	const isToday = (day: number) => {
		return new Date().getDate() == day + 1

	}

	const numberOfDays = getDaysInMonth(props.year, props.month)
	const firstDay = firstDayInMonthIndex(props.year, props.month)

	const paddingCalenderItems = Array(firstDay).fill("").map<CalenderItem>((_val, index) => {
		return {isPadding: true, date: index - firstDay}
	})
	
	const calenderDays = Array(numberOfDays).fill("").map<CalenderItem>((_val, index) => {
		return {isPadding: false, date: index}
	})
	
	const calender = [...paddingCalenderItems, ...calenderDays]
</script>

<style scoped>
	#calender
	{
		display: grid;
		grid-template-columns: repeat(7, 1fr);
		gap: 4px;
		
		max-width: 1400px;
		margin: auto;
		padding: 10px;
		padding-bottom: 80px;
	}

	a.date
	{
		display: flex;
		flex-direction: column;
		aspect-ratio: 1 / 1;
		overflow: hidden;

		text-decoration: none;
		color: var(--black);
		background: var(--white);

		transition: background-color 1.6s ease-in;
	}

	a.date.padding
	{
		opacity: 0;
		pointer-events: none;
	}

	a.date:hover,
	a.date:focus
	{
		background-color: var(--red);
		transition: background-color 0.3s ease;
	}
	
	h3
	{
		font-family: var(--numbers-font);
		font-size: 2.5rem;
		font-weight: normal;

		padding: 0.22em 0.11em 0;
		margin: 0;
		margin-bottom: auto;
		border-radius: 100%;

		line-height: 2ch;
		width: 2ch;
		text-align: center;

		transform: translate(-5px, -5px);
	}

	.today h3
	{
		background: var(--red);
	}

	p.user
	{
		font-family: var(--body-font);
		color: var(--black);
		margin: 0.25em 1ch;
		line-height: 0.9;

		border-radius: 2px;
		border-top-left-radius: 1em;
		border-bottom-right-radius: 1rem;

		max-width: max-content;
	}

	p.user:last-child
	{
		margin-bottom: 0.8em;
	}

	p.user.ontime
	{
		background-image: linear-gradient(90deg,
			hsl(0, 100%, 38%, 0),
			hsl(0, 100%, 38%, 1) 10%,
			hsl(0, 100%, 38%, 0.8) 53%,
			hsl(0, 100%, 38%, 1) 83%,
			hsl(0, 100%, 38%, 0.5));
	}

	p.user.late
	{
		background-image: linear-gradient(90deg, 
			hsl(0, 100%, 38%, 0),
			hsl(0, 100%, 38%, 1) 10%,
			hsl(0, 100%, 38%, 0.4) 30%,
			hsl(0, 100%, 38%, 1) 50%,
			hsl(0, 100%, 38%, 0.6) 70%,
			hsl(0, 100%, 38%, 1) 90%,
			hsl(0, 100%, 38%, 0.5));
	}

	@media (max-width: 975px)
	{
		#calender
		{
			gap: 3px;
		}

		h3
		{
			font-size: 1.3rem;
			transform: translate(-3px, -3px);
		}

		p.user
		{
			font-size: 0.8rem;
			letter-spacing: 0.05em;
		}
	}
	
	@media (max-width: 640px)
	{
		#calender
		{
			gap: 2px;
		}

		p.user
		{
			font-size: 0.7rem;
			letter-spacing: 0em;
			margin: 0.25em 2px;
		}
		
		a.date
		{
			aspect-ratio: auto;
		}
	}
</style>
