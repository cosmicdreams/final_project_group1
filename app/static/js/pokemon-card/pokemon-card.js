import {css, html, LitElement} from 'lit';

export class PokemonCard extends LitElement {
    static properties = {
        name: {type: String},
        poketype: {type: String, reflect: true}, // Reflect = true, allows this property to show on the host.
        data: {state: true},
        hp: {state: true},
        imgSrc: {state: true},
        pokeName: {state: true},
        statAttack: {state: true},
        statDefense: {state: true},
        statSpeed: {state: true},
        themeColor: {state: true}
    };

    static styles = css`
    :host {
        --bug: #26de81;
        --dragon: #ffeaa7;
        --electric: #fed330;
        --fairy: #FF0069;
        --fighting: #30336b;
        --fire: #f0932b;
        --flying: #81ecec;
        --grass: #00b894;
        --ground: #EFB549;
        --ghost: #a55eea;
        --ice: #74b9ff;
        --normal: #95afc0;
        --poison: #6c5ce7;
        --psychic: #a29bfe;
        --rock: #2d3436;
        --water: #0190FF;
        --default: clear;
    }
    :host {
        position: relative;      
        width: 100%;
        padding: 30px 20px;
        box-shadow: 0 20px 30px rgba(0, 0, 0, 0.15);
        border-radius: 10px;
        display: block;
        background: radial-gradient(circle at 50% 0%, var(--default) 35%, 36%);
    }
    :host([poketype=electric]) {
        background: radial-gradient(circle at 50% 0%, var(--electric) 35%, #fed330 36%);
    } 
    }
    :host([poketype=bug]) {
        background: radial-gradient(circle at 50% 0%, var(--bug) 35%, ##26de81 36%);
    }
    }
    :host([poketype=dragon]) {
        background: radial-gradient(circle at 50% 0%, var(--dragon) 35%, #ffeaa7 36%);
    }
    }
    :host([poketype=fairy]) {
        background: radial-gradient(circle at 50% 0%, var(--fairy) 35%, #FF0069 36%);
    }
    }
    :host([poketype=fighting]) {
        background: radial-gradient(circle at 50% 0%, var(--fighting) 35%, ##30336b 36%);
    }
    }
    :host([poketype=fire]) {
        background: radial-gradient(circle at 50% 0%, var(--fire) 35%, #f0932b 36%);
    }
    }
    :host([poketype=flying]) {
        background: radial-gradient(circle at 50% 0%, var(--flying) 35%, #81ecec 36%);
    }
    }
    :host([poketype=grass]) {
        background: radial-gradient(circle at 50% 0%, var(--grass) 35%, #00b894 36%);
    }
    }
    :host([poketype=ground]) {
        background: radial-gradient(circle at 50% 0%, var(--ground) 35%, #EFB549 36%);
    }
    }
    :host([poketype=ghost]) {
        background: radial-gradient(circle at 50% 0%, var(--ghost) 35%, #a55eea 36%);
    }
    }
    :host([poketype=ice]) {
        background: radial-gradient(circle at 50% 0%, var(--ice) 35%, #74b9ff 36%);
    }
    }
    :host([poketype=normal]) {
        background: radial-gradient(circle at 50% 0%, var(--normal) 35%, #95afc0 36%);
    }
    }
    :host([poketype=poison]) {
        background: radial-gradient(circle at 50% 0%, var(--poison) 35%, #6c5ce7 36%);
    }
    }
    :host([poketype=psychic]) {
        background: radial-gradient(circle at 50% 0%, var(--psychic]) 35%, #a29bfe 36%);
    }
    }
    :host([poketype=rock]) {
        background: radial-gradient(circle at 50% 0%, var(--rock) 35%, #2d3436 36%);
    }
    }
    :host([poketype=water]) {
        background: radial-gradient(circle at 50% 0%, var(--water) 35%, #0190FF 36%);
    }
    }
    :host([poketype=default]) {
        background: radial-gradient(circle at 50% 0%, var(--default) 35%, white 36%);
    } 
    img {
        display: block;
        width: 180px;
        max-height: 200px; 
        position: relative;
        margin: 20px auto;
    }
    .hp {
        width: 80px;
        background-color: #ffffff;
        text-align: center;
        padding: 8px 0;
        border-radius: 30px;
        margin-left: auto;
        font-weight: 400;
    }
    .poke-name {
        text-align: center;
        font-weight: 600;
    }
    .types {
        display: flex;
        justify-content: space-around;
        margin: 20px 0 40px 0;
    }
    .hp span,
    .types span {
        font-size: 12px;
        letter-spacing: 0.4px;
        font-weight: 600;
    }
    .types span {
        padding : 5px 20px;
        border-radius: 20px;
        color: #ffffff;
    }
    .stats {
        display: flex;
        align-items: center;
        justify-content: space-between;
        text-align: center;
    }
    .stats p {
        color: #404060;
    }
    
    
    ::slotted(*) { height: 180px; margin: 0 auto; } 
    `

    constructor() {
        super();
        this.name = 'Pikachu';
        this.poketype = '';
        this.data = '';
        this.hp = '';
        this.imgSrc = '';
        this.pokeName = '';
        this.statAttack = '';
        this.statDefense = '';
        this.statSpeed = '';
    }

    async load(name) {
        const response = await fetch("https://pokeapi.co/api/v2/pokemon/" + name.toLowerCase())
        this.data = await response.json();

        this.hp = this.data.stats[0].base_stat;
        this.imgSrc = this.data.sprites.other.dream_world.front_default;
        this.pokeName = this.data.name[0].toUpperCase() + this.data.name.slice(1);
        this.statAttack = this.data.stats[1].base_stat;
        this.statDefense = this.data.stats[2].base_stat;
        this.statSpeed = this.data.stats[5].base_stat;
        this.poketype = this.data.types[0].type.name
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
          <img src=${this.imgSrc} alt="${this.pokeName}"/>
          <h2 class="poke-name">${this.pokeName}</h2>
          <div class="types">
            <span style="background-color: var(--${this.poketype}, black)">${this.poketype}</span>
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
