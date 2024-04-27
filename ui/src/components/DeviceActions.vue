<script setup lang="ts"></script>

<template>
    <div id="device_actions_main_cont">
        <h4 class="box_title">DEVICE ACTIONS</h4>
        <div id="device_actions_cont">
            <button class="device_action_btn">SAVE CONF</button>
            <button class="device_action_btn">REBOOT</button>
            <button class="device_action_btn">LTD EMU</button>
            <button class="device_action_btn">ERROR PACKET</button>
        </div>
    </div>
</template>

<style scoped>
#device_actions_main_cont {
    border: 1px solid var(--font-color-light);
    width: 100%;
}

#device_actions_cont {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    margin-top: 8px;
}

.device_action_btn {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    font-family: "Orbitron", sans-serif;
    width: 80%;
    margin-bottom: 8px;
    height: 40px;
    cursor: pointer;
    background-color: transparent;
    border: 1px solid var(--font-color-light);
    color: var(--font-color-light);
    font-size: 14px;
    font-weight: bold;
    transition: 0.3s ease;
}

.device_action_btn:hover {
    color: var(--font-color-dark);
    background-color: var(--font-color-light);
}
</style>