
async function getAllItems() {
    const response = await fetch(API_URL + "items/", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
        credentials: "include",
    })

    const data = await response.json();

    for (const item of data) {
        const itemElement = document.createElement("div")
        itemElement.textContent = item.name
        document.getElementById("items").appendChild(itemElement)
    }
}

async function getAllUserItems() {
    const response = await fetch(API_URL + "users/owned-items/", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
        credentials: "include",
    })

    const data = await response.json();

    for (const item of data) {
        const ownedItemElement = document.createElement("div")
        ownedItemElement.textContent = item.name
        document.getElementById("user-items").appendChild(ownedItemElement)
    }
}

getAllItems()
getCurrentUser()
getAllUserItems()