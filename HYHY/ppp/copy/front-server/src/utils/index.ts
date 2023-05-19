export function getDaysInMonth(year: number, month: number) {
    return new Date(year, month, 0).getDate();
}

export function firstDayInMonthIndex(year: number, month: number) {
    return new Date(year, month - 1, 1).getDay()
}

export function getMonthSuffix(month: number) {
	switch (month) {
		case 1:  // same as Feb.
		case 2:  return 'uary'
		case 3:  return 'arch'
		case 4:  return 'pril'
		case 5:  return 'ay'
		case 6:  return 'une'
		case 7:  return 'uly'
		case 8:  return 'gust'
		case 9:  return 'tember'
		case 10: return 'tober'
		case 11: return 'vember'
		case 12: return 'cember'
	}
}