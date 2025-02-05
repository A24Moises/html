function fetchData(){
    let random=Math.floor(Math.random()*1000) + 1
    fetch('https://api.slingacademy.com/v1/sample-data/users?offset=10&limit=1000')
    .then(response => response.json())
    .then(data => {
            let name=document.getElementById("first_name")
            let image=document.getElementById("profile_img")
            let job=document.getElementById("job")
            let phone=document.getElementById("phone")
            let city=document.getElementById("city")
            let country=document.getElementById("country")
            name.innerText=data.users[random].first_name
            image.src=data.users[random].image
            job.innerText=data.users[random].job
            phone.innerText=data.users[random].phone
            city.innerText=data.users[random].city
            country.innerText=data.users[random].country
            console.log(data)
        }
    )
    .catch(error => console.error('Error:', error));
}