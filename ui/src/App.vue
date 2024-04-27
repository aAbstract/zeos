<script setup lang="ts">

import { onBeforeMount } from 'vue';

import StatusBar from './components/StatusBar.vue';
import FSBrowser from './components/FSBrowser.vue';
import SystemLogs from './components/SystemLogs.vue';
import CodeEditor from './components/CodeEditor.vue';
import DeviceHealth from './components/DeviceHealth.vue';
import DeviceActions from './components/DeviceActions.vue';
import DeviceTerminal from './components/DeviceTerminal.vue';

const app_theme = {
  '--background-color': '#000000',
  '--font-color-light': '#bdecf6',
  '--font-color-dark': '#112b3d',
  '--color-success': '#64DD17',
  '--color-warn': '#FFD600',
  '--color-error': '#DD2C00',
};

function load_theme(theme: Record<string, string>) {
  for (const theme_var in theme)
    document.documentElement.style.setProperty(theme_var, theme[theme_var]);
}

onBeforeMount(() => {
  load_theme(app_theme);
});

</script>

<template>
  <div id="zeos_ui_shell">
    <div id="main_cont">
      <div class="ui_main_col" style="width: 25vw;">
        <FSBrowser style="height: 100%;" />
      </div>
      <div class="ui_main_col" style="width: 50vw;">
        <SystemLogs style="flex-grow: 1; margin-bottom: 8px;" />
        <CodeEditor style="height: 50%; margin-bottom: 8px;" />
        <DeviceTerminal />
      </div>
      <div class="ui_main_col" style="width: 25vw;">
        <DeviceHealth style="height: 60%; margin-bottom: 8px;" />
        <DeviceActions style="height: 40%;" />
      </div>
    </div>
    <StatusBar />
  </div>
</template>

<style>
.ui_main_col {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: 6px;
}

.box_title {
  margin: 0px;
  padding: 8px;
  background-color: var(--font-color-light);
  color: var(--font-color-dark);
}

#main_cont {
  flex-grow: 1;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
}

#zeos_ui_shell {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

body,
html {
  width: 100%;
  height: 100%;
  margin: 0;
  background-color: var(--background-color);
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-family: "Orbitron", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: var(--font-color-light);
  width: 100%;
  height: 100%;
}

::-webkit-scrollbar {
  width: 6px;
  height: 6px;
  background-color: transparent;
}

::-webkit-scrollbar-thumb {
  background: var(--font-color-light);
  border-radius: 8px;
}

::-webkit-scrollbar-corner {
  background-color: var(--font-color-light);
}
</style>
