export default function updateUniqueItems(map) {
    if (!(map instanceof Map)) {
    throw new Error("Cannot process");
    }

    for (const [food, quantity] of map) {
        if (quantity == 1) {
            map.set(food, 100);
        }
    }
    return map;
}