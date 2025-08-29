export default function cleanSet(set, startString) {
    if (!startString) {
    return "";
}

    const result = [];
    for (const value of set) {
        if (value.startsWith(startString)) {
            const sliced = value.slice(startString.length);
            result.push(sliced);
        }
    }
    return result.join("-");
}