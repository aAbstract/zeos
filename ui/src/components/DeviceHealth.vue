<script setup lang="ts">

import { computed, ref } from 'vue';

import StateTag from './StateTag.vue';

const success_color = document.documentElement.style.getPropertyValue('--color-success');
const warn_color = document.documentElement.style.getPropertyValue('--color-warn');
const error_color = document.documentElement.style.getPropertyValue('--color-error');

const cpu_util = ref('12 %');
const mem_util = ref('200 MB');
const cpu_temp = ref('50 C');
const cpu_util_font_color = computed(() => success_color);
const mem_util_font_color = computed(() => error_color);
const cpu_temp_font_color = computed(() => warn_color);



</script>

<template>
    <div id="device_health_main_cont">
        <h4 class="box_title">DEVICE HEALTH</h4>

        <div id="num_kpis_cont">
            <div class="num_kpi" :style="`color: ${cpu_util_font_color};`">
                <span class="num_kpi_lbl">CPU</span>
                <span class="num_kpi_val">{{ cpu_util }}</span>
            </div>
            <div class="num_kpi" :style="`color: ${mem_util_font_color};`">
                <span class="num_kpi_lbl">MEM</span>
                <span class="num_kpi_val">{{ mem_util }}</span>
            </div>
            <div class="num_kpi" :style="`color: ${cpu_temp_font_color};`">
                <span class="num_kpi_lbl">TEMP</span>
                <span class="num_kpi_val">{{ cpu_temp }}</span>
            </div>
        </div>

        <StateTag :label="'DEVICE_IP'" :value="'192.168.1.1'" :tag_color="warn_color" />
        
        <StateTag :label="'WIFI'" :value="'CONNECTED'" :tag_color="success_color" />
        <StateTag :label="'ZEOS_BACKEND'" :value="'CONNECTED'" :tag_color="success_color" />
        <StateTag :label="'MQTT_BROKER'" :value="'DISCONNECTED'" :tag_color="error_color" />
    </div>
</template>

<style scoped>
.num_kpi_val {
    font-weight: bold;
}

.num_kpi {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}

#num_kpis_cont {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    font-size: 16px;
    margin: 0px 8px;
    margin-bottom: 8px;
}

#device_health_main_cont {
    border: 1px solid var(--font-color-light);
    width: 100%;
}
</style>