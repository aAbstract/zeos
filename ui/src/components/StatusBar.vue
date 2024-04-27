<script setup lang="ts">

import { computed } from 'vue';

import { ZEOS_IP, ZEOS_HTTP_PORT } from '../lib/defines';

const zoes_backend_str = computed(() => `http://${ZEOS_IP}:${ZEOS_HTTP_PORT}`);

</script>

<template>
    <div id="status_bar_cont">
        <span id="version_text">ZEOS 1.0.0</span>
        <div style="flex-grow: 1;"></div>
        <span id="zeos_ip_text">ZEOS_BACKEND: {{ zoes_backend_str }}</span>
    </div>
</template>

<style scoped>
#zeos_ip_text {
    font-weight: bold;
    font-size: 12px;
    margin-right: 8px;
}

#version_text {
    font-weight: bold;
    font-size: 16px;
    margin-left: 8px;
}

#status_bar_cont {
    width: 100%;
    height: 24px;
    background-color: var(--font-color-light);
    color: var(--font-color-dark);
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
}
</style>