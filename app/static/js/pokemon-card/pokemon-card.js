import {LitElement, html, css} from 'https://cdn.jsdelivr.net/gh/lit/dist@2/all/lit-all.min.js';

export class PokemonCard extends LitElement {
    const
    typeColor = {
        bug: "#26de81",
        dragon: "#ffeaa7",
        electric: "#fed330",
        fairy: "#FF0069",
        fighting: "#30336b",
        fire: "#f0932b",
        flying: "#81ecec",
        grass: "#00b894",
        ground: "#EFB549",
        ghost: "#a55eea",
        ice: "#74b9ff",
        normal: "#95afc0",
        poison: "#6c5ce7",
        psychic: "#a29bfe",
        rock: "#2d3436",
        water: "#0190FF",
    }


    static properties = {
        name: {type: String},
        data: {state: true},
        hp: {state: true},
        imgSrc: {state: true},
        pokeName: {state: true},
        statAttack: {state: true},
        statDefense: {state: true},
        statSpeed: {state: true}
    };

    static styles = css`
    li {
        list-style: none;
        padding: 40px;
        background-color: #F4F4F4;
        color: #222222;
        display: grid;
        border-radius: 5px;
        cursor: pointer;
    }
    
    li:hover {
        animation: bounce 0.5s linear;
    }
    
    .card-id {
        color: #000000;
        font-size: 20px;
        font-weight: 500;
        margin-bottom: 10px;
        height: 100px;
    }
    
    .card-title {
        font-size: 35px;
        font-weight: 600;
        text-transform: capitalize;
        margin-top: 0px;
        margin-bottom: 15px;
    }
    
    .card-type {
        font-size: 18px;
        font-weight: 400;
        text-transform: capitalize;
        margin-top: 0px;
        margin-bottom: 10px;
    }
    
    .card-attribute {
        font-size: 16px;
        font-weight: 400;
        text-transform: capitalize;
    }
    
    ::slotted(*) { height: 180px; margin: 0 auto; } 
    `

    constructor() {
        super();
        this.name = 'Pikachu';
        this.data = '';
        this.hp = '';
        this.imgSrc = '';
        this.pokeName = '';
        this.statAttack = '';
        this.statDefense = '';
        this.statSpeed = '';
    }

    async load(name) {
        const response = await fetch("https://pokeapi.co/api/v2/pokemon/" + name)
        const responseBody = await response.json()
        this.data = responseBody;

        this.hp = data.stats[0].base_stat;
        this.imgSrc = data.sprites.other.dream_world.front_default;
        this.pokeName = data.name[0].toUpperCase() + data.name.slice(1);
        this.statAttack = data.stats[1].base_stat;
        this.statDefense = data.stats[2].base_stat;
        this.statSpeed = data.stats[5].base_stat;

    }

    connectedCallback() {
        super.connectedCallback()
        this.load(this.name)
    }

    render() {
        return html`
            <p class="hp">
                <span>HP</span>
                ${this.hp}
            </p>
            <img src=${this.imgSrc} />
            <h2 class="poke-name">${this.pokeName}</h2>
            <div class="types">

            </div>
            <div class="stats">
                <div>
                    <h3>${this.statAttack}</h3>
                    <p>Attack</p>
                </div>
                <div>
                    <h3>${this.statDefense}</h3>
                    <p>Defense</p>
                </div>
                <div>
                    <h3>${this.statSpeed}</h3>
                    <p>Speed</p>
                </div>
            </div>
        `;
    }
}

customElements.define('pokemon-card', PokemonCard);