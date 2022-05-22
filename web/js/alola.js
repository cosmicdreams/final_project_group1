// FETCH ALOLA POKEMON

const alolaPokedex = document.getElementById("alolaPokedex");

const pokeCache = {};

const fetchAlolaPokemon = () => {

    const promises = [];

    for (let i = 722; i <= 809; i++) {

        const url = `http://pokeapi.co/api/v2/pokemon/${i}`;

        promises.push(fetch(url).then((res) => res.json()));

    }

    Promise.all(promises).then((results) => {

        const pokemon = results.map((data) => ({

            id: data.id,
            name: data.name,
            image: data.sprites['front_default'],
            type: data.types.map((type) => type.type.name).join(' & '),
            height: data.height,
            weight: data.weight

        }));

        displayAlolaPokemon(pokemon);

    });

};

const displayAlolaPokemon = (pokemon) => {

    const pokemonHTMLString = pokemon.map(alolaPokemon => `
    <li class="card" onclick="selectAlolaPokemon(${alolaPokemon.id})">
        <img class="card-image" src="${alolaPokemon.image}"/>
        <h2 class="card-id">#${alolaPokemon.id}</h2>
        <h3 class="card-title">${alolaPokemon.name}</h3>
    </li>
    `).join('')

    alolaPokedex.innerHTML = pokemonHTMLString;

};

const selectAlolaPokemon = async (id) => {

    if (!pokeCache[id]) {

        const url = `http://pokeapi.co/api/v2/pokemon/${id}`;
        const res = await fetch(url);
        const alolaPokemon = await res.json();
        pokeCache[id] = alolaPokemon;
        console.log(pokeCache)
        displayPopup(alolaPokemon);

    } else {

        displayPopup(pokeCache[id]);
        
    }

};

const displayPopup = (alolaPokemon) => {

    const type = alolaPokemon.types.map((type) => type.type.name).join(' & ')

    const image = alolaPokemon.sprites['front_default'];

    const htmlString = `
    <div class="popup">
        <button id="closeBtn" onclick="closePopup()">Close</button>
        <div class="card">
            <img class="card-image" src="${image}"/>
            <h2 class="card-id">#${alolaPokemon.id}</h2>
            <h3 class="card-title">${alolaPokemon.name}</h3>
            <h4 class="card-type">${type}</h4>
            <p class="card-attribute">${alolaPokemon.height}m & ${alolaPokemon.weight}kg</p>
        </div>
    </div>
    `;
    alolaPokedex.innerHTML = htmlString + alolaPokedex.innerHTML;
    console.log(htmlString);
};

const closePopup = () => {
    const popup = document.querySelector('.popup');
    popup.parentElement.removeChild(popup);
};

fetchAlolaPokemon();