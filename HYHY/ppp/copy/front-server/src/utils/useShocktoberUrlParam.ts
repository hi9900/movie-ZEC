export function useShocktoberUrlParams() {
    const urlParams = new URLSearchParams(window.location.search)
    const userNamesFromUrl = urlParams.getAll('u') ?? []
    const listFromUrl = urlParams.get('list') ?? ''
    const monthFromUrl = parseNumberFromUrl(urlParams.get('m'))

    return {
        userName: userNamesFromUrl,
        list: listFromUrl,
        month: monthFromUrl
    }

}

function parseNumberFromUrl(value: string | null) {
    if (value === null) {
        return 10
    }
    const maybeNumber = Number(value)
    return isNaN(maybeNumber) ? 10 : maybeNumber
}