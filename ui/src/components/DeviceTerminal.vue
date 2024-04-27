<script setup lang="ts"></script>

<template>
    <div id="device_terminal_cont">
        <span id="prompt">(ZEOS)></span>
        <input id="inp_cmd" type="text">
    </div>
</template>

<style scoped>
#device_terminal_cont #inp_cmd {
    font-family: "Lucida Console", "Courier New", monospace;
    background-color: transparent;
    border: none;
    color: var(--font-color-light);
    flex-grow: 1;
    margin: 0 4px;
    font-size: 16px;
}

#device_terminal_cont #inp_cmd:focus {
    outline: none;
}

#device_terminal_cont #prompt {
    font-size: 12px;
    font-weight: bold;
    background-color: var(--font-color-light);
    color: var(--font-color-dark);
    padding: 4px;
}

#device_terminal_cont {
    border: 1px solid var(--font-color-light);
    height: fit-content;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    width: 100%;
}
</style>