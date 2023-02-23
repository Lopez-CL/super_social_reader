const superAPI = e => {
    e.preventDefault();
    let search = document.getElementById('superAPIForm');
    let searchObject= new FormData(search)
    fetch("http://127.0.0.1:5000/get/character", {method: 'POST', body: searchObject})
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.log(err))
}