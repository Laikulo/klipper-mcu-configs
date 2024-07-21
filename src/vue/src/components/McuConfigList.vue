<script setup lang="ts">
import McuConfig from "@/components/McuConfig.vue";

const props = defineProps(['source_filename'])

const json_data = await (await fetch(props.source_filename)).json()
console.log(json_data)
</script>

<template>
 <mcu-config v-for="item in json_data" :mcu_config="item"></mcu-config>
</template>