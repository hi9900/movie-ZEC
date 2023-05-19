<template>
	<form @submit.prevent>
		<div class="username">
			<label for="username">usernames</label>
			<input type="text"
				id="username" 
				name="u"
				@change="userName = ($event.target as HTMLInputElement).value"
				:value="userName"
				required
			>
		</div>
		<div class="listName">
			<label for="listName">list</label>
			<input type="text"
				id="list" 
				name="ln"
				placeholder="holopollock/list/full-shocktober-2022"
				@change="listName = ($event.target as HTMLInputElement).value"
				:value="listName"
				required
			>
		</div>
		<button v-on:click="update()">Submit</button>
	</form>
</template>

<script setup lang="ts">
    import { ref } from 'vue'
    import { useControlsStore } from '@/stores/controls'
	import { useShocktoberUrlParams } from '@/utils/useShocktoberUrlParam';

	const {list, userName: userNamesFromUrl} = useShocktoberUrlParams()
    const userName = ref(userNamesFromUrl.join(','))  
    const listName = ref(list)

    const controls = useControlsStore()
    if (userName.value !== '' && listName.value !== '') {
        controls.$patch({
            userNames: userName.value,
            listName: listName.value
        })
    }
    const update = () => {
        controls.$patch({
            userNames: userName.value,
            listName: listName.value
        })
    }
</script>

<style scoped>
	form
	{
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: flex-end;
		gap: 10px;

		margin-bottom: 40px;
	}

	div
	{
		display: flex;
		flex-direction: column;
		align-items: flex-start;
	}

	label
	{
		font-size: 0.8rem;
		letter-spacing: 0.05em;
		padding: 4px;
	}

	input, button
	{
		font-family: var(--body-text);
		font-size: 1rem;
		color: var(--white);
		background: transparent;
		border: 2px solid var(--white);
		padding: 0 0.5ch;
		line-height: 2;
		outline: none;
	}

	input:focus,
	input:focus-within
	{
		border-color: var(--red);
	}

	button
	{
		background: var(--white);
		color: var(--black);
		cursor: pointer;
		transition: all 0.3s ease;
	}
	
	button:hover,
	button:focus
	{
		background: var(--red);
		border-color: var(--red);
	}

	@media (max-width: 830px)
	{
		form
		{
			flex-direction: column;
			align-items: flex-start;

			max-width: 400px;
			margin: 0 auto 40px;
			padding: 10px;
		}

		input, button, div
		{
			display: block;
			width: 100%;
			box-sizing: border-box;
		}
	}
</style>