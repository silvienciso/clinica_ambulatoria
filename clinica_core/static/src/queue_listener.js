/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { session } from '@web/session';

publicWidget.registry.QueueListener = publicWidget.Widget.extend({
    selector: '.queue_container',

    start: function () {
        var self = this;
        this.fadeInOutDelay = 400;
        return this._super.apply(this, arguments).then(function () {

            self._updateQueue();

        });
    },

    _updateQueue: function () {
        var self = this;

        this.call('bus_service', 'addChannel', 'queue_channel');
        this.call('bus_service', 'subscribe', 'queue_update', this._onQueueUpdate.bind(this));

    },

    _onQueueUpdate(notification) {
        window.location.reload();
    },

    destroy() {
        super.destroy(...arguments);
    },
});

export default publicWidget.registry.QueueListener;