/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { session } from '@web/session';

publicWidget.registry.QueueListener = publicWidget.Widget.extend({
    selector: '.queue_container',

    start: async function () {
        var self = this;
        this.fadeInOutDelay = 400;
        return this._super.apply(this, arguments).then(async function () {

            await self._updateQueue();

        });
    },

    _updateQueue: async function () {
        var self = this;

        this.call('bus_service', 'addChannel', 'queue_channel');
        this.call('bus_service', 'subscribe', 'queue_update', await this._onQueueUpdate.bind(this));

    },

    async _onQueueUpdate(notification) {
        const self = this;
        fetch('/queue/partial')
            .then(response => response.text())
            .then(html => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const newContent = doc.querySelector('.queue_container');
                if (newContent) {
                    const container = document.querySelector('.queue_container');
                    if (container) {
                        container.innerHTML = newContent.innerHTML;
                        this.leerTurnoActual();
                    }
                }
            });
    },

    destroy() {
        super.destroy(...arguments);
    },

    leerTurnoActual() {
        const paciente = document.querySelector(".en-consulta .paciente-name")?.innerText || "";
        const doctor = document.querySelector(".en-consulta .doctor-name")?.innerText || "";
        const especialidad = document.querySelector(".en-consulta .especialidad")?.innerText || "";

        if (paciente !== "" && doctor !== "" && especialidad !== ""){
            const texto = `Llamando a ${paciente}. Con ${doctor}, especialista en ${especialidad}.`;

            if (texto.trim() !== "") {
                const voz = new SpeechSynthesisUtterance(texto);
                voz.lang = "es-ES";
                speechSynthesis.speak(voz);
            }
        }
    }
});

export default publicWidget.registry.QueueListener;