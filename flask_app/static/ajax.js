const superAPI = e => {
    e.preventDefault();
    let search = document.getElementById('superAPIForm');
    let searchObject= new FormData(search);
    fetch("http://127.0.0.1:5000/get/character", {method: 'POST', body: searchObject})
    .then(res => res.json())
    .then(data =>{
        console.log(data) 
        // if(data.error){
        //     let popUp =document.querySelector("#hidden")
        //     popUp.id = '';
        //     console.log("Couldn't find by that name")
        // }
            
        
        // if(data.results.length > 10){
        //     return console.log('Too many results matched your query. Try again')}
        // const container = document.getElementById('character-container')
        // container.innerHTML = "";
        for(let i = 0; i < 5; i++){
            let cardInfo = document.createElement('div');
            cardInfo.classList.add('card', 'bg-warning', 'me-5', 'mt-4', 'text-dark', 'comics', 'details', 'border', 'border-2', 'border-dark', 'current-background');
            cardInfo.style.width = "18rem"
            let image = document.createElement('img');
            image.classList.add('card-img-top');
            image.src = data.results[i].image.url
            let characterInfo = document.createElement('ul')
            characterInfo.classList.add('list-group', 'list-group-flush' );
            characterInfo.innerHTML =`<li class="list-group-item list-group-item-action">Name: ${data.results[i].name}/${data.results[i].biography["full-name"]}</li> \n
            <li class="list-group-item list-group-item-action">First Appearance (Comic): ${data.results[i].biography["first-appearance"]}</li>
            <li class="list-group-item list-group-item-action">Publisher: ${data.results[i].biography.publisher}</li>`
            cardInfo.appendChild(image)
            cardInfo.appendChild(characterInfo)
            container.appendChild(cardInfo)
        }})
    .catch(err => console.log(err))
}