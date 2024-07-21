<script setup lang="ts">
const props = defineProps(['mcu_config'])
</script>
<template>
  <div class="mcu-config">
    <div class="title">
      <div class="config-manufacturer">{{ mcu_config['vendor'] }}</div>
      <div class="config-product">{{ mcu_config['product'] }}</div>
      <div class="config-variant" v-if="mcu_config['variant']">{{ mcu_config['variant'] }}</div>
      <div class="config-name" v-if="mcu_config['configuration'] != 'build'">{{ mcu_config['configuration'] }}</div>
    </div>
    <div class="actions">
      <div class="losenge losenge-yellow" v-if="mcu_config['provenance'] == 'community'">
        Community Supported
      </div>
      <div class="losenge losenge-green" v-else-if="mcu_config['provenance'] == 'vendor-official'">
        Vendor Official
      </div>
      <div class="losenge losenge-lightgreen" v-else-if="mcu_config['provenance'] == 'vendor-scraped'">
        From vendor docs
      </div>
      <div class="losenge" v-else>
        Unknown Origin
      </div>
      <div>
        <a :href="mcu_config['kconfig_path']">Build Configuration</a>
      </div>
    </div>
  </div>
</template>
<style scoped>
.mcu-config {
  border: 1px solid black;
  padding: .25em 1em;
}

.title {
  display: inline-block;
}

.title > div {
  display: inline-block;
  padding-right: 1em;
}

.title :last-child {
  padding-right: 0;
}

.config-product {
  font-weight: bold;
}

.losenge {
  border-radius: 4px;
  background: #333;
  color: white;
}

.losenge-yellow {
  background: gold;
  color: black;
}

.losenge-green {
  background: darkgreen;
  color: white;
}

.losenge-lightgreen {
  background: greenyellow;
  color: black;
}

.actions {
  float: right;
}

.actions > div {
  padding-left: 1em;
  padding-right: 1em;
  display: inline-block;
}
</style>