import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useControlsStore = defineStore('controls', () => {
	const userNames = ref('')
	const userNameList = computed(() => userNames.value.split(/(?:,| )+/))
	const listName = ref('')

	return { userNames, userNameList, listName }
})

