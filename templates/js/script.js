/* background squares */

const ulSquares = document.querySelector("ul.squares")

for (let i = 0; i < 11; i++) {  
    const li = document.createElement("li");

    const random = (min, max) => Math.random() * (max - min) + min

    const size = Math.floor(random(10, 120)); 
    const position = random(1, 99);
    const delay = random(5, 0.1)
    const duration = random(24, 12)

    li.style.width = `${size}px`;
    li.style.height = `${size}px`;
    li.style.bottom = `-${size}px`;

    li.style.left = `${position}%`; 

    li.style.animationDelay = `${delay}s`;
    li.style.animationDuration = `${duration}s`;  
    li.style.animationTimingFunction = `cubic-bezier(${Math.random()}, ${Math.random()}, ${Math.random()}, ${Math.random()})`

    ulSquares.appendChild(li)
}

/* Create List */

let btn = document.querySelector("#btn");
let list = document.querySelector("lista");

btn.addEventListener("click", function() {
    fetch('url')
    .then(function(response) {
        return response.json();        
    })
    .then(function(response) {
        response.data.forEach(function(user) {
            let item = document.createElement("li");

            item.innerHTML = '<span>' + user.name + '<span/>'
        });
    })
})