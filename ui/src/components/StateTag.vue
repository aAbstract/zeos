<script setup lang="ts">

defineProps<{
    label: string,
    value: string,
    tag_color: string,
}>();

</script>

<template>
    <div class="state_tag">
        <span class="state_tag_lbl">{{ label }}</span>
        <span class="state_tag_val">{{ value }}</span>
    </div>
</template>

<style scoped>
.state_tag_lbl {
    margin-left: 8px;
    font-weight: bold;
    color: v-bind(tag_color);
}

.state_tag_val {
    margin-right: 8px;
    font-weight: bold;
    color: v-bind(tag_color);
}

.state_tag {
    border: 1px solid v-bind(tag_color);
    border-left-width: 8px;
    margin: 0px 4px;
    font-size: 14px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 2px;
    margin-bottom: 8px;
}
</style>