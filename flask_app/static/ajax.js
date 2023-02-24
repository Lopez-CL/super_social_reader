const superAPI = e => {
    e.preventDefault();
    let search = document.getElementById('superAPIForm');
    let searchObject= new FormData(search)
    fetch("http://127.0.0.1:5000/get/character", {method: 'POST', body: searchObject})
    .then(res => res.json())
    .then(data =>{
        console.log(data) 
        data.error && console.log("Couldn't find by that name")
        if(data.results.length > 3){
            console.log('Too many results matched your query. Try again')}
        const container = document.getElementById('character-container')
        container.innerHTML = "";
        for(let i = 0; i < data.results.length; i++){
            let name = data.results[i].name
            let info = document.createElement('p')
            info.innerHTML = name
            container.appendChild(info)
        }})
    .catch(err => console.log(err))
}