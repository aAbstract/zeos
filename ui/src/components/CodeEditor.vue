<script setup lang="ts">

import { ref } from 'vue';

const code_editor_val = ref(`
let subscribers: any = {};
let requests: any = {};

export function subscribe(event_type: string, func_id: string, func: (args: any) => void) {
    if (!(event_type in subscribers))
        subscribers[event_type] = {};
    subscribers[event_type][func_id] = func;
}

export function unsubscribe(event_type: string, func_id: string) {
    delete subscribers[event_type][func_id];
    if (Object.keys(subscribers[event_type]).length === 0)
        delete subscribers[event_type];
}

export function post_event(event_type: string, args: any) {
    if (!(event_type in subscribers))
        return;
    Object.keys(subscribers[event_type]).forEach((key: string) => {
        subscribers[event_type][key](args);
    });
}

export function reg_request(req_type: string, func: (args: any) => any) {
    if (!(req_type in requests))
        requests[req_type] = func;
}

export function rm_request(req_type: string) {
    delete requests[req_type];
}

export function request(req_type: string) {
    return requests[req_type]();
}
`);

</script>

<template>
    <div id="code_editor_main_cont">
        <h4 class="box_title">CODE EDITOR</h4>
        <textarea spellcheck="false" v-model="code_editor_val"></textarea>
    </div>
</template>

<style scoped>
#code_editor_main_cont {
    border: 1px solid var(--font-color-light);
    width: 100%;
    display: flex;
    flex-direction: column;
}

#code_editor_main_cont textarea {
    font-family: "Lucida Console", "Courier New", monospace;
    background-color: transparent;
    width: calc(100% - 4px);
    flex-grow: 1;
    resize: none;
    border: none;
    color: var(--font-color-light);
    font-size: 16px;
    white-space: nowrap;
}

#code_editor_main_cont textarea:focus {
    outline: none;
}
</style>