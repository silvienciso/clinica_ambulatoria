/** @odoo-module **/

import { browser } from "@web/core/browser/browser";
import { registry } from "@web/core/registry";
import { Component, xml } from "@odoo/owl";

export class YourCustomComponent extends Component {

    setup() {
        super.setup();
        var self = this;
        // Subscribe to the custom event
        this.call('bus_service', 'subscribe', 'your_custom_event_name', this._onBackendFieldChange.bind(this));
    }



    _onBackendFieldChange(payload) {
        console.log("Backend field changed:", payload);
        this.state.state = payload.new_value;
    }


    static template = xml`<div><p>Current value of Your Field:/></p></div>`;



    static props = {}; // Define props if your component receives data from parent

    static defaultProps = {}; // Define default props

    static components = {}; // Register any child components used

    static state = { yourFieldValue: '' }; // Define initial state

}

registry.category("actions").add("your_custom_component", YourCustomComponent);