/** @odoo-module **/

import { Component, useState } from "@odoo/owl";

export class WordSearchGame extends Component {
    setup() {
        this.state = useState({
            grid: [],
            found: [],
            time: 0,
        });
        this.startTimer();
    }

    startTimer() {
        setInterval(() => {
            this.state.time++;
        }, 1000);
    }

    selectCell(letter) {
        this.state.found.push(letter);
    }
}

WordSearchGame.template = "word_search_game_template";
