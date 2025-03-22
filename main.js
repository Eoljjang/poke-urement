document.querySelector("#search-btn").addEventListener("click", handleSearch)
const url_203 = 'https://203collectibles.com/search?q='
const url_eclipse = 'https://eclipsegames.ca/search?q='
const url_swirl = "https://swirlyeg.com/search?q="
const url_hpw = "https://hpwcards.com/search?q="
const url_prisma = "https://www.prismatcg.com/store/search/"
const url_taps = 'https://tapsgames.com/search.php?search_query='

function handleSearch(event){
    event.preventDefault();
    const inputName = document.querySelector("#input-card-name").value;
    const inputCollectionNum = document.querySelector("#input-collection-number").value;
    const inputSetName = document.querySelector("#input-set-name").value;

    search203(url_203 + encodeURIComponent(inputName))
}

async function fetch_url(queryUrl){
    
    try {
        const response = await fetch(queryUrl, {
            method: "GET", // or "POST", "PUT", etc.
            mode: "cors", // Enable CORS
        })

        if (!response.ok){
            throw new Error(`Response Status: ${response.status}`)
        }

        const json = await response.json()
        console.log(json)
    }
    catch(e){
        console.log(`Error when searching: ${e}`)
    }

}

function search203(queryUrl){
    fetch_url(queryUrl)

}