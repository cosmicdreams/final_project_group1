import {LitElement, html, css} from 'https://cdn.jsdelivr.net/gh/lit/dist@2/all/lit-all.min.js';

export class PokemonCard extends LitElement {
    static properties = {
        id: {},
        name: {},
    }

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

    render() {
        return html`
            <li>
                <slot>image goes here</slot>
                <h2 class="card-id">#${this.id}</h2>
                <h3 class="card-title">${this.name}</h3>
            </li>
        `;
    }
}

customElements.define('pokemon-card', PokemonCard);